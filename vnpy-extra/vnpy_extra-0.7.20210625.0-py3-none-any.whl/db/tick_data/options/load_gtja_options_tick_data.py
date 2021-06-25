"""
@author  : MG
@Time    : 2021/6/23 13:35
@File    : load_gtja_options_tick_data.py
@contact : mmmaaaggg@163.com
@desc    : 用于将国泰君安提供的期权tick数据合成分钟线数据导入到数据库中
"""
import logging
import zipfile
import pandas as pd

from ibats_utils.path import get_file_name_iter

logger = logging.getLogger(__name__)


def load_tick_data_from_zip(file_path, chunk_size=1000):
    zf = zipfile.ZipFile(file_path, 'r')
    for z_info in zf.filelist:
        if z_info.is_dir():
            continue
        data = zf.read(z_info.filename)
        with zf.open(z_info.filename, "r") as fp:
            df = pd.read_csv(fp, chunksize=chunk_size, encoding="GBK", header=None, usecols=[])
            for chunk in df:
                break



def load_tick_data_from_dir(dir_path):
    count = 0
    for _ in get_file_name_iter(dir_path, '*.zip', recursive=True):
        count += load_tick_data_from_zip(_)


def _test_load_tick_data_from_zip():
    file_path = r'f:\downloads\截止2020年历史期权tick数据\商品期权CO\GTA_COL1_TAQ_201703.zip'
    load_tick_data_from_zip(file_path)


if __name__ == "__main__":
    # load_tick_data_from_dir(r"f:\downloads\截止2020年历史期权tick数据\商品期权CO")
    _test_load_tick_data_from_zip()
