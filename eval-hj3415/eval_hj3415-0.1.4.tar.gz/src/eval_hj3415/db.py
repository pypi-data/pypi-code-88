import numpy
import datetime
from stock_core.load_db import Corps

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


class CorpsEval(Corps):
    def __init__(self, code, col=None):
        super().__init__(code, col)

    @staticmethod
    def get_all_codes_in_db() -> list:
        return Corps.get_all_dbs()

    @staticmethod
    def chk_old_value(dv: tuple) -> float:
        """
        인자로 받은 튜플의 d를 검사해서 너무 오래된 자료는 0으로 치환한다.
        """
        d, v = dv
        logger.debug(f'd {d} v {v}')
        if d is None or d.startswith('Unna') or datetime.datetime.today().year - 1 > int(d[:4]):
            # 연도가 너무 오래된 경우 넘어간다.
            return 0
        else:
            return v

    @staticmethod
    def remove_nan(item: dict) -> dict:
        r_dict = {}
        for d, v in item.items():
            if numpy.isnan(v):
                continue
            else:
                r_dict[d] = v
        return r_dict

    def latest_value(self, title) -> float:
        # 부모클래스에서 받은 (d,v)튜플에서 d의 날짜가 오래되었는지 검사하여 실수를 반환함
        return self.chk_old_value(super().latest_value(title))

    def sum_recent_4q(self, title) -> float:
        # 부모클래스에서 받은 (d,v)튜플에서 d의 날짜가 오래되었는지 검사하여 실수를 반환함
        return self.chk_old_value(super().sum_recent_4q(title))

    def find_c103(self, page, title, leave_ratio=True) -> dict:
        # 전분기전년대비를 기본으로 남겨두고 추가로 nan을 제거한다.
        return self.remove_nan(super().find_c103(page, title, leave_ratio))

    def find_c104(self, page, title, leave_ratio=True) -> dict:
        # 전분기전년대비를 기본으로 남겨두고 추가로 nan을 제거한다.
        return self.remove_nan(super().find_c104(page, title, leave_ratio))

    def find_c106(self, period, title) -> dict:
        """
        해당 코드의 c106의 값이 nan인 경우는 빈딕셔너리로 반환한다.
        """
        d = super().find_c106(period, title)
        if len(d) == 0 or numpy.isnan(float(list(d.items())[0][1])):
            return {}
        else:
            return d

    def calc당기순이익(self) -> float:
        if len(super().find_c103('재무상태표q', '*(지배)당기순이익', leave_ratio=False)) == 0:
            # 금융관련은 재무상태표에 지배당기순이익이 없어서 손익계산서의 당기순이익에서 비지배당기순이익을 빼서 간접적으로 구한다
            self.set_col('c103손익계산서q')
            t1 = self.sum_recent_4q('당기순이익')    # 확인됨
            self.set_col('c103재무상태표q')
            t2 = self.latest_value('*(비지배)당기순이익')       # 확인됨
            return t1 + t2
        else:
            self.set_col('c103재무상태표q')
            return self.latest_value('*(지배)당기순이익')  # 확인됨

    def calc유동자산(self) -> float:
        # 유효한 유동자산 구하는 함수
        # Red와 Bluebook에서 공통사용
        self.set_col('c103재무상태표q')
        if len(super().find_c103('재무상태표q', '유동자산', leave_ratio=False)) == 0:
            # 금융관련업종...
            t1 = self.latest_value('현금및예치금')        # 확인됨
            t2 = self.latest_value('단기매매금융자산')      # 확인됨
            t3 = self.latest_value('매도가능금융자산')      # 확인됨
            t4 = self.latest_value('만기보유금융자산')      # 확인됨
            return t1 + t2 + t3 + t4
        else:
            return self.sum_recent_4q('유동자산')      # 확인됨

    def calc유동부채(self) -> float:
        # 유효한 유동부채 구하는 함수
        # Red와 Bluebook에서 공통사용
        self.set_col('c103재무상태표q')
        if len(super().find_c103('재무상태표q', '유동부채', leave_ratio=False)) == 0:
            # 금융관련업종...
            t1 = self.latest_value('당기손익인식(지정)금융부채')        # 확인됨
            t2 = self.latest_value('당기손익-공정가치측정금융부채')       # 확인됨
            t3 = self.latest_value('매도파생결합증권')              # 확인됨
            t4 = self.latest_value('단기매매금융부채')              # 확인됨
            return t1 + t2 + t3 + t4
        else:
            return self.sum_recent_4q('유동부채')       # 확인됨

    def calc비유동부채(self) -> float:
        self.set_col('c103재무상태표q')
        if len(super().find_c103('재무상태표q', '비유동부채', leave_ratio=False)) == 0:
            # 금융관련업종...
            # 보험관련업종은 예수부채가 없는대신 보험계약부채가 있다...
            t1 = self.latest_value('예수부채')                  # 확인됨
            t2 = self.latest_value('보험계약부채(책임준비금)')     # 확인됨
            t3 = self.latest_value('차입부채')                  # 확인됨
            t4 = self.latest_value('기타부채')                  # 확인됨
            return t1 + t2 + t3 + t4
        else:
            return self.sum_recent_4q('비유동부채')  # 확인됨

    def calcFCF(self) -> dict:
        # a와 b를 각 연도별로 빼주어 fcf를 구하고 리턴값으로 fcf딕셔너리를 반환한다.
        a = super().find_c103('현금흐름표y', '영업활동으로인한현금흐름', leave_ratio=False)
        b = super().find_c103('재무상태표y', '*CAPEX', leave_ratio=False)
        logger.debug(f'영업활동으로인한현금흐름 {a}')
        logger.debug(f'CAPEX {b}')
        r_dict = {}

        if len(b) == 0:
            # CAPEX가 없는 업종은 영업활동현금흐름을 그대로 사용한다.
            return a

        for i in range(len(a)):
            # a에서 아이템을 하나씩꺼내서 b 전체와 비교하여 같으면 차를 구해서 r_dict에 추가한다.
            d_a, v_a = a.popitem()
            r_dict[d_a] = v_a # 해당연도의 capex가 없는 경우도 있어 일단 capex를 0으로 치고 먼저 추가한다.
            for d_b, v_b in b.items():
                if d_a == d_b:
                    r_dict[d_a] = round(v_a - v_b, 2)
        logger.info(f'r_dict {r_dict}')
        return r_dict




