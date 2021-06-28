import math
import re
import datetime
import requests
from bs4 import BeautifulSoup

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)


def to_float(s) -> float:
    """
    인자의 예 '1432', '1,432', '23%', 1432
    인자를 실수형으로 변환하고 불가능하면 nan을 리턴한다.
    """
    def is_digit(str):
        # reference from http://seorenn.blogspot.com/2011/04/python-isdigit.html 음수 is_digit()
        try:
            tmp = float(str)
            return True
        except (ValueError, TypeError):
            return False
    logger.debug(f'to_float : {s}')

    if is_digit(s):
        return float(s)
    elif is_digit(str(s).replace(',', '').replace('%', '')):
        return float(s.replace(',', '').replace('%', ''))
    else:
        return float('nan')


def to_int(s):
    t = to_float(s)
    if math.isnan(t):
        return t
    else:
        return int(t)


def deco_num(s):
    # 숫자형 인수를 받아서 천단위에 컴마가 붙은 문자열로 반환한다.
    t = to_int(s)
    return None if s is None or math.isnan(t) else format(t, ",")


def to_억(v) -> str:
    """
    유동형식 인자를 입력받아 float으로 바꿔 nan이면 '-'리턴 아니면 '억'을 포함한 읽기쉬운 숫자 문자열로 반환
    """
    logger.debug(f'to_억 : {v}')
    float_v = to_float(v)
    if math.isnan(float_v):
        return '-'
    else:
        return str(round(float_v / 100000000, 1)) + '억'


def to_만(v) -> str:
    """
    유동형식 인자를 입력받아 float으로 바꿔 nan이면 '-'리턴 아니면 '만'을 포함한 읽기쉬운 숫자 문자열로 반환
    """
    logger.debug(f'to_만 : {v}')
    float_v = to_float(v)
    if math.isnan(float_v):
        return '-'
    else:
        return str(int(float_v / 10000)) + '만'


def str_to_date(d: str) -> datetime.datetime:
    """
    다양한 형태의 날짜 문자열을 날짜형식으로 변환
    '2021년 04월 13일'
    '2021/04/13'
    '2021-04-13'
    '2021.04.13'
    '20210413'
    """
    r = re.compile('^(20[0-9][0-9])[가-힣/.\-]?([0,1][0-9])[가-힣/.\-]?([0-3][0-9])[가-힣/.\-]?$')
    try:
        Ymd = "".join(re.findall(r, d.replace(' ', ''))[0])
    except IndexError:
        # 입력문자열이 날짜형식이 아닌경우 - ex) '-'
        return d
    return datetime.datetime.strptime(Ymd, '%Y%m%d')


def date_to_str(d: datetime.datetime, sep: str = None) -> str:
    """
    datetime 형식을 %Ysep%msep%d형식으로 반환
    """
    s = d.strftime('%Y%m%d')
    if sep is None:
        return s
    else:
        return s[0:4] + sep + s[4:6] + sep + s[6:8]


def chk_date_format_Ymd(date: str) -> bool:
    # date 형식여부 확인
    p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
    if p.match(date) is None:
        return False
    return True


def ext_latest_value(period_dict: dict) -> tuple:
    if len(period_dict) == 0:
        return '', float('nan')
    else:
        return max(period_dict.keys()), float(period_dict[max(period_dict.keys())])


def is_6digit(word: str) -> bool:
    # 파일명이 숫자6자리로 되어있는지 검사하여 참거짓 반환
    p = re.compile('^\d\d\d\d\d\d$')
    m = p.match(word)
    if m:
        return True
    else:
        return False


def scrape_simple_data(url, selector):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'From': 'hj3415@hanmail.net'
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    raw_data = soup.select(selector)[0]
    data = re.sub(r'<.+?>', '', str(raw_data).replace('\t', '').replace('\n', ''))
    return data
