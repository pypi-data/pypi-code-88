# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:16:19 2017

@author: Piotr Zioło
"""

import numpy as np


def jsonify_dict(d):
    if type(d) == dict:
        json_d = {}
        for key, value in d.items():
            if type(key) == tuple:
                s_key = "("
                for idx in range(len(key)):
                    s_key += str(key[idx])
                    if idx < len(key) - 1:
                        s_key += ", "
                s_key += ")"
                json_d[s_key] = jsonify_dict(value)
            elif type(key) in [int, np.int32, np.int64, float, np.float32, np.float64]:
                json_d[str(key)] = jsonify_dict(value)
            else:
                json_d[key] = jsonify_dict(value)
        return json_d
    elif type(d) == np.ndarray:
        lst = d.tolist()
        for idx in range(len(lst)):
            if type(lst[idx]) in [np.int32, np.int64, np.float32, np.float64]:
                lst[idx] = jsonify_dict(lst[idx])
        return lst
    elif type(d) == list:
        lst = d
        for idx in range(len(lst)):
            if type(lst[idx]) in [np.int32, np.int64, np.float32, np.float64]:
                lst[idx] = jsonify_dict(lst[idx])
            elif type(lst[idx]) == tuple:
                tup = list(lst[idx])
                for t_idx in range(len(tup)):
                    tup[t_idx] = jsonify_dict(tup[t_idx])
                lst[idx] = tuple(tup)
        return lst
    elif type(d) in [np.int32, np.int64]:
        return int(d)
    elif type(d) in [np.float32, np.float64]:
        return float(d)
    else:
        return d


def reduce_array_sizes(d, size_limit=180):
    if type(d) == dict:
        json_d = {}
        for key, value in d.items():
            json_d[key] = reduce_array_sizes(value)
        return json_d
    if type(d) == list:
        if len(d) > size_limit:
            indices = [int(i) for i in np.linspace(0, len(d)-1, size_limit)]
            return [reduce_array_sizes(d[idx]) for idx in indices]
        else:
            return [reduce_array_sizes(el) for el in d]
    else:
        return d
