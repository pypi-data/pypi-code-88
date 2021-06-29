# -*- coding:utf-8 -*-
"""
用于存取不同格式的数据，txt,csv，excel,...
"""
import pandas as pd
import h5py
import json
import pickle

def load_data_from_xls(file_path, sheet_name=0, engine=None):
    """
    读取xls文件

    :param file_path: 文件路径
    :param sheet_name: sheet name
    :param engine: 解析xls的引擎，默认为none,可选为openxl
    :return: df 数据
    """

    df = None
    try:
        df = pd.read_excel(file_path, sheet_name, engine=engine)
    except Exception as e:
        print(e)
    return df


def load_data_from_csv(file_path, encoding='utf-8'):
    """
    csv 格式文件读取

    :param file_path: 文件路径
    :param encoding: 文件编码
    :return: df 数据框
    """
    df = None
    try:
        df = pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        print(e)
    return df


def load_data_from_txt(file_path, encoding='utf-8'):
    """
    读取txt格式文件

    :param file_path: 文件路径
    :param encoding:  文件编码
    :return: data 一行为一个元素的列表
    """
    data = []
    try:
        with open(file_path, "r", encoding=encoding) as f:
            for line in f.readlines():
                line = line.strip('\n')
                data.append(line)
    except Exception as e:
        print(file_path, e)
    return data


def load_data_from_h5(file_path, name_list):
    """
    读取h5文件

    :param file_path: 文件路径
    :param name_list:  h5中的矩阵名列表
    :return: 字典：矩阵名到矩阵的映射
    """
    data_dic = {}
    try:
        f = get_data_h5_handle(file_path)
        for name in name_list:
            data_dic[name] = f[name]
    except Exception as e:
        print(e)
    return data_dic


def get_data_h5_handle(file_path):
    """
    获取h5文件句柄

    :param file_path: h5文件路径
    :return: 文件句柄
    """
    try:
        f = h5py.File(file_path, 'r')
        return f
    except Exception as e:
        raise e

def load_data_from_json(file_path, encoding='utf-8'):
    """
    加载json数据格式

    :param file_path: json格式文件路径
    :param encoding: 文件编码
    :return: json格式的数据
    """

    try:
        with open(file_path, 'r', encoding=encoding) as load_f:
            load_dict = json.load(load_f)
            return load_dict
    except Exception as e:
        print(e)


def load_model(file_path, mode='r'):
    """
    加载sklearn 训练的模型

    :param file_path: 模型路径
    :param mode: 读写模式
    :return: 模型
    """

    try:
        with open(file_path, mode) as fr:
            model = pickle.load(fr)
            return model
    except Exception as e:
        raise e

def save_data_to_xls(df, file_path, index=False):
    """
    保存df数据到xls

    :param df: 数据框
    :param file_path: 保存文件路径
    :param index: 是否保存index
    :return: True/False 成功或者失败
    """

    try:
        df.to_excel(file_path, index=index)
    except Exception as e:
        print(e)
        return False
    return True


def save_data_to_xls_mul_sheet(file_path, df_list, sheet_list):
    """
    保存多个df数据到xls

    :param file_path: 文件路径
    :param df_list: df 列表
    :param sheet_list: sheet 列表
    :return: True/False 成功或者失败
    """

    try:
        with pd.ExcelWriter(file_path) as xlsx:
            for df, sheet in zip(df_list, sheet_list):
                df.to_excel(xlsx, sheet_name=sheet, index=False)
    except Exception as e:
        print(e)
        return False
    return True


def save_data_to_csv(df, file_path, index=False, encoding='utf-8', mode='w', header=True):
    """
    保存数据到csv

    :param df: df数据
    :param file_path: 保存路径
    :param index: 是否保存索引
    :param encoding: 文件编码
    :param mode: 读写模式
    :param header: 是否保存表头
    :return: True/False 成功或者失败
    """
    try:
        df.to_csv(file_path, index=index, encoding=encoding, mode=mode, header=header)
    except Exception as e:
        print(e)
        return False
    return True


def save_data_to_txt(data_list, file_path, encoding='utf-8'):
    """
    保存文件到txt

    :param data_list: 数据
    :param file_path: 文件路径
    :param encoding: 数据编码
    :return: True/False 成功或者失败
    """

    try:
        with open(file_path, 'w', encoding=encoding) as fw:
            for ele in data_list:
                fw.write(ele)
                fw.write('\n')
    except Exception as e:
        print(e)
        return False
    return True


def save_data_to_h5(data_list, name_list, file_path):
    """
    保存文件到h5

    :param data_list: 矩阵列表
    :param name_list:  矩阵对应的名字列表
    :param file_path:  保存的文件路径
    :return: True/False 成功或者失败
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

def save_data_to_json(file_path, data):
    """
    保存数据到json格式

    :param file_path: 文件路径
    :param data: 数据
    :return: True/False 成功或者失败
    """
    try:
        with open(file_path, "w") as dump_f:
            json.dump(data, dump_f, ensure_ascii=False)
    except Exception as e:
        print(e)
        return False
    return True

def save_model(model, file_path, mode='w'):
    """
    保存机器学习的模型文件

    :param model: 需要保存的模型
    :param file_path: 模型保存路径
    :param mode: 读写模式
    :return: True/False 成功或者失败

    Example
    -------
    >>> flag = save_model(model, file_path)
    >>> print(flag)
    True
    """
    try:
        with open(file_path, mode) as fw:
            pickle.dump(model, fw)
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == '__main__':
    """
    测试模块是否正常运行
    """
    from sk_nlp.util import file_conf

    get_data_h5_handle(file_path=file_conf.tf_idf_file_path)