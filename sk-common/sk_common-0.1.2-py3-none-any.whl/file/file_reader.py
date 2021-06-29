# -*- coding:utf-8 -*-
"""用于读取不同格式的数据，
包括txt, csv，excel, HDF5 , json
"""

import pandas as pd
import h5py
import json


def read_excel_to_df(io,
                     encoding='utf-8',
                     sheet_name=0,
                     header=0,
                     names=None,
                     index_col=None,
                     usecols=None,
                     dtype=None,
                     engine=None,
                     skiprows=None,
                     nrows=None,
                     na_values=None,
                     keep_default_na=True
                     ):
    """
    读取excel数据到pandas DataFrame，
    支持从本地文件系统或URL读取的xls，xlsx，xlsm，xlsb和odf文件扩展名。 支持读取单一sheet或几个sheet。

    :param io: str, bytes, ExcelFile, xlrd.Book, path object, or file-like object。
    :param encoding: str, 数据集的字符编码，默认'utf-8'。
    :param sheet_name: str, int, list, None, default 0，
                       默认为0，表示不输入sheet_name的参数下，默认引用第一张sheet的数据。
    :param header: int, list of int, default 0，表示用第几行作为表头，
                    默认header=0，即默认第一行为表头。None表示不使用数据源中的表头。
    :param names: array-like, default None，表示自定义表头的名称，需要传递数组参数。
    :param index_col: int, list of int, default None，
                      指定列为索引列，默认为None，也就是索引为0的列用作DataFrame的行标签。
    :param usecols: int, str, list-like, or callable default None，
                    需要解析的列，默认为None，解析所有列。
    :param dtype: type, default None，指定列的数据类型，默认为None，不改变数据类型。
    :param engine: str, default None，支持参数有“ xlrd”，“ openpyxl”或“ odf”，用于使用第三方的库去解析excel文件。
    :param skiprows: int,list, defalut None, 跳过指定的行
    :param nrows: int, default None，指定需要读取前多少行，通常用于较大的数据文件中。
    :param na_values: scalar, str, list-like, or dict, default None，指定某些列的某些值为NaN。
    :param keep_default_na: bool, default True，表示导入数据时是否导入空值。

    :return: pandas DataFrame
    """

    df = None
    try:
        df = pd.read_excel(io,
                           encoding=encoding,
                           sheet_name=sheet_name,
                           header=header,
                           names=names,
                           index_col=index_col,
                           usecols=usecols,
                           dtype=dtype,
                           engine=engine,
                           skiprows=skiprows,
                           nrows=nrows,
                           na_values=na_values,
                           keep_default_na=keep_default_na)
    except Exception as e:
        print(e)
    return df


def read_csv_txt_to_df(
        filepath_or_buffer,
        encoding=None,
        sep=',',
        delimiter=None,
        header='infer',
        index_col=None,
        chunksize=None,
        prefix=None,
        dtype=None,
        engine=None,
        compression='infer'):
    """"
    读取csv或txt等文件数据到pandas DataFrame

    :param filepath_or_buffer: str, 读取的文件路径,URL（包含http,ftp,s3）链接等。
    :param encoding: str, default None, 指定字符集编码类型，通常指定为'utf-8'。
    :param sep: str, 文件分割符。
    :param delimiter: str, default None，定界符，备选分隔符（如果指定该参数，则sep参数失效）。
    :param header: int or list of ints, default ‘infer’，
                   指定行数用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。
    :param index_col: int or sequence or False, default None,
                      用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。
    :param chunksize: int, default None，文件块的大小。
    :param prefix:  str, default None, 在没有列标题时，给列添加前缀。
    :param dtype: type, default None, 每列数据的数据类型。
    :param engine: {‘c’, ‘python’}, optional
                    使用的分析引擎, 可以选择C或者是python, C引擎快但是Python引擎功能更加完备。
    :param compression: {‘infer’,‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}, default ‘infer’
                        直接使用磁盘上的压缩文件。如果使用infer参数，则使用 gzip, bz2, zip或者解压文件名中以
                      ‘.gz’, ‘.bz2’, ‘.zip’, or ‘xz’这些为后缀的文件，否则不解压
    :return: pandas DataFrame
    """

    df = None
    try:
        df = pd.read_csv(filepath_or_buffer,
                         encoding=encoding,
                         sep=sep,
                         delimiter=delimiter,
                         header=header,
                         index_col=index_col,
                         chunksize=chunksize,
                         prefix=prefix,
                         dtype=dtype,
                         engine=engine,
                         compression=compression)
    except Exception as e:
        print(e)
    return df


def read_txt_to_list(file_path, encoding='utf-8', line_strip='\n', sep=','):
    """
    读取txt文件数据到list

    :param file_path: str,文件路径
    :param encoding: str, default 'utf-8', 指定字符集编码类型，通常指定为'utf-8'。
    :param line_strip:  str, default '\n' , 行分割符，默认’\n'
    :param sep: str default ',', 每行中字段分隔符, 默认','
    :return: 多维数组，每一维为每行数据，维度为文件的数据行数
    """
    data = []
    try:
        with open(file_path, "r", encoding=encoding) as f:
            for line in f.readlines():
                line = line.strip(line_strip)
                text = line.split(sep)
                data.append(text)
    except Exception as e:
        print(file_path, e)
    return data


def read_h5_to_dict(file_path, name_list=None):
    """
    读取HDF5文件数据到字典

    :param file_path: str, HDF5文件路径。
    :param name_list: list, default None, 所需key的数组，默认为None，则包含所有key。
    :return: 存储hdf5数据字典。
    """
    data_dict = {}
    try:
        f = h5py.File(file_path, 'r')
        if name_list is None or len(name_list) == 0:
            name_list = f.keys()
        for name in name_list:
            data_dict[name] = f[name]
        return data_dict

    except Exception as e:
        print(e)
    return data_dict


def read_json_to_dict(file_path, encoding='utf-8'):
    """
    读取json文件数据到字典

    :param file_path: str, json文件路径。
    :param encoding: str, default 'utf-8', 指定字符集编码类型，默认为'utf-8'。
    :return: json数据存储字典
    """
    data_dict = {}
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            data_dict = json.load(f)
            return data_dict
    except Exception as e:
        print(e)
    return data_dict
