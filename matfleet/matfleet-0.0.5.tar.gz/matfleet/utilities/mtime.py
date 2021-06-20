#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:42:15'

import six
import datetime
from matfleet.utilities.constant import TIME_FORMAT, TIME_FORMAT_FS


def reconstitute_dates(obj_dict):
    if obj_dict is None:
        return None

    if isinstance(obj_dict, dict):
        return {k: reconstitute_dates(v) for k, v in obj_dict.items()}

    if isinstance(obj_dict, (list, tuple)):
        return [reconstitute_dates(v) for v in obj_dict]

    if isinstance(obj_dict, six.string_types):
        try:
            return datetime.datetime.strptime(obj_dict, TIME_FORMAT_FS)
        except:
            try:
                return datetime.datetime.strptime(obj_dict, TIME_FORMAT)
            except:
                pass
    return obj_dict


def now_time(as_str=True):
    dd = reconstitute_dates(datetime.datetime.utcnow())
    if as_str:
        return str(dd)
    return dd


if __name__ == '__main__':
    print(now_time())