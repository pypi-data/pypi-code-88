import math
import numpy
import copy
import time
import pandas as pd
from .db import CorpsEval
from krx_hj3415 import krx
from util_hj3415 import utils
from stock_core.nfscrapy import scraper
from multiprocessing import Process, cpu_count, Queue

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)

"""
- 각분기의 합이 연이 아닌 타이틀(즉 sum_4q를 사용하면 안됨)
'*(지배)당기순이익'
'*(비지배)당기순이익'
'장기차입금'
'현금및예치금'
'매도가능금융자산'
'매도파생결합증권'
'만기보유금융자산'
'당기손익-공정가치측정금융부채'
'당기손익인식(지정)금융부채'
'단기매매금융자산'
'단기매매금융부채'
'예수부채'
'차입부채'
'기타부채'
'보험계약부채(책임준비금)'
'*CAPEX'
'ROE'
"""

"""
- sum_4q를 사용해도 되는 타이틀
'자산총계'
'당기순이익'
'유동자산'
'유동부채'
'비유동부채'

'영업활동으로인한현금흐름'
'재무활동으로인한현금흐름'
'ROIC'
"""


class Eval:
    # 주식을 통한 기대수익률 - 금리가 3%일 경우 두배인 6% 정도로 잡는다.
    EXPECT_EARN = 0.04

    def __init__(self, code):
        self.code = code
        try:
            self.corp_eval_db = CorpsEval(code)
            self.corp_eval_db.set_col('c101')
            self.rc101 = self.corp_eval_db.get_recent()[0]
        except StopIteration:
            # 데이터베이스에 c101자료가 없는 경우는 직접 스크래핑을 시도한다.
            scraper.run('c101', [code, ])
            self.corp_eval_db = CorpsEval(code)
            self.corp_eval_db.set_col('c101')
            self.rc101 = self.corp_eval_db.get_recent()[0]
        logger.debug(f'rc101:{self.rc101}')
        self.name = self.rc101['종목명']
        self.marketcap = int(self.rc101['시가총액']) / 100000000
        # self.corf_df = CorpDF(code, 'c101')

    def set_code(self, code):
        self.code = code
        self.name = krx.get_name_codes()[code]
        self.corp_eval_db.set_db(code)
        self.corp_eval_db.set_col('c101')
        self.rc101 = self.corp_eval_db.get_recent()[0]
        self.marketcap = int(self.rc101['시가총액']) / 100000000

    def c101(self) -> dict:
        return self.rc101

    def c108(self) -> list:
        self.corp_eval_db.set_col('c108')
        return self.corp_eval_db.get_recent()

    def red(self) -> dict:
        지배주주당기순이익 = self.corp_eval_db.calc당기순이익()
        유동자산 = self.corp_eval_db.calc유동자산()
        유동부채 = self.corp_eval_db.calc유동부채()
        부채평가 = self.corp_eval_db.calc비유동부채()
        self.corp_eval_db.set_col('c103재무상태표q')
        투자자산 = self.corp_eval_db.latest_value('투자자산')
        투자부동산 = self.corp_eval_db.latest_value('투자부동산')

        # 사업가치 계산 - 지배주주지분 당기순이익 / 기대수익률
        사업가치 = round(지배주주당기순이익 / Eval.EXPECT_EARN, 2)

        # 재산가치 계산 - 유동자산 - (유동부채*1.2) + 고정자산중 투자자산
        재산가치 = round(유동자산 - (유동부채 * 1.2) + 투자자산 + 투자부동산, 2)

        발행주식수 = self.corp_eval_db.latest_value('발행주식수') * 1000

        try:
            red_price = round(((사업가치 + 재산가치 - 부채평가) * 100000000) / 발행주식수)
        except ZeroDivisionError:
            logger.debug(f'ZeroDivisionError : {self.code} 발행주식수 {발행주식수}')
            red_price = float('nan')

        logger.debug(f'Red Price : {red_price}원')
        return {
            'red_price': red_price,
            '사업가치': 사업가치,
            '재산가치': 재산가치,
            '부채평가': 부채평가,
            '발행주식수': 발행주식수
        }

    def mil(self) -> dict:
        def calcPFCF(fcf: dict) -> dict:
            pfcf = copy.deepcopy(fcf)
            for k, v in pfcf.items():
                if v == 0:
                    continue
                else:
                    pfcf[k] = round(self.marketcap / v, 2)
            return pfcf

        지배주주당기순이익 = self.corp_eval_db.calc당기순이익()
        self.corp_eval_db.set_col('c104q')
        roic = self.corp_eval_db.sum_recent_4q('ROIC')
        roe = self.corp_eval_db.latest_value('ROE')
        fcf_dict = self.corp_eval_db.calcFCF()
        pfcf_dict = calcPFCF(fcf_dict)
        pcr_dict = self.corp_eval_db.find_c104('q', 'PCR')
        logger.debug(f'{self.code} fcf_dict : {fcf_dict}')
        logger.debug(f"{self.code} market_cap : {self.marketcap}")
        logger.debug(f'{self.code} pfcf_dict : {pfcf_dict}')
        logger.debug(f'{self.code} pcr_dict : {pcr_dict}')
        self.corp_eval_db.set_col('c103현금흐름표q')
        재무활동현금흐름 = self.corp_eval_db.sum_recent_4q('재무활동으로인한현금흐름')
        영업활동현금흐름 = self.corp_eval_db.sum_recent_4q('영업활동으로인한현금흐름')
        주주수익률 = None if self.marketcap == 0 else round((재무활동현금흐름 / self.marketcap * -100), 2)
        이익지표 = None if self.marketcap == 0 else round((지배주주당기순이익 - 영업활동현금흐름) / self.marketcap, 5)

        return {
            '주주수익률': 주주수익률,
            '이익지표': 이익지표,
            '투자수익률': {'ROIC': roic, 'ROE': roe},
            '가치지표': {'FCF': fcf_dict, 'PFCF': pfcf_dict, 'PCR': pcr_dict}
        }

    def blue(self) -> dict:
        """
        <유동비율>
        100미만이면 주의하나 현금흐름창출력이 좋으면 괜찮을수 있다.
        만약 100%이하면 유동자산에 추정영업현금흐름을 더해서 다시계산해보아 기회를 준다.
        <이자보상배율>
        이자보상배율 영업이익/이자비용으로 1이면 자금사정빡빡 5이상이면 양호
        <순운전자금회전율>
        순운전자금 => 기업활동을 하기 위해 필요한 자금 (매출채권 + 재고자산 - 매입채무)
        순운전자본회전율은 매출액/순운전자본으로 일정비율이 유지되는것이 좋으며 너무 작아지면 순운전자본이 많아졌다는 의미로 재고나 외상이 쌓인다는 뜻
        <재고자산회전율>
        재고자산회전율은 매출액/재고자산으로 회전율이 낮을수록 재고가 많다는 이야기이므로 불리 전년도등과 비교해서 큰차이 발생하면 알람.
        재고자산회전율이 작아지면 재고가 쌓인다는뜻
        <순부채비율>
        부채비율은 업종마다 달라 일괄비교 어려우나 순부채 비율이 20%이하인것이 좋고 꾸준히 늘어나지 않는것이 좋다.
        순부채 비율이 30%이상이면 좋치 않다.
        <매출액>
        매출액은 어떤경우에도 성장하는 기업이 좋다.매출이 20%씩 늘어나는 종목은 유망한 종목
        <영업이익률>
        영업이익률은 기업의 경쟁력척도로 경쟁사에 비해 높으면 경제적해자를 갖춘셈
        """
        self.corp_eval_db.set_col('c104q')
        유동비율 = self.corp_eval_db.latest_value('유동비율')
        logger.debug(f'{self.code} 유동비율 {유동비율}')
        if 유동비율 is None or numpy.isnan(유동비율) or 유동비율 < 100:
            유동자산 = self.corp_eval_db.calc유동자산()
            유동부채 = self.corp_eval_db.calc유동부채()
            self.corp_eval_db.set_col('c103현금흐름표q')
            추정영업현금흐름 = self.corp_eval_db.sum_recent_4q('영업활동으로인한현금흐름')
            if 유동부채 == 0:
                유동비율 = None
            else:
                logger.debug(f'{self.code} 계산전 유동비율 {유동비율}')
                유동비율 = round(((유동자산 + 추정영업현금흐름) / 유동부채) * 100, 2)
                logger.debug(f'{self.code} 계산된 유동비율 {유동비율}')

        try:
            dict영업이익률 = self.corp_eval_db.find_c106('q', '영업이익률')
        except KeyError:
            dict영업이익률 = {self.name: float('nan')}
        logger.debug(f'{self.code} 영업이익률 {dict영업이익률}')

        return {
            '유동비율': 유동비율,
            '이자보상배율': self.corp_eval_db.find_c104('q', '이자보상배율'),
            '순운전자본회전율': self.corp_eval_db.find_c104('q', '순운전자본회전율'),
            '재고자산회전율': self.corp_eval_db.find_c104('q', '재고자산회전율'),
            '순부채비율': self.corp_eval_db.find_c104('q', '순부채비율'),
            '매출액증가율': self.corp_eval_db.find_c104('y', '매출액증가율'),
            '영업이익률': dict영업이익률,
        }

    def get_all(self) -> dict:
        return {
            'c101': self.c101(),
            'c108': self.c108(),
            'red': self.red(),
            'mil': self.mil(),
            'blue': self.blue(),
        }


class Score:
    def __init__(self, code):
        self.code = code
        self.eval_dict = Eval(code).get_all()

    def set_code(self, code):
        self.code = code
        self.eval_dict = Eval(code).get_all()

    def red(self) -> tuple:
        """
        red price와 최근 주가의 괴리율 파악
        양수면 주가가 고평가되어 있는 상태, 음수면 저평가
        음수가 현재 주가가 싸다는 의미
        {'red_price': 47896, '사업가치': 7127.5, '재산가치': 7152.78, '부채평가': 902.4, '발행주식수': 27931.0}
        """
        logger.info('<<<<<< score red >>>>>>')
        recent_price = utils.to_float(self.eval_dict['c101']['주가'])
        red_price = utils.to_float(self.eval_dict['red']['red_price'])
        logger.info(f"recent_price : {recent_price}\tred_price : {red_price}")
        try:
            # 괴리율 구하는 공식이 두가지임. 어떤걸 사용해도 동일함
            f1 = round((recent_price / red_price - 1) * 100, 2)
            f2 = round((recent_price - red_price) / red_price * 100, 2)
            logger.info(f'f1 : {f1}, f2 : {f2}')
            괴리율 = round((recent_price / red_price - 1) * 100, 2)
        except ZeroDivisionError:
            괴리율 = float('nan')

        logger.info(f'괴리율 : {괴리율}')
        p = 0
        if math.isnan(괴리율) or red_price <= 0:
            return p, None
        else:
            p += -math.ceil(괴리율 / 10)
        logger.info(f'point : {p}')
        return p, int(괴리율)

    def mil(self) -> tuple:
        """
        - 재무활동현금흐름이 마이너스라는 것은 배당급 지급했거나, 자사주 매입했거나, 부채를 상환한 상태임.
        - 반대는 채권자로 자금을 조달했거나 신주를 발행했다는 의미
        <주주수익률> - 재무활동현금흐름/시가총액 => 5%이상인가?

        투하자본수익률(ROIC)가 30%이상인가
        ROE(자기자본이익률) 20%이상이면 아주 우수 다른 투자이익률과 비교해볼것 10%미만이면 별로...단, 부채비율을 확인해야함.

        이익지표 ...영업현금흐름이 순이익보다 많은가 - 결과값이 음수인가..

        FCF는 영업현금흐름에서 자본적 지출(유·무형투자 비용)을 차감한 순수한 현금력이라 할 수 있다.
        말 그대로 자유롭게(Free) 사용할 수 있는 여윳돈을 뜻한다.
        잉여현금흐름이 플러스라면 미래의 투자나 채무상환에 쓸 재원이 늘어난 것이다.
        CAPEX(Capital expenditures)는 미래의 이윤을 창출하기 위해 지출된 비용을 말한다.
        이는 기업이 고정자산을 구매하거나, 유효수명이 당회계년도를 초과하는 기존의 고정자산에 대한 투자에 돈이 사용될 때 발생한다.

        잉여현금흐름이 마이너스일때는 설비투자가 많은 시기라 주가가 약세이며 이후 설비투자 마무리되면서 주가가 상승할수 있다.
        주가는 잉여현금흐름이 증가할때 상승하는 경향이 있다.
        fcf = 영업현금흐름 - capex

        가치지표평가
        price to fcf 계산
        https://www.investopedia.com/terms/p/pricetofreecashflow.asp
        pcr보다 정확하게 주식의 가치를 평가할수 있음. 10배이하 추천

        {'주주수익률': 1.27,
        '이익지표': -0.05547,
        '투자수익률': {'ROIC': 13.86, 'ROE': 9.04},
        '가치지표': {'FCF': {'2020/12': 18.98, '2019/12': 50.4, '2018/12': -54.65, '2017/12': -21.86, '2016/12': 17.48},
                    'PFCF': {'2020/12': 18.98, '2019/12': 50.4, '2018/12': -54.65, '2017/12': -21.86, '2016/12': 17.48},
                    'PCR': {'2019/12': 17.47, '2020/03': 5.65, '2020/06': 10.26, '2020/09': 13.14, '2020/12': 10.51, '전분기대비': -20.03}}}
        """
        logger.info(self.eval_dict['mil'])

        p = 0

        # 주주수익률 평가
        MAX1 = 5
        주주수익률평가 = math.ceil(self.eval_dict['mil']['주주수익률'] - (Eval.EXPECT_EARN * 100))
        주주수익률평가 = MAX1 if MAX1 < 주주수익률평가 else 주주수익률평가
        p += 주주수익률평가 if 0 < 주주수익률평가 else 0

        # 이익지표 평가
        MAX2 = 2
        p += MAX2 if self.eval_dict['mil']['이익지표'] < 0 else 0

        # 투자수익률 평가
        MAX3 = 3
        roic = self.eval_dict['mil']['투자수익률']['ROIC']
        roe = self.eval_dict['mil']['투자수익률']['ROE']
        if roic is None or math.isnan(roic) or roic <= 0:
            if 10 < roe <= 20:
                p += round(MAX3 * 0.333)
            elif 20 < roe:
                p += round(MAX3 * 0.666)
        elif 0 < roic:
            if 0 < roic <= 15:
                p += round(MAX3 * 0.333)
            elif 15 < roic <= 30:
                p += round(MAX3 * 0.666)
            elif 30 < roic:
                p += MAX3

        # PFCF 평가
        MAX4 = 10
        r_year, r_pfcf = Score.get_recent_from_c1034_dict(self.eval_dict['mil']['가치지표']['PFCF'])
        logger.info(f'recent pfcf {r_year}, {r_pfcf}')
        if r_pfcf is None or math.isnan(r_pfcf) or r_pfcf <= 0:
            pass
        else:
            p += 0 if round(MAX4 - r_pfcf) < 0 else round(MAX4 - r_pfcf)
        return p, MAX1 + MAX2 + MAX3 + MAX4

    @staticmethod
    def get_recent_from_c1034_dict(d: dict) -> tuple:
        # pfcf 같이 데이터베이스의 딕셔너리가 아니라 계산된 딕셔너리를 위해서 만듬
        d2 = copy.deepcopy(d)
        try:
            del(d2['전분기대비'])
        except KeyError:
            pass
        try:
            del(d2['전년대비'])
        except KeyError:
            pass
        try:
            r_year, r_data = sorted(d2.items(), reverse=True)[0]
        except IndexError:
            r_year, r_data = None, float('nan')
        return r_year, r_data

    def blue(self) -> tuple:
        """
        <유동비율>
        100미만이면 주의하나 현금흐름창출력이 좋으면 괜찮을수 있다.
        만약 100%이하면 유동자산에 추정영업현금흐름을 더해서 다시계산해보아 기회를 준다.
        <이자보상배율>
        이자보상배율 영업이익/이자비용으로 1이면 자금사정빡빡 5이상이면 양호
        <순운전자금회전율>
        순운전자금 => 기업활동을 하기 위해 필요한 자금 (매출채권 + 재고자산 - 매입채무)
        순운전자본회전율은 매출액/순운전자본으로 일정비율이 유지되는것이 좋으며 너무 작아지면 순운전자본이 많아졌다는 의미로 재고나 외상이 쌓인다는 뜻
        <재고자산회전율>
        재고자산회전율은 매출액/재고자산으로 회전율이 낮을수록 재고가 많다는 이야기이므로 불리 전년도등과 비교해서 큰차이 발생하면 알람.
        재고자산회전율이 작아지면 재고가 쌓인다는뜻
        <순부채비율>
        부채비율은 업종마다 달라 일괄비교 어려우나 순부채 비율이 20%이하인것이 좋고 꾸준히 늘어나지 않는것이 좋다.
        순부채 비율이 30%이상이면 좋치 않다.
        <매출액>
        매출액은 어떤경우에도 성장하는 기업이 좋다.매출이 20%씩 늘어나는 종목은 유망한 종목
        <영업이익률>
        영업이익률은 기업의 경쟁력척도로 경쟁사에 비해 높으면 경제적해자를 갖춘셈

        {'유동비율': 330.02,
        '이자보상배율': {'2019/12': 57.18, '2020/03': 45.79, '2020/06': 111.47, '2020/09': 132.58, '2020/12': 57.16, '전분기대비': -75.42},
        '순운전자본회전율': {'2019/12': 1.16, '2020/03': 1.12, '2020/06': 1.36, '2020/09': 1.2, '2020/12': 1.21, '전분기대비': 0.01},
        '재고자산회전율': {'2019/12': 2.0, '2020/03': 2.03, '2020/06': 2.11, '2020/09': 1.83, '2020/12': 1.75, '전분기대비': -0.08},
        '순부채비율': {'2019/12': -37.74, '2020/03': -43.93, '2020/06': -45.68, '2020/09': -35.82, '2020/12': -30.2, '전분기대비': 5.62},
        '매출액증가율': {'2019/12': 12.29, '2020/03': -19.6, '2020/06': 4.22, '2020/09': -4.68, '2020/12': 3.16, '전분기대비': 7.83},
        '영업이익률': {'동화약품': '10.23', '휴온스글로벌': '-74.99', '안트로젠': '6.18', '에스씨엠생명과학': '16.41', '이수앱지스': nan}}
        """

        def 유동비율평가() -> tuple:
            # 채점은 0을 기준으로 마이너스 해간다. 즉 0이 제일 좋은 상태임.
            # 유동비율 평가 - 100 이하는 문제 있음
            p = 0
            NEG_MAX = -10
            유동비율 = self.eval_dict['blue']['유동비율']
            if 유동비율 is None or math.isnan(유동비율) or 유동비율 <= 0:
                p += NEG_MAX
            else:
                p += 0 if 100 < round(유동비율) else NEG_MAX + round(유동비율/10)
            logger.info(f'point after 유동비율 : {p}')
            return p, NEG_MAX

        def 이자보상배율평가() -> tuple:
            # 이자보상배율평가 - 1이면 자금사정빡빡 5이상이면 양호
            p = 0
            NEG_MAX = -5
            r_year, r_rate = Score.get_recent_from_c1034_dict(self.eval_dict['blue']['이자보상배율'])
            logger.info(f'최근 이자보상배율 : {r_rate}')

            if r_rate is None or math.isnan(r_rate) or r_rate <= 1:
                p += NEG_MAX
            else:
                p += 0 if 5 < r_rate else NEG_MAX + round(r_rate)

            try:
                compare_prev = self.eval_dict['blue']['이자보상배율']['전분기대비']
            except KeyError:
                compare_prev = float('nan')
            if compare_prev is None or math.isnan(compare_prev) or compare_prev < 0:
                pass
            else:
                p += 0 if p == 0 else 1
            logger.info(f'point 이자보상배율 : {p}')
            return p, NEG_MAX

        def 순운전자본회전율평가() -> tuple:
            # 순운전자본회전율은 매출액/순운전자본으로 일정비율이 유지되는것이 좋으며 너무 작아지면 순운전자본이 많아졌다는 의미로 재고나 외상이 쌓인다는 뜻
            p = 0
            NEG_MAX = -5

            d = self.eval_dict['blue']['순운전자본회전율']
            logger.info(d)
            try:
                del (d['전분기대비'])
            except KeyError:
                pass
            try:
                del (d['전년대비'])
            except KeyError:
                pass

            d_values = list(d.values())
            logger.info(f'd_values : {d_values}')
            if len(d_values) == 0:
                return NEG_MAX, NEG_MAX
            std = numpy.std(d_values)
            logger.info(f'표준편차 : {std}')
            p += NEG_MAX if round(float(std)) > -NEG_MAX else -round(float(std))
            logger.info(f'point 순운전자본회전율 : {p}')
            return p, NEG_MAX

        def 재고자산회전율평가() -> tuple:
            # 재고자산회전율은 매출액/재고자산으로 회전율이 낮을수록 재고가 많다는 이야기이므로 불리 전년도등과 비교해서 큰차이 발생하면 알람.
            # 재고자산회전율이 작아지면 재고가 쌓인다는뜻
            p = 0
            NEG_MAX = -5

            d = self.eval_dict['blue']['재고자산회전율']
            logger.info(d)
            try:
                del (d['전분기대비'])
            except KeyError:
                pass
            try:
                del (d['전년대비'])
            except KeyError:
                pass

            d_values = list(d.values())
            logger.info(f'd_values : {d_values}')
            if len(d_values) == 0:
                return NEG_MAX, NEG_MAX
            std = numpy.std(d_values)
            logger.info(f'표준편차 : {std}')
            p += NEG_MAX if round(float(std)) > -NEG_MAX else -round(float(std))
            logger.info(f'point 재고자산회전율 : {p}')
            return p, NEG_MAX

        def 순부채비율평가() -> tuple:
            # 부채비율은 업종마다 달라 일괄비교 어려우나 순부채 비율이 20%이하인것이 좋고 꾸준히 늘어나지 않는것이 좋다.
            # 순부채 비율이 30%이상이면 좋치 않다.

            p = 0
            NEG_MAX = -5
            logger.info(f"순부채비율 : {self.eval_dict['blue']['순부채비율']}")
            r_year, r_rate = Score.get_recent_from_c1034_dict(self.eval_dict['blue']['순부채비율'])
            logger.info(f"최근 순부채비율 : {r_rate}")

            if r_rate is None or math.isnan(r_rate) or 80 < r_rate:
                p += NEG_MAX
            else:
                p += 0 if r_rate < 30 else round((30 - r_rate)/10)

            try:
                compare_prev = self.eval_dict['blue']['순부채비율']['전분기대비']
            except KeyError:
                compare_prev = float('nan')
            logger.info(f"전분기대비 : {compare_prev}")

            if compare_prev is None or math.isnan(compare_prev) or 0 < compare_prev:
                pass
            else:
                p += 0 if p == 0 else 1
            logger.info(f'point 순부채비율 : {p}')
            return p, NEG_MAX

        def 매출액증가율평가() -> tuple:
            # 매출액은 어떤경우에도 성장하는 기업이 좋다.매출이 20%씩 늘어나는 종목은 유망한 종목
            p = 0
            매출액증가율 = self.eval_dict['blue']['매출액증가율']
            try:
                del (매출액증가율['전분기대비'])
            except KeyError:
                pass
            try:
                del (매출액증가율['전년대비'])
            except KeyError:
                pass
            logger.info(f"매출액증가율 : {self.eval_dict['blue']['매출액증가율']}")

            d_values = list(매출액증가율.values())
            logger.info(f'd_values : {d_values}')
            if len(d_values) == 0:
                return p, float('nan')
            my_mean = round(float(numpy.mean(d_values)))
            # std = round(numpy.std(d_values))
            logger.info(f'평균 : {my_mean}')
            # logger.info(f'표준편차 : {std}')
            p += 0 if my_mean < 0 else round(my_mean / 10)
            logger.info(f'point 매출액증가율 : {p}')
            return p, my_mean

        def 영업이익률평가() -> int:
            # 영업이익률은 기업의 경쟁력척도로 경쟁사에 비해 높으면 경제적해자를 갖춘셈
            p = 0
            영업이익률 = copy.deepcopy(self.eval_dict['blue']['영업이익률'])
            logger.info(f"영업이익률 : {영업이익률}")

            corp_eval_db = CorpsEval(self.code)
            corp_eval_db.set_col('c101')
            name = corp_eval_db.get_recent()[0]['종목명']

            try:
                profit1 = utils.to_float(영업이익률.pop(name))
            except KeyError:
                return 0
            logger.info(f'영업이익률1 : {profit1}')

            for profit in 영업이익률.values():
                profit = utils.to_float(profit)
                if profit is None or math.isnan(profit):
                    continue
                elif profit1 > profit:
                    p += 1
                else:
                    continue

            logger.info(f'point 영업이익률 : {p}')
            return p

        def calc_neg_total() -> tuple:
            p1, m1 = 유동비율평가()
            p2, m2 = 이자보상배율평가()
            p3, m3 = 순운전자본회전율평가()
            p4, m4 = 재고자산회전율평가()
            p5, m5 = 순부채비율평가()
            return p1 + p2 + p3 + p4 + p5, m1 + m2 + m3 + m4 + m5

        def calc_pos_total() -> tuple:
            p1, m = 매출액증가율평가()
            p2 = 영업이익률평가()
            return p1 + p2, m

        neg_p, TOTAL_NEG_MAX = calc_neg_total()
        pos_p, mean = calc_pos_total()

        logger.info(f'neg point : {neg_p}/{TOTAL_NEG_MAX}\t pos point : {pos_p} 평균매출액증가율{mean}')
        return neg_p, TOTAL_NEG_MAX, pos_p, mean


class ReportOne:
    """
    Eval 클래스와 Score 클래스를 같이 계산하여 다양한 방식의 출력구조에 맞춰 형식을 반환한다.
    즉 Eval 과 Score 를 외부에서 직접 사용할 필요 없이 ReportOne 클래스를 사용한다.
    """
    seperate_line = '\n' + ('-' * 65) + '\n'

    def __init__(self, code: str):
        self.code = code
        s = Score(code)
        self.eval_dict = s.eval_dict
        self.red_scores = s.red()
        self.mil_scores = s.mil()
        self.blue_scores = s.blue()

    @staticmethod
    def deco_num(x: str) -> str:
        # 숫자의 세자리마다 콤마를 붙여 읽기 쉽게 만들어 준다.
        return None if x is None or math.isnan(float(x)) else format(int(x), ",")

    def for_console(self) -> str:
        def c101_str() -> str:
            c101d = self.eval_dict['c101']
            logger.info(c101d)
            title = '=' * 35 + f"\t{c101d['코드']}\t\t{c101d['종목명']}\t\t{c101d['업종']}\t" + '=' * 35
            import textwrap
            intro = textwrap.fill(f"{c101d['intro']}", width=70)
            price = (f"{c101d['date']}\t\t"
                     f"주가: {self.deco_num(c101d['주가'])}원\t\t"
                     f"52주최고: {self.deco_num(c101d['최고52주'])}원\t"
                     f"52주최저: {self.deco_num(c101d['최저52주'])}원")
            info = (f"PER: {c101d['PER']}\t\t"
                    f"PBR: {c101d['PBR']}\t\t\t"
                    f"배당수익률: {c101d['배당수익률']}%\t\t"
                    f"시가총액: {self.deco_num(c101d['시가총액'])}억\n"
                    f"업종PER: {c101d['업종PER']}\t"
                    f"유통비율: {c101d['유통비율']}%\t\t"
                    f"거래대금: {utils.to_억(c101d['거래대금'])}원\t"
                    f"발행주식: {utils.to_만(c101d['발행주식'])}주")
            return title + '\n' + intro + self.seperate_line + price + '\n' + info

        def red_str() -> str:
            red, 괴리율 = self.red_scores
            red_dict = self.eval_dict['red']
            logger.info(red_dict)
            return (f"Red Price\tPoint({red})\n"
                    f"사업가치({self.deco_num(red_dict['사업가치'])}억) "
                    f"+ 재산가치({self.deco_num(red_dict['재산가치'])}억) "
                    f"- 부채({self.deco_num(red_dict['부채평가'])}억) "
                    f"/ 발행주식({utils.to_만(red_dict['발행주식수'])}주) "
                    f"= {self.deco_num(red_dict['red_price'])}원")

        def mil_str() -> str:
            mil, MAX = self.mil_scores
            mil_dict = self.eval_dict['mil']
            logger.info(mil_dict)
            return (f"Millenial\tPoint({mil}/{MAX})\n"
                    f"1. 주주수익률: {mil_dict['주주수익률']} %\n"
                    f"2. 이익지표: {mil_dict['이익지표']}\n"
                    f"3. 투자수익률: ROIC 4분기합: {mil_dict['투자수익률']['ROIC']}%, 최근 ROE: {mil_dict['투자수익률']['ROE']}%\n"
                    f"4. 가치지표\n"
                    f"\tFCF: {mil_dict['가치지표']['FCF']}\n"
                    f"\tPFCF : {mil_dict['가치지표']['PFCF']}\n"
                    f"\tPCR: {mil_dict['가치지표']['PCR']}")

        def blue_str() -> str:
            neg_p, NEG_MAX, pos_p, mean = self.blue_scores
            blue_dict = self.eval_dict['blue']
            logger.info(blue_dict)
            return (f"Blue\t - Point({neg_p}/{NEG_MAX})\t+ Point({pos_p})\n"
                    f"1. 유동비율: {blue_dict['유동비율']}(100이하 위험)\n"
                    f"2. 이자보상배율: {blue_dict['이자보상배율']}(1이하 위험 5이상 양호)\n"
                    f"3. 순운전자본회전율: {blue_dict['순운전자본회전율']}\n"
                    f"4. 재고자산회전율: {blue_dict['재고자산회전율']}\n"
                    f"5. 순부채비율: {blue_dict['순부채비율']}(30이상 not good)\n"
                    f"6. 매출액증가율: {blue_dict['매출액증가율']}\n"
                    f"\t평균매출액증가율: {mean}\n"
                    f"7. 영업이익률: {blue_dict['영업이익률']}")

        def c108_str() -> str:
            s = ''
            for i, c108_dict in enumerate(self.eval_dict['c108']):
                logger.info(c108_dict)
                opinion = c108_dict['내용'].replace('▶', '\n\t')
                if i == 0:
                    pass
                else:
                    s += '\n'
                s += f"{c108_dict['날짜']}\thprice : {c108_dict['목표가']} 원\n<<{c108_dict['제목']}>>{opinion}"
            return s

        return (c101_str() + self.seperate_line
                + red_str() + self.seperate_line
                + mil_str() + self.seperate_line
                + blue_str() + self.seperate_line
                + c108_str() + self.seperate_line)

    def for_telegram(self) -> str:
        def c101_str() -> str:
            c101d = self.eval_dict['c101']
            logger.info(c101d)
            title = '=' * 35 + f"\t{c101d['코드']}\t\t{c101d['종목명']}\t\t{c101d['업종']}\t" + '=' * 35

            intro = f"{c101d['intro']}"
            price = (f"<< {c101d['date']} >>\n"
                     f"주가: {self.deco_num(c101d['주가'])}원\n"
                     f"52주최고: {self.deco_num(c101d['최고52주'])}원\n"
                     f"52주최저: {self.deco_num(c101d['최저52주'])}원")
            info = (f"PER: {c101d['PER']}\n"
                    f"업종PER: {c101d['업종PER']}\n"
                    f"PBR: {c101d['PBR']}\n"
                    f"배당수익률: {c101d['배당수익률']}%\n"
                    f"유통비율: {c101d['유통비율']}%\n"
                    f"거래대금: {utils.to_억(c101d['거래대금'])}원\n"
                    f"발행주식: {utils.to_만(c101d['발행주식'])}주\n"
                    f"시가총액: {self.deco_num(c101d['시가총액'])}억")
            return title + '\n' + intro + self.seperate_line + price + '\n' + info

        def red_str() -> str:
            red, 괴리율 = self.red_scores
            red_dict = self.eval_dict['red']
            logger.info(red_dict)
            return (f"<< Red Price >> Point({red})\n"
                    f"{self.deco_num(red_dict['red_price'])}원\n"
                    f"괴리율({괴리율}%)")

        def mil_str() -> str:
            mil, MAX = self.mil_scores
            mil_dict = self.eval_dict['mil']
            logger.info(mil_dict)
            return (f"<< Millenial >> Point({mil}/{MAX})\n"
                    f"1. 주주수익률: {mil_dict['주주수익률']} %\n"
                    f"2. 이익지표: {mil_dict['이익지표']}\n"
                    f"3. 투자수익률\nROIC 4분기합: {mil_dict['투자수익률']['ROIC']}%\n최근 ROE: {mil_dict['투자수익률']['ROE']}%\n"
                    f"4. 가치지표\n"
                    f"FCF\n{mil_dict['가치지표']['FCF']}\n"
                    f"PFCF\n{mil_dict['가치지표']['PFCF']}\n"
                    f"PCR\n{mil_dict['가치지표']['PCR']}")

        def blue_str() -> str:
            neg_p, NEG_MAX, pos_p, mean = self.blue_scores
            blue_dict = self.eval_dict['blue']
            logger.info(blue_dict)
            return (f"<< Blue >>\n"
                    f"Neg_P: {neg_p}/{NEG_MAX}\n"
                    f"Pos_P: {pos_p}\n"
                    f"평균매출액증가율: {mean}%\n"
                    f"영업이익률\n{blue_dict['영업이익률']}")

        def c108_str() -> str:
            s = ''
            for i, c108_dict in enumerate(self.eval_dict['c108']):
                logger.info(c108_dict)
                opinion = c108_dict['내용'].replace('▶', '\n\t')
                if i == 0:
                    pass
                else:
                    s += '\n'
                s += f"{c108_dict['날짜']}\thprice : {c108_dict['목표가']} 원\n<<{c108_dict['제목']}>>{opinion}"
            return s

        return (c101_str() + self.seperate_line
                + red_str() + self.seperate_line
                + mil_str() + self.seperate_line
                + blue_str() + self.seperate_line
                + c108_str() + self.seperate_line)

    def for_django(self) -> dict:
        """
        장고의 view context는 딕셔너리 형식이기 때문에 딕셔너리 모음으로 반환한다.
        """
        return {
            'c101': self.eval_dict['c101'],
            'red': self.eval_dict['red'],
            'mil': self.eval_dict['mil'],
            'blue': self.eval_dict['blue'],
            'c108': self.eval_dict['c108'],
            'red_s': self.red_scores,
            'mil_s': self.mil_scores,
            'blue_s': self.blue_scores,
        }

    def for_table(self) -> dict:
        # 장고에서 사용할 eval 테이블을 만들기 위해 각각의 레코드를 구성하는 함수
        logger.debug(f"code: {self.eval_dict['c101']['코드']}")
        logger.debug(f"PFCF : {self.eval_dict['mil']['가치지표']['PFCF']}")
        logger.debug(f"PCR : {self.eval_dict['mil']['가치지표']['PCR']}")
        return {
            'code': self.eval_dict['c101']['코드'],
            '종목명': self.eval_dict['c101']['종목명'],
            '주가': utils.to_int(self.eval_dict['c101']['주가']),
            'PER': utils.to_float(self.eval_dict['c101']['PER']),
            'PBR': utils.to_float(self.eval_dict['c101']['PBR']),
            '시가총액': utils.to_float(self.eval_dict['c101']['시가총액']),
            'RED': utils.to_int(self.eval_dict['red']['red_price']),
            '주주수익률': utils.to_float(self.eval_dict['mil']['주주수익률']),
            '이익지표': utils.to_float(self.eval_dict['mil']['이익지표']),
            'ROIC': utils.to_float(self.eval_dict['mil']['투자수익률']['ROIC']),
            'ROE': utils.to_float(self.eval_dict['mil']['투자수익률']['ROE']),
            'PFCF': utils.to_float(utils.ext_latest_value(self.eval_dict['mil']['가치지표']['PFCF'])),
            'PCR': utils.to_float(utils.ext_latest_value(self.eval_dict['mil']['가치지표']['PCR'])),
        }


def _make_df_part(codes: list, q):
    t = len(codes)
    d = []
    for i, code in enumerate(codes):
        print(f'{i+1}/{t} {code}')
        try:
            d.append(ReportOne(code).for_table())
        except:
            logger.error(f'{code} / {ReportOne(code).for_table()}')
            continue
    df = pd.DataFrame(d)
    logger.debug(df)
    q.put(df)


def make_eval_df_all() -> pd.DataFrame:
    def _code_divider(entire_codes: list) -> tuple:
        # 전체 종목코드를 리스트로 넣으면 cpu 코어에 맞춰 나눠준다.
        # reference from https://stackoverflow.com/questions/19086106/how-to-utilize-all-cores-with-python-multiprocessing
        def _split_list(alist, wanted_parts=1):
            # 멀티프로세싱할 갯수로 리스트를 나눈다.
            # reference from https://www.it-swarm.dev/ko/python/%EB%8D%94-%EC%9E%91%EC%9D%80-%EB%AA%A9%EB%A1%9D%EC%9C%BC%EB%A1%9C-%EB%B6%84%ED%95%A0-%EB%B0%98%EC%9C%BC%EB%A1%9C-%EB%B6%84%ED%95%A0/957910776/
            length = len(alist)
            return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                    for i in range(wanted_parts)]

        core = cpu_count()
        print(f'Get number of core for multiprocessing : {core}')
        n = core - 1
        if len(entire_codes) < n:
            n = len(entire_codes)
        print(f'Split total {len(entire_codes)} codes by {n} parts ...')
        divided_list = _split_list(entire_codes, wanted_parts=n)
        return n, divided_list

    codes = CorpsEval.get_all_codes_in_db()

    print('*' * 25, f"Eval all using multiprocess", '*' * 25)
    print(f'Total {len(codes)} items..')
    logger.info(codes)
    n, divided_list = _code_divider(codes)

    start_time = time.time()
    q = Queue()
    ths = []
    for i in range(n):
        ths.append(Process(target=_make_df_part, args=(divided_list[i], q)))
    for i in range(n):
        ths[i].start()
    df_list = []
    for i in range(n):
        df_list.append(q.get())
    # 부분데이터프레임들을 하나로 합침
    final_df = pd.concat(df_list, ignore_index=True)
    for i in range(n):
        ths[i].join()
    print(f'Total spent time : {round(time.time() - start_time, 2)} sec.')
    logger.debug(final_df)
    return final_df


def eval_spac():
    codes = CorpsEval.get_all_codes_in_db()
    logger.warning(f'len(codes) : {len(codes)}')
