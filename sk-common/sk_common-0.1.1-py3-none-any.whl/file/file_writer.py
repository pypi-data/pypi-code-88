# -*- coding:utf-8 -*-
"""用于将数据写入不同格式文件
包括txt, csv，excel, HDF5 , json
"""

import pandas as pd
import h5py
import json


def write_df_to_excel(df,
                      file_path,
                      sheet_name="Sheet1",
                      na_rep="",
                      columns=None,
                      header=True,
                      index=False,
                      index_label=None,
                      engine=None,
                      encoding='utf-8'
                      ):
    """
    存入dataframe数据到excel文件

    :param df: pandas dataframe，需要写入excel的dataframe数据。
    :param file_path: str, excel文件目标路径。
    :param sheet_name: str, default "Sheet1"，excel表名命名。
    :param na_rep: int, str, default "", 缺失值填充,默认值为空字符串。
    :param columns: list，选择需要输出的的列名数组。
    :param header: bool, list， default True 写出列名。如果给定字符串列表，则假定它是列名称的别名。
    :param index: bool， default False, 是否显示索引，默认False，不显示index。
    :param index_label: str, default None,设置索引列的列名。
    :param engine: str, default None, 所使用的写引擎。
    :param encoding:  str ，数据集的字符编码，默认'utf-8'。
    :return: bool 是否写入成功，成功为True，失败为False
    """
    try:
        df.to_excel(file_path,
                    sheet_name=sheet_name,
                    na_rep=na_rep,
                    columns=columns,
                    header=header,
                    index=index,
                    index_label=index_label,
                    engine=engine,
                    encoding=encoding)
    except Exception as e:
        print(e)
        return False
    return True


def write_df_to_multi_sheet(file_path,
                            df_list,
                            sheet_name_list,
                            na_rep="",
                            columns=None,
                            header=True,
                            index=False,
                            index_label=None,
                            engine=None,
                            encoding='utf-8'
                            ):
    """
    将dataframe数组写入excel多张sheet中

    :param file_path: str, excel文件目标路径。
    :param df_list: list，存储多个dataframe。
    :param sheet_name_list: list，包含每张表的表名。
    :param na_rep: int, str, default "", 缺失值填充,默认值为空字符串。
    :param columns:  list，选择需要输出的的列名数组。
    :param header: bool, list， default True 写出列名。如果给定字符串列表，则假定它是列名称的别名。
    :param index:  bool， default False, 是否显示索引，默认False，不显示index。
    :param index_label:  str, default None,设置索引列的列名。
    :param engine:  str, default None, 所使用的写引擎
    :param encoding:  str ，数据集的字符编码，默认'utf-8'。
    :return: bool 是否写入成功，成功为True，失败为False
    """
    try:
        with pd.ExcelWriter(file_path) as each_sheet:
            for df, sheet in zip(df_list, sheet_name_list):
                df.to_excel(each_sheet,
                            sheet_name=sheet,
                            index=index,
                            na_rep=na_rep,
                            columns=columns,
                            header=header,
                            index_label=index_label,
                            engine=engine,
                            encoding=encoding
                            )
    except Exception as e:
        print(e)
        return False
    return True


def write_df_to_csv_txt(
        df,
        file_path,
        index=False,
        encoding='utf-8',
        mode='w',
        header=True,
        sep=",",
        columns=None,
        index_label=None,
        compression="infer",
        line_terminator=None,
        chunksize=None,
        date_format=None
):
    """
    存入dataframe数据到csv或txt文件

    :param df: pandas dataframe，需要写入的dataframe数据。
    :param file_path:  str, 文件目标路径。
    :param index: bool， default False, 是否显示索引，默认False，不显示index。
    :param encoding: str ，数据集的字符编码，默认'utf-8'。
    :param mode:  str, 写入模式，默认为 'w'。
    :param header: bool, list， default True 写出列名。如果给定字符串列表，则假定它是列名称的别名。
    :param sep: str, default "," , 输出文件的字段分隔符,默认","。
    :param columns: list，选择需要输出的的列名数组。默认None。
    :param index_label: str, default None,设置索引列的列名。
    :param compression: str，表示压缩模式，默认'infer'。
    :param line_terminator:  str，输出文件中使用的换行符或字符序列。
    :param chunksize: int，写入的批次个数，默认 None，一次性写入。
    :param date_format: str，日期时间对象的格式字符串，默认None。
    :return: bool 是否写入成功，成功为True，失败为False。
    """
    try:
        df.to_csv(
            file_path,
            index=index,
            encoding=encoding,
            mode=mode,
            header=header,
            sep=sep,
            columns=columns,
            index_label=index_label,
            compression=compression,
            line_terminator=line_terminator,
            chunksize=chunksize,
            date_format=date_format
        )
    except Exception as e:
        print(e)
        return False
    return True


def write_list_to_txt(
        data_list,
        file_path,
        encoding='utf-8',
        line_strip='\n',
        sep=','):
    """
    将数组写入txt文件中

    :param data_list: list，需要写入txt的数据，格式为[[a,b,c],[d,e,f],.....],每一维写入同一行。
    :param file_path: str, txt文件目标路径。
    :param encoding: str ，数据集的字符编码，默认'utf-8'。
    :param line_strip: str, default '\n' , 行分割符，默认’\n'。
    :param sep: str default ',', 每行中字段分隔符, 默认','。
    :return: bool 是否写入成功，成功为True，失败为False。
    """
    try:
        with open(file_path, 'w', encoding=encoding) as fw:
            for line in data_list:
                for i in range(len(line)):
                    fw.write(str(line[i]))
                    if i != len(line) - 1:
                        fw.write(sep)
                fw.write(line_strip)
    except Exception as e:
        print(e)
        return False
    return True


def write_list_to_h5(data_list, name_list, file_path):
    """
    将data数据和key数组一一对应写入目标h5文件

    :param data_list: list，需要写入h5文件的数据数组
    :param name_list: list，需要写入h5文件的key数组
    :param file_path: str，h5文件目标路径
    :return:  bool 是否写入成功，成功为True，失败为False。
    """
    try:
        f = h5py.File(file_path, 'w')
        for d, name in zip(data_list, name_list):
            f.create_dataset(name, data=d)
        f.close()
    except Exception as e:
        f.close()
        return False
    finally:
        f.close()
    return True


def write_dict_to_json(dict, file_path, encoding='utf-8'):
    """
    写入字典数据到json文件

    :param dict: 字典，需写入json文件的数据。
    :param file_path:  str，json文件目标路径。
    :param encoding:  str ，数据集的字符编码，默认'utf-8'。
    :return: bool 是否写入成功，成功为True，失败为False。
    """
    try:
        with open(file_path, "w", encoding=encoding) as dump_f:
            json.dump(dict, dump_f, ensure_ascii=False)
    except Exception as e:
        print(e)
        return False
    return True
