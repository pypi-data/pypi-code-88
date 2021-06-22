#!/usr/bin/env python
# coding: utf-8

from typing import Any


def write_once(fp: str, data: Any):
        """
        写入一个数据到一个文件，然后关闭文件
        :param fp:
        :param data: 任意类型的数据
        :param data_type: 数据的类型，与Python3的类型注解一致
            支持的类型有:
            1. str 写入一个字符串
            2. List[str] 写入一个字符串数组
        :return:
        """

        text = None
        if isinstance(data, str):
            text = data
        elif isinstance(data, list):
            if any([isinstance(i, str) for i in data]):
                text = '\n'.join(data)
            elif any([isinstance(i, int) for i in data]):
                text = '\n'.join([int(i) for i in data])
        
        if text is None:
            raise ValueError('Not supported type')

        with open(fp, 'w') as writer:
            writer.write(text)


def read_chunk(fp: str, chunk_size=512):
    with open(fp, 'r') as reader:
        while True:
            chunk = reader.read(chunk_size)
            if chunk:
                yield chunk
            else:
                break