# -*- coding:utf-8 -*-
import os
import copy
import math
from pathlib import Path
from typing import List, NoReturn
from skydl.common.option import Option
from skydl.common.enhanced_float import EnhancedFloat
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP


class CommonUtils:

    @staticmethod
    def cycle(iterable=[None]):
        """
        e.g.
        from skydl.common.common_utils import CommonUtils
        ...
        iter = CommonUtils.cycle([0,2,3,1])
        next(iter)->0,next(iter)->2,...,next(iter)->0,next(iter)->2,...
        :param iterable: e.g. [0,2,3,1]
        :return:
        """
        from itertools import cycle
        return cycle(iterable)

    @staticmethod
    def camelcase_to_snakecase(class_name):
        """
        Convert camel-case string to snake-case.
        e.g. SuperDatasetBuilder.camelcase_to_snakecase(RecommendDatasetBuilder().__class__.__name__)
        -> "recommend_dataset_builder"
        or SuperDatasetBuilder.camelcase_to_snakecase("RecommendDatasetBuilder")
        -> "recommend_dataset_builder"
        """
        # @see tensorflow_datasets.core.naming#camelcase_to_snakecase
        import re
        _first_cap_re = re.compile("(.)([A-Z][a-z0-9]+)")
        _all_cap_re = re.compile("([a-z0-9])([A-Z])")
        s1 = _first_cap_re.sub(r"\1_\2", class_name)
        return _all_cap_re.sub(r"\1_\2", s1).lower()

    @staticmethod
    def deepcopy(x, memo=None, _nil=[]):
        """深拷贝，该方法执行比较耗时间，应谨慎使用"""
        return copy.deepcopy(x, memo, _nil)

    @staticmethod
    def format_number(x, times=1, format_args="0.2f", use_round_down=True):
        """
        格式化数字输出, e.g. 12.3456->"12.34"
        :param x: 数字 e.g. 12.3456
        :param times: 乘以的倍数，方便%输出
        :param format_args: e.g. "0.2f" 保留小数点后2位输出 e.g. 123.465->"123.47"
        :param use_round_down True直接截取, False四舍五入 e.g. False: 99.999989->'100.00', 99.11789->'99.12'
        :return: "12.34" 如果要to float类型就用: EnhancedFloat(format_number(12.3456, 100)), 注意EnhancedFloat("100.0000")->100.0
        """
        if x is None or math.isnan(x):
            return "0.00"
        try:
            # 最原始的四舍五入的方法：return format(EnhancedFloat(x)*times, format_args)
            # 用Decimal精确截取小数点后2位小数，也可以四舍五入。e.g. 123.465->"123.46"
            rounding = ROUND_DOWN if use_round_down else ROUND_HALF_UP
            return str(Decimal(EnhancedFloat(x) * times).quantize(Decimal(EnhancedFloat(0, format_args)), rounding=rounding))
        except:
            return str(x)

    @staticmethod
    def isnan(value):
        try:
            return math.isnan(EnhancedFloat(value))
        except:
            return False

    @staticmethod
    def get_user_home_path(default_value: str = "/tmp") -> str:
        """
        get user home
        :param default_value the default value
        :return str
        """
        return str(Option(Path.home()).get_or_else(default_value))

    @staticmethod
    def path_exists(path: str) -> bool:
        """
        文件或路径是否在本地环境存在
        :param path 文件名或路径 e.g. "/xxx/a.json" or "/xxx"
        :return bool true-存在 false-不存在
        """
        return os.path.exists(Option(path).get_or_else(""))

    @staticmethod
    def get_dirname(file_path: str) -> str:
        """
        获取带路径文件名的根目录
        获取文件名可以用：os.path.basename(file_path) e.g. "/Users/tony/tmp/yyy11/7778/99/22.txt" -> "22.txt"
        :param file_path 带路径的文件名
        e.g. "/Users/tony/tmp/yyy11/7778/99/22.txt" -> "/Users/tony/tmp/yyy11/7778/99"
        "/Users/tony/tmp/yyy11/7778/99" -> "/Users/tony/tmp/yyy11/7778"
        :return str
        """
        return os.path.dirname(file_path)

    @staticmethod
    def mkdirs(path: str) -> NoReturn:
        """
        递归创建文件夹目录
        :param path 需要递归创建的目录，可以是相对或者绝对路径 e.g. "/xxx/a.json" or "/xxx"
        """
        if not CommonUtils.path_exists(path):
            os.makedirs(path)  # 如果路径不存在，就创建这个路径

    @staticmethod
    def write_file(file: str, content: str) -> int:
        """
        写文件
        :param file 文件名 e.g. '/Users/michael/test.txt'
        :param content 文件内容 e.g. "abc"
        :return 写入的size
        """
        with open(file, 'w', newline='') as f:
            return f.write(content)

    @staticmethod
    def read_file(file: str) -> str:
        """
        读文件
        注意：写入文件里的\r\n会变为\n问题，参考：Python Write Replaces “\n” With “\r\n” in Windows https://stackoverflow.com/questions/47384652/python-write-replaces-n-with-r-n-in-windows
        :param file 文件名 e.g. '/Users/michael/test.txt'
        :return 读到的文件内容
        """
        with open(file, 'r', newline='') as f:
            return f.read()

    @staticmethod
    def calc_batch_size(num_total: int = 1, num_partitions: int = 1) -> int:
        """
        * 计算batch size，包括最后数量不足的那一批
        * e.g. calcBatchSize(20,8)=3,calcBatchSize(20,20)=1,calcBatchSize(20,15)=2,calcBatchSize(20,5)=4,
        * calcBatchSize(20,100)=1,calcBatchSize(20,-2)=-10
        * @param num_total 总数
        * @param num_partitions 分区数
        * @return batch_size
        """
        return int(math.ceil(EnhancedFloat(num_total) / EnhancedFloat(num_partitions)))  # e.g. math.ceil(6.3) -> 7

    @staticmethod
    def total_num_batch(num_total, batch_size, allow_smaller_final_batch=False) -> int:
        """
        计算总的批次数
        :param num_total 总数
        :param batch_size 每批的size
        :param allow_smaller_final_batch 是否允许最后不足批的数再加1批
        :return num_batch
        """
        num_batch = num_total // batch_size  # e.g. 12.1 // 2.0 -> 6.0
        if allow_smaller_final_batch:
            if num_total > (num_batch * batch_size):
                return num_batch + 1
            else:
                return num_batch
        else:
            # 舍去最后不能够成1批的剩余训练数据部分
            return num_batch

    @staticmethod
    def batch_index_split(num_total: int, batch_size: int, allow_smaller_final_batch: bool = False, begin_index: int = 0) -> List[List[int]]:
        """
        * 对index分批，可以作分页用
        * e.g. 有数据的index范围是lowerbound=12, upperbound=1001, numPartitions=5，则totalLen=upperbound-lowerbound+1,
        * 则分批函数为batch_index_split(1001-12+1, calc_batch_size(1001-12+1,5), 12),
        * 最后分批结果为：List[List[Long]] = List(List(12, 209, 0), List(210, 407, 1), List(408, 605, 2), List(606, 803, 3), List(804, 1001, 4))
        * :param num_total e.g. 10
        * :param batch_size e.g. 3
        * :param begin_index 对于index不是从0开始的数据集，这里指定第1页从第几个index的元素开始。 e.g. 1 即 [0, 100]->[1, 101]
        * :param allow_smaller_final_batch 是否允许最后不足批的数再加1批
        * :return batched_indexes List[List[begin_index, end_index, batched_num(即页次)]]
        usage:
        ```
        assert 3 == SparkWrapper.total_num_batch(13, SparkWrapper.calc_batch_size(13, 3), True)
        batched_indexes: List[List[int]] = SparkWrapper.batch_index_split(13, SparkWrapper.calc_batch_size(13, 3))
        for batch in batched_indexes:
            begin_index = batch[0]
            end_index = batch[1]
            page_index = batch[2]
            print(f"page_index：{page_index}, begin_index：{begin_index}，end_index={end_index}")
            for data_index in range(begin_index, end_index+1):
                print(f"data index: {data_index}")
        或
        batched_indexes = CommonUtils.batch_index_split(num_total=len(security_code_list),
                                                        batch_size=100,
                                                        allow_smaller_final_batch=True)
        start_batch_index = 10
        if start_batch_index > 0:
            logging.warn("注意：get_and_save_finance_daily#获取股本结构数据#start_batch_index已经被手工临时改为大于0的值，务必要记得下次改回初始化的0值！！！")
        for page, (begin, end, page) in enumerate(batched_indexes[start_batch_index:], start_batch_index):
            print(f"正在处理数据：batch index: {page} of {len(batched_indexes)-1}, 该批次里当前数据index范围: {begin}-{end}。。。")
        ```
        """
        # num_batch: int = int(math.ceil(EnhancedFloat(num_total) / EnhancedFloat(batch_size)))    # e.g. math.ceil(6.3) -> 7
        num_batch: int = CommonUtils.total_num_batch(num_total=num_total,
                                                     batch_size=batch_size,
                                                     allow_smaller_final_batch=allow_smaller_final_batch)
        batched_indexs: List[List[int]] = []
        for row in range(0, num_batch):
            end_index = (row + 1) * batch_size - 1 + begin_index
            batched_indexs.append(
                [row*batch_size + begin_index,
                 end_index if end_index < (num_total-1+begin_index) else num_total-1+begin_index,
                 row]
            )
        return batched_indexs


if __name__ == '__main__':
    # CommonUtils.write_file("/Users/tony/tmp/yyy/12.txt", "aaaabbbccc")
    # print(f"文件内容：{CommonUtils.read_file('/Users/tony/tmp/yyy/12.txt')}")
    print(CommonUtils.path_exists("/"))
    print(CommonUtils.isnan(EnhancedFloat("nan")))
    # 计算批次
    assert 3 == CommonUtils.total_num_batch(13, CommonUtils.calc_batch_size(13, 3), True)
    batched_indexes: List[List[int]] = CommonUtils.batch_index_split(13, CommonUtils.calc_batch_size(13, 3))
    for batch in batched_indexes:
        begin_index = batch[0]
        end_index = batch[1]
        page_no = batch[2]
        print(f"page_no：{page_no}, begin_index：{begin_index}，end_index={end_index}")
        for data_index in range(begin_index, end_index+1):
            print(f"data index: {data_index}")


