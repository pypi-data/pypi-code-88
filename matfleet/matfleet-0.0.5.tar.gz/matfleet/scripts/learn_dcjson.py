#   coding:utf-8
#   This file is part of DancingCell.
#
#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2019/05/24 17:33:46'

import json
import bson
import datetime
import numpy as np
from importlib import import_module
from inspect import getfullargspec


class ALKSON(object):
    """
    完全兼容Mony JSON， MSONable
    通过下面的方法初始构建一个可以写为字典的类
    class MSONClass(MSONable):
        def __init__(self, a, b, c, d=1, **kwargs):
            self.a = a
            self.b = b

    对于字典中包含一个class的to_dict方法必须包含 -FromModule 和 -FromClass 两个键值

        d["-FromModule"] = self.__class__.__module__
        d["-FromClass"] = self.__class__.__name__

    可以将继承自该类的所有 init传进来的属性输出成字典格式
    并且支持json 的解码和编码， 除了json支持的python基本类型，还支持以下类型
        datatime
        numpy
        bson

    """

    def to_dict(self):
        """
        A JSON serializable dict representation of an object.
        """
        d = {"-FromModule": self.__class__.__module__,
             "-FromClass": self.__class__.__name__}

        try:
            _parentmod = self.__class__.__module__.split('.')[0]
            _modver = import_module(_parentmod).__version__
            d["-ModVersion"] = u"{}".format(_modver)
        except AttributeError:
            d["-ModVersion"] = None

        # get all init rm_self_args except self
        rm_self_args = [i for i in getfullargspec(self.__class__.__init__).args if i != 'self']

        def cir_to_dict(obj):
            if isinstance(obj, list):
                return [cir_to_dict(__t) for __t in obj]
            elif isinstance(object, tuple):
                return (cir_to_dict(__i) for __i in obj)
            elif isinstance(obj, dict):
                return {__k: cir_to_dict(__v) for __k, __v in obj.items()}
            elif hasattr(obj, "to_dict"):
                return obj.to_dict()
            return obj

        for c in rm_self_args:
            try:
                a = self.__getattribute__(c)
            except AttributeError:
                try:
                    a = self.__getattribute__("_" + c)
                except AttributeError:
                    raise NotImplementedError(
                        "Unable to automatically determine to_dict ")
            # 将所有不是字典的数值解析成字典
            d[c] = cir_to_dict(a)

        if hasattr(self, "kwargs"):
            d.update(**self.kwargs)
        if hasattr(self, "_kwargs"):
            d.update(**self._kwargs)

        return d

    @classmethod
    def read_dict(cls, d):
        decoded = {k: ALKDecoder().alk_parse(v) for k, v in d.items()
                   if not k.startswith("-")}
        return cls(**decoded)

    def to_json(self):
        """
        Returns a json string representation of the MSONable object.
        """
        return json.dumps(self, cls=ALKEncoder)


class ALKEncoder(json.JSONEncoder):
    """Json can output data for numpy objects."""

    def default(self, o):
        """function to check validity of data

        Args:
            o: objects

        Return:
            have valid formatted object.
        """
        if isinstance(o, datetime.datetime):
            return {"-FromModule": "datetime", "-FromClass": "datetime",
                    "string": o.__str__()}

        if isinstance(o, np.ndarray):
            return {"-FromModule": "numpy",
                    "-FromClass": "array",
                    "-NPDtype": o.dtype.__str__(),
                    "-Data": o.tolist()}
        elif isinstance(o, np.generic):
            return o.item()

        if isinstance(o, bson.objectid.ObjectId):
            return {"-FromModule": "bson.objectid",
                    "-FromClass": "ObjectId",
                    "oid": str(o)}

        try:
            d = o.to_dict()
            if "-FromModule" not in d:
                d["-FromModule"] = u"{}".format(o.__class__.__module__)
            if "-FromClass" not in d:
                d["-FromClass"] = u"{}".format(o.__class__.__name__)
            if "-ModVersion" not in d:
                try:
                    _parentmod = o.__class__.__module__.split('.')[0]
                    _modver = import_module(_parentmod).__version__
                    d["-ModVersion"] = u"{}".format(_modver)
                except AttributeError:
                    d["-ModVersion"] = None
            return d
        except AttributeError:
            return json.JSONEncoder.default(self, o)


class ALKDecoder(json.JSONDecoder):
    """
    A Json Decoder which supports the MSONable API. By default, the
    decoder attempts to find a module and name associated with a dict. If
    found, the decoder will generate a Pymatgen as a priority.  If that fails,
    the original decoded dictionary from the string is returned. Note that
    nested lists and dicts containing pymatgen object will be decoded correctly
    as well.

    Usage:

        # Add it as a %cls% keyword when using json.load
        json.loads(json_string, cls=MontyDecoder)
    """

    def alk_parse(self, d):
        """
        Recursive method to support decoding dicts and lists containing
        pymatgen objects.
        """
        if isinstance(d, dict):
            if "-FromModule" in d and "-FromClass" in d:
                _nmod = d["-FromModule"]
                _ncal = d["-FromClass"]
            else:
                _nmod = None
                _ncal = None

            if _nmod and _nmod not in ["bson.objectid", "numpy"]:
                if _nmod == "datetime" and _ncal == "datetime":
                    dt = datetime.datetime.strptime(d["string"], "%Y-%m-%d %H:%M:%S")
                    return dt

                mod = __import__(_nmod, globals(), locals(), [_ncal], 0)
                if hasattr(mod, _ncal):
                    cls_ = getattr(mod, _ncal)
                    data = {k: v for k, v in d.items() if not k.startswith("-")}
                    if hasattr(cls_, "read_dict"):
                        return cls_.read_dict(data)

            elif _nmod == "numpy" and _ncal == "array":
                return np.array(d["-Data"], dtype=d["-NPDtype"])

            elif _nmod == "bson.objectid" and _ncal == "ObjectId":
                return bson.objectid.ObjectId(d["oid"])

            return {self.alk_parse(k): self.alk_parse(v)
                    for k, v in d.items()}

        elif isinstance(d, list):
            return [self.alk_parse(x) for x in d]

        return d

    def decode(self, s):
        d = json.JSONDecoder.decode(self, s)
        return self.alk_parse(d)


# test
class TTT(ALKSON):
    def __init__(self, a, b, c, d, **kwargs):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.kwargs = kwargs

class FFF(ALKSON):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


if __name__ == '__main__':
    # _ = __import__('dancingcell.Atom', globals(), locals(), ['Site'], 0)
    # print(_)
    # a = getattr(_, 'Site')
    # print(hasattr(getattr(_, 'Site'), 'read_dict'))
    # print(getfullargspec(getattr(_, 'Site')))
    #
    # _parentmod = a.__module__
    # print(_parentmod)
    # _modver = import_module(_parentmod).__version__
    # print(_modver)
    # c = {'a': 1, 'b': 2, 1: {'d': '23423', 'dd':'dfsdf'}, 2: ['232', '3423']}
    fff = FFF(111, 222, 333, np.array([111, 222, 333], dtype=np.int))
    aa = TTT(1, {3:fff}, ['sdfsd', 'sdfsdg', 123], np.array([1, 2, 3], dtype=np.int), dsf=23423, ghfjkdghjkd=898589678934)
    cc = aa.to_dict()
    dd = TTT.read_dict(cc)
    print(dd.__dict__)
