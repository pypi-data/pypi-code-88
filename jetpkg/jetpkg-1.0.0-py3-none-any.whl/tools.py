#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2020/12/7 14:12
@Author   : ji hao ran
@File     : tools.py
@Project  : jetCloud
@Software : PyCharm
"""
from typeguard import typechecked
from typing import Union, Iterable, Iterator
import inspect
import re
import time
import functools
import pandas as pd
from pandas import DataFrame, Timestamp
import numpy as np
import simplejson as json
import requests
import sqlalchemy
from functools import partial, reduce
from itertools import product
from tqdm import tqdm
from pathos.pools import ProcessPool, ThreadPool
import warnings

"""
jetCloud项目工具箱模块，包括数据源获取，格式转换，自定义装饰器，以及各种自定义函数。
"""
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


def parallel_map(func, *iterables, thread: bool = False, **kwargs) -> list:
    """
    map函数的并行计算版本

    :param func: 并行函数
    :param iterables: func的位置参数
    :param thread: 是否为多线程
    :param kwargs: func的关键字参数
    :return: 与位置参数等长的列表
    """

    # 冻结位置参数
    p_func = partial(func, **kwargs)
    # 打开进程/线程池
    pool = ThreadPool() if thread else ProcessPool()
    try:
        start = time.time()
        # imap方法
        with tqdm(total=len(iterables[0]), desc="进度") as t:  # 进度条设置
            r = []
            for i in pool.imap(p_func, *iterables):
                r.append(i)
                t.set_postfix({'函数': func.__name__, "用时": f"{time.time() - start:.0f}秒"})
                t.update()
        return r
    except Exception as e:
        print(e)
    finally:
        # 关闭池
        pool.close()  # close the pool to any new jobs
        pool.join()  # cleanup the closed worker processes
        pool.clear()  # Remove server with matching state


class Decorator:
    """装饰器"""

    @staticmethod
    def time_cost(func):
        """
        统计函数计算花销装饰器，单位秒
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = pd.Timestamp.now()
            r = func(*args, **kwargs)
            print(f"函数：{func.__name__}，用时：{(pd.Timestamp.now() - start).seconds:.0f}秒")
            return r

        return wrapper


class Jet:
    """
    jet基类
    """

    def __new__(cls, *args, **kwargs):
        """为类添加参数检查功能"""
        return super().__new__(typechecked(cls))

    @staticmethod
    def color_str(obj: str, forecolor: str = None, backcolor: str = None) -> str:
        """给字符添加颜色显示属性

        :param obj: 字符对象
        :param forecolor: 前景色[black,red,green,yellow,orange,purple,blue,gray],默认不设置
        :param backcolor: 背景色,与前景色相同，默认不设置
        :return: 拥有颜色属性的字符
        """
        forecolor_dict = {
            'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'orange': 34, 'purple': 35, 'blue': 36, 'gray': 37
        }
        backcolor_dict = {
            'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'orange': 44, 'purple': 45, 'blue': 46, 'gray': 47
        }
        fore = forecolor_dict.get(forecolor)
        back = backcolor_dict.get(backcolor)
        if fore is None and back is None:  # 都不添加
            return obj
        elif fore and back:  # 添加前景色和背景色
            return f"\033[0;{fore};{back};1m{obj}\033[0m"
        elif fore:  # 只添加前景色
            return f"\033[0;{fore};1m{obj}\033[0m"
        else:  # 只添加背景色
            return f"\033[0;;{back};1m{obj}\033[0m"

    @staticmethod
    def merge_dict(*args: dict) -> dict:
        """合并多个字典

        :param args: 字典
        :return: 合并后的字典，重复key会覆盖
        """
        return dict(reduce(lambda l1, l2: l1 + l2, map(lambda d: list(d.items()), args)))

    @staticmethod
    def filter_dict(obj: dict, conf: str = None) -> dict:
        """字典筛选过滤

        :param obj: 字典
        :param conf: 过滤条件语句，字典的key用k表示，value用v表示
        :return: 筛选后的字典
        """
        if conf:
            if 'k' not in conf and 'v' not in conf:
                raise ValueError(f'parameter "filter" need contain "k" or "v"!')
            return {k: v for k, v in obj.items() if (lambda k, v: eval(conf))(k, v)}
        else:
            return obj

    @staticmethod
    def flat(obj) -> list:
        """扁平化嵌套序列

        :param obj: 序列
        :return: 扁平化后的列表
        """
        return list(pd.core.common.flatten(obj))

    @staticmethod
    def groupbyprod(*args: DataFrame):
        """数据框按行求笛卡尔积分组

        :param args: 多个数据框
        :return: 分组数据框
        """
        # reset index
        # _df = [v.set_index(v.index.map(lambda x: f'{i}{sep}{x}')) for i, v in enumerate(args)]
        # merge dataframe
        _merge = pd.concat(args)
        # product all dataframe index
        _prod = list(product(*map(lambda x: x.T, args)))
        # repeat index
        _repeat = np.repeat(_prod, len(args), axis=0)
        # sub dataframe
        _sub_df = _merge.loc[[j for i in _prod for j in i]]
        # rename index sub dataframe
        _sub_df.set_axis(_repeat, inplace=True)
        # group
        g_df = _sub_df.groupby(level=0)
        return g_df

    @staticmethod
    def check_df(*args: DataFrame, row: int = None, col: int = None):
        """
        检查数据框是否合法

        :param args: 数据框
        :param row: 行数目标值
        :param col: 列数目标值
        :return: True数据框合法
        """
        legal = list()
        for i in args:
            if i.empty:
                legal.append(False)
            else:
                is_row = False if row and i.shape[0] != row else True
                is_col = False if col and i.shape[1] != col else True
                legal.append(all([is_row, is_col]))
        if all(legal):
            return True
        else:
            print('DataFrame is illegal!')
            return False

    def check(self, *statement: str, scope=None, silent=False):
        """条件语句检查

        :param statement: 约束条件语句
        :param scope: 约束条件作用域
        :param silent: 不满足约束条件时，是否保存，默认报错
        :return: True,满足约束条件；False,不满足约束条件
        """
        scope = scope if scope else locals()
        result = []
        for s in statement:
            try:
                r = eval(s, globals(), scope)
            except Exception:
                raise Exception
            if not r and not silent:
                raise ValueError(f'{self.meta} statement "{s}" not satisfied')
            result.append(r)
        return True if all(result) else False

    @property
    def _msg(self):
        """信息"""
        class_name = self.__class__.__name__
        now = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{now} {class_name}'

    @property
    def meta(self):
        """运行头信息"""
        return f'{self._msg} {inspect.stack()[1][3]}'

    @property
    def fail(self):
        """运行失败信息"""
        return f'{self._msg} {inspect.stack()[1][3]} {self.color_str("Fail", forecolor="red")}'

    @property
    def success(self):
        """运行成功信息"""
        return f'{self._msg} {inspect.stack()[1][3]} {self.color_str("Success", forecolor="green")}'


class JetEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        重写json模块JSONEncoder类中的default方法
        """
        # pandas naive Timestamp类型数据转为毫秒时间戳
        if isinstance(obj, pd.Timestamp):
            return JetTimeStamp(obj).ms
        # np整数转为内置int
        elif isinstance(obj, np.integer):
            return int(obj)
        # np浮点数转为内置float
        elif isinstance(obj, np.floating):
            return float(obj)
        # 字节串转为字符串
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        # series转list
        elif isinstance(obj, pd.Series):
            return obj.to_list()
        else:
            # return json.JSONEncoder.default(obj)
            return super().default(obj)


class JetTimeStamp(Jet):
    # 本地时区
    tz = 'Asia/shanghai'
    # 相对时间偏移和对齐字符模式
    pattern = '-?\\d*[A-Z]'
    # 相对时间允许模式
    allow_pattern = [pattern, pattern + ':', ':' + pattern, pattern + ':' + pattern]

    def __init__(self, obj: Union[float, str, Timestamp, np.integer] = None, **kwargs):
        """
        jet自定义时间戳格式，可转各种自定义时间格式为时间戳。
        支持输入：
        1. numpy integer/int/float: 绝对时间
        2. str: 绝对时间：'%Y%m%d%H:%M:%S',相对时间：'-3D:-H'
        3. None: 当前时间
        4. pd.TimeStamp: 绝对时间

        :param obj: 时间，JetTimeStamp支持的输入类型
        :param kwargs: 时间的其他关键字参数,绝对时间时，为TimeStamp的关键字参数，相对时间时为base,相对时间的基准
        """
        self.obj = obj
        self.kwargs = kwargs
        self.now = pd.Timestamp.now(self.tz)

    def __str__(self):
        return self.ts.__str__()

    def _get_number_unit(self, value: str, offset=True):
        """
        获取offset/align value字符串中的数值和单位
        :param value: 字符串
        :param offset: 是否是偏移字符串
        :return:
        """
        # 负号
        minus_str = re.findall('^-', value)
        # 数值
        n_str = re.findall('\\d+', value)
        # 单位
        u_str = re.findall('[A-Z]$', value)
        # 单位检查
        self._unit_check(u_str[0], offset)
        # 无数值设置为1
        n = int(n_str[0]) if n_str else 1
        # 有负号添加负号
        n = -n if minus_str else n
        # 更新value
        value_update = str(n) + u_str[0]
        # 返回
        return n, value_update

    @staticmethod
    def _unit_check(unit: str, offset=True):
        """
        对单位做检查
        :param unit:
        :param offset:
        :return: 错误信息
        """
        offset_unit = ['T', 'H', 'D', 'W', 'M', 'Y']
        align_unit = ['T', 'H', 'D', 'M', 'Y']
        if offset:
            if unit not in offset_unit:
                raise ValueError('OFFSET unit must be one of {},bug get {} !'.format(str(offset_unit), unit))
        else:
            if unit not in align_unit:
                raise ValueError('ALIGN unit must be one of {},bug get {} !'.format(str(align_unit), unit))

    def _add_offset(self, x, offset_value: str):
        """
        给基准时间x增加偏移量
        :param x: pandas TimeStamp,基准时间
        :param offset_value: 偏移量
        :return:
        """
        offset_n, offset_value = self._get_number_unit(offset_value)
        if 'M' in offset_value:
            x_offset = x + pd.DateOffset(months=offset_n)
        else:
            x_offset = x + pd.Timedelta(offset_value)
        return x_offset

    def _add_align(self, x, align_value: str):
        """
        对时间x对齐操作
        :param x: pandas TimeStamp,时间
        :param align_value: 对齐量
        :return:
        """
        align_n, align_value = self._get_number_unit(align_value, offset=False)
        if align_n < 0:
            if 'M' in align_value:
                x_align = x.date() + pd.offsets.MonthBegin(align_n)
            elif 'Y' in align_value:
                x_align = x.date() + pd.offsets.YearBegin(align_n)
            else:
                x_align = x.ceil(align_value)
        else:
            if 'M' in align_value:
                x_align = x.date() + pd.offsets.MonthEnd(align_n)
            elif 'Y' in align_value:
                x_align = x.date() + pd.offsets.YearEnd(align_n)
            else:
                x_align = x.ceil(align_value)
        return x_align

    def _absolute(self, obj, **kwargs):
        """
        绝对时间转为时间戳
        :param obj: 绝对时间
        :return: 毫秒时间戳
        """
        if isinstance(obj, (float, int, np.integer)):
            digits = len(int(obj).__str__())
            if digits == 10:  # 秒
                return pd.Timestamp(obj, unit='s', tz=self.tz)
            elif digits == 13:  # 毫秒
                return pd.Timestamp(obj, unit='ms', tz=self.tz)
            else:
                return pd.Timestamp(obj, tz=self.tz, **kwargs)
        elif isinstance(obj, pd.Timestamp):
            if obj.tz:
                return obj
            else:
                return pd.Timestamp(obj, tz=self.tz, **kwargs)
        elif isinstance(obj, str):
            return pd.Timestamp(obj, tz=self.tz, **kwargs)

    def _relative(self, obj: str, **kwargs):
        """
        相对时间转为时间戳
        :param obj: 相对时间字符串，'-3D:-H'
        :param kwargs: base,相对时间基准
        :return: 毫秒时间戳
        """
        # 输入模式判断
        if not any([re.fullmatch(i, obj) for i in self.allow_pattern]):
            raise ValueError(f'string pattern not supported,got {obj}\nallow pattern{self.allow_pattern}')
        else:
            # 相对时间基准(默认当前时间)
            base = self._absolute(kwargs.get('base')) if kwargs.get('base') else self.now
            # 添加分隔符
            obj = obj if ':' in obj else obj + ":"
            # 提取value
            offset_value, align_value = re.split(':', obj)
            # 增加偏移
            offset = self._add_offset(base, offset_value) if offset_value else base
            # 增加对齐
            align = self._add_align(offset, align_value) if align_value else offset
            return align

    @property
    def ts(self):
        """
        :return: pandas TimeStamp时间戳
        """
        # 1.输入为空
        if self.obj is None:
            ts = self.now
        # 2.输入为字符
        elif isinstance(self.obj, str):
            if re.findall('[a-zA-Z]', self.obj):  # 包含字母则为相对时间
                ts = self._relative(self.obj, **self.kwargs)
            else:  # 绝对时间
                ts = self._absolute(self.obj, **self.kwargs)
        # 3.输入为数值或pd.TimeStamp
        else:
            # 绝对时间
            ts = self._absolute(self.obj, **self.kwargs)
        return ts

    @property
    def ms(self):
        """
        :return: 毫秒
        """
        return int(self.ts.timestamp() * 1e3)


class Mysql(Jet):
    """
    MySQL数据库操作，读取，写入
    """

    def __init__(self, host: str = None, port: int = 3306, user: str = None, pw: str = None, name: str = None):
        """

        :param host: 数据库地址
        :param port: 端口
        :param user: 用户名
        :param pw: 密码
        :param name: 数据库名称
        """

        self.host = host if host else "192.168.1.56"
        self.port = port
        self.user = user if user else 'root'
        self.pw = pw if pw else 'jizhongjieneng9-28'
        self.name = name if name else 'jet_huawei_dev'
        # 数据库连接
        self.connect = f'mysql+pymysql://{self.user}:{self.pw}@{self.host}:{self.port}/{self.name}?charset=utf8'

    def insert(self, obj: Union[DataFrame, dict], table_name: str, if_exists='append'):
        """
        向mysql数据库写入数据函数

        :param obj: 数据
        :param table_name: 表格名字
        :param if_exists: 表格存在插入模式，默认追加，可选[fail,append,replace]
        :return:
        """
        if obj is None:
            print(f'{self.fail}(empty)')
        else:
            try:
                # 创建连接
                con = sqlalchemy.create_engine(self.connect)
                # 转为dataFrame，若数据库中无表，则自动创建。选择存在则追加模式。
                if isinstance(obj, dict):
                    df = pd.DataFrame(obj, index=[0])
                else:
                    df = obj
                # 数据写入表(默认重复追加，索引不插入)
                df.to_sql(table_name, con, if_exists=if_exists, index=False)
                print(f'{self.success}({table_name})')
            except Exception as e:  # 报错则输出错误
                raise e

    def query(self, table_name: str):
        """
        从数据库中获取表的全部数据

        :param table_name: 表格名字
        :return: 查询的表格数据
        """
        try:
            # sql 查询语句
            sql = f'select * from {table_name}'
            # 查询sql，结果为dataFrame
            df = pd.read_sql_query(sql, self.connect)
            print(f'{self.success}({table_name})')
            return df
        except Exception as e:  # 报错则输出错误
            raise e


class Rtdb(Jet):
    """
    jet RTDB V10实时库数据操作，插入，查询，删除
    """
    _ip = "http://192.168.1.240:8055/api/v1/"
    _headers = {"Content-Type": "application/json"}
    _insert_url = _ip + "insertSampleData"  # 插入数据接口
    _sample_url = _ip + 'querySampleData'  # 查询历史数据接口
    _history_url = _ip + "queryHisData"  # 查询历史数据接口(固定时间间隔查询)
    _latest_url = _ip + "queryLastSampleData"  # 查询最新数据接口
    _delete_url = _ip + "deleteSampleData"  # 删除数据接口

    def __init__(self, point: Iterable, start_time=None, end_time=None, **kwargs):
        """

        :param point: RTDB实时库测点
        :param start_time: 开始时间 ,jetTimeStamp输入格式
        :param end_time: 结束时间 ,jetTimeStamp输入格式
        :param kwargs: jetTimeStamp关键字参数
        """
        self.check('len(point)>0', scope=locals())
        # 实时库测点转为list
        self.point = [point] if isinstance(point, str) else point
        # 开始和结束时间转为毫秒
        self.start_time = JetTimeStamp(start_time, **kwargs).ms
        self.end_time = JetTimeStamp(end_time, **kwargs).ms

    @staticmethod
    def _convert_insert_json(df: DataFrame, cls, split_n: int = 5000):
        """
        数据框转为插入api的json
        :param df: pandas dataframe
        :param cls: json转换的基类
        :param split_n: 列表分组长度，每次插入一组数据
        :return:
        """
        # 构造目标列表
        object_list = []
        # 数据框元素逐个加入
        for i in range(df.shape[0]):
            for j in range(df.shape[1] - 1):
                point = df.columns[j + 1]
                timestamp = df.iloc[i, 0]
                value = df.iloc[i, j + 1]
                if not np.isnan(value):  # value为nan则过滤(接口要求，空值不能插入！)
                    object_list.append({'point': point, 'timestamp': timestamp, 'value': value})
        # 分割长度小于等于列表长度
        split_n = split_n if split_n <= len(object_list) else len(object_list)
        # list 按split_n分组
        object_list_group = [object_list[i:i + split_n] for i in range(0, len(object_list), split_n)]
        # 每组转为json，添加进度条
        js = [json.dumps(i, cls=cls, ignore_nan=True) for i in tqdm(object_list_group, desc='Convert')]
        return js

    def _insert(self, url, js, headers):
        # 请求
        r = requests.post(url, js, headers=headers)
        if r.ok:
            raw_dict = json.loads(r.content)
            if raw_dict.get('opResult') == 'SUCCESS':
                print(self.success)
            else:
                if raw_dict.get('msg') is None:
                    print(f'{self.fail}(empty)')
                else:
                    print(self.fail, raw_dict.get('msg'))
        else:
            print(f'{self.fail} status code {r.status_code}')

    def insert(self, obj: Union[DataFrame, dict]):
        """
        向实时库插入测点数据

        :param obj: pandas dataframe类型:第一列为时间列，列名任意，数值为毫秒时间戳或者pandas Timestamp；
        第二列及以后列名为测点名，数值为测点数值。dict类型,key为point,timestamp,value
        :return:
        """

        if obj is None:
            print(f'{self.fail} (empty)')
        else:
            try:
                if isinstance(obj, dict):
                    body_json = json.dumps([obj], cls=JetEncoder)
                    self._insert(self._insert_url, body_json, self._headers)
                else:
                    body_json_group = self._convert_insert_json(obj, cls=JetEncoder)
                    for i in tqdm(body_json_group, desc='Insert'):
                        self._insert(self._insert_url, i, self._headers)
            except Exception as e:
                raise e

    @staticmethod
    def _sample_parse(response_list):
        # 数据框格式
        df_dict = {"timestamps": response_list[0].get('timestamps')}
        for i in range(response_list.__len__()):
            k = response_list[i].get('point')
            v = response_list[i].get('values')
            v = v if v else [None]
            df_dict[k] = v
        df = pd.DataFrame(df_dict)
        df.timestamps = df.timestamps.map(lambda x: JetTimeStamp(x).ts)
        df.set_index(keys='timestamps', inplace=True)
        return df

    def query_sample(self):
        """
        查询实时库历史真实数据
        """
        try:
            # 构造request的body
            body_json = json.dumps({'points': self.point,
                                    'startTime': self.start_time,
                                    'endTime': self.end_time}, cls=JetEncoder)
            r = requests.post(self._sample_url, body_json, headers=self._headers)
            if r.ok:
                raw_list = json.loads(r.content)
                df = self._sample_parse(raw_list)
                print(self.success, f'(points:{len(self.point)},point name:{list(self.point)[0]}...)')
                return df
            else:
                raise ValueError(f'{self.fail} status code {r.status_code}')
        except Exception as e:
            print(self.fail)
            raise e

    @staticmethod
    def _history_parse(response_dict: dict):
        """
        解析历史接口响应的数据为数据框
        :param response_dict: 响应的字典数据
        :return:
        """
        # 数据框格式
        df_dict = {k: v for k, v in response_dict.items() if k == 'timestamps'}
        for i in range(response_dict.get("values").__len__()):
            k = response_dict.get("values")[i].get('metricName')
            v = response_dict.get("values")[i].get('values')
            v = v if v else None
            df_dict[k] = v
        df = pd.DataFrame(df_dict)
        df.timestamps = df.timestamps.map(lambda x: JetTimeStamp(float(x)).ts)
        df.set_index(keys='timestamps', inplace=True)
        return df

    def query_history(self, **kwargs):
        """
        查询实时库历史数据 可以完成多测点相同（或不同）时段的数据查询

        :param kwargs: 查询数据的其他关键字参数,interval,查询间隔，unit,查询单位
        :return: 测点数据
        """
        try:
            # 构造request的body
            interval = kwargs.get('interval', 5)
            unit = kwargs.get('unit', 'minutes')
            body_json = json.dumps({'points': self.point,
                                    'startTime': self.start_time,
                                    'endTime': self.end_time,
                                    "interval": interval,
                                    "unit": unit}, cls=JetEncoder)
            r = requests.post(self._history_url, body_json, headers=self._headers)
            if r.ok:
                raw_dict = json.loads(r.content)
                print(self.success, f'(points:{len(self.point)},point name:{list(self.point)[0]}...)')
            else:
                raise ValueError(f'{self.fail} status code {r.status_code}')
            # 返回结果
            return self._history_parse(raw_dict)
        except Exception as e:
            print(self.fail)
            raise e

    @staticmethod
    def _latest_parse(response_list: list):
        """
        解析最新接口响应的数据为数据框
        :param response_list: 响应的列表数据
        :return:
        """
        # 数据框格式
        df_dict = {"timestamps": response_list[0].get('timestamp')}
        for i in range(response_list.__len__()):
            k = response_list[i].get('point')
            v = response_list[i].get('value')
            v = v if v else None
            df_dict[k] = v
        df = pd.DataFrame(df_dict, index=[0])
        df.timestamps = df.timestamps.map(lambda x: JetTimeStamp(x).ts)
        df.set_index(keys='timestamps', inplace=True)
        return df

    def query_latest(self):
        """
        查询实时库测点最新数据

        :return: 测点数据
        """
        try:
            # 构造request的body
            body_json = json.dumps({'points': self.point}, cls=JetEncoder)
            # 请求
            r = requests.post(self._latest_url, body_json, headers=self._headers)
            if r.ok:
                raw_list = json.loads(r.content)
                print(self.success, f'(points:{len(self.point)},point name:{list(self.point)[0]}...)')
            else:
                raise ValueError(f'{self.fail} status code {r.status_code}')
            # 返回结果
            return self._latest_parse(raw_list)
        except Exception as e:
            print(self.fail)
            raise e

    def delete(self):
        """
        删除实时库测点数据

        :return:
        """
        # 构造request的body
        body_json = json.dumps({'points': self.point,
                                'startTime': self.start_time,
                                'endTime': self.end_time}, cls=JetEncoder)
        # 请求
        r = requests.post(self._delete_url, body_json, headers=self._headers)
        raw_dict = json.loads(r.content)
        if raw_dict.get('opResult') == 'SUCCESS':
            print(self.success, f'(points:{len(self.point)},point name:{list(self.point)[0]}...)')
        else:
            raise ValueError(self.fail)


if __name__ == '__main__':
    Jet.filter_dict({'a': 1, 'b': 2}, 'k in ["a"]')
    # print(Rtdb('JTJT.JET.CT_4-5.P', start_time='-D:-D', end_time='-D:D').query_sample())
    # train1 = Rtdb('LGHB.NCGF.G1N1-I-A1-2.Pin').query_latest()
    # print(JetTimeStamp('2020-7-4').ts, JetTimeStamp('2020-7-4').ms)
    # print(JetTimeStamp('2020/01/16 12:10:23').ts)
    # print(JetTimeStamp(1424044800000).ts)
    # print(JetTimeStamp(1424044800).ts)
    # print(JetTimeStamp('-D:').ts)
    # print(JetTimeStamp('-D', base='2010').ts)
    # print(JetTimeStamp('-3D', ).ts)
    # print(JetTimeStamp('-D:5T', ).ts)
