#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/27 11:38:13

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import json, copy, os
from .kfpath import path_join, path_parent, path_abs
#===============================================================================
# 
#===============================================================================
__all__ = ['get_subpath', 'get_data']

class Config(object):
    def __init__(self, json_file = None, **kws):
        if json_file:
            self.update_json(json_file)
        self.update_dict(kws)

    def update_json(self, json_file):
        with open(json_file, "r", encoding='utf-8') as reader:
            json_config = json.loads(reader.read())
        for key, value in json_config.items():
            self.__dict__[key] = value

    def update_dict(self, kws):
        self.__dict__.update(kws)

    @classmethod
    def from_dict(cls, json_object):
        config = Config()
        config.update_dict(json_object)
        return config

    @classmethod
    def from_json_file(cls, json_file):
        with open(json_file, "r", encoding='utf-8') as f:
            return cls.from_dict(json.load(f))

    def __repr__(self):
        return str(self.to_json_string())

    def __getitem__(self, item):
        return self.__dict__[item]

    def to_dict(self):
        return copy.deepcopy(self.__dict__)

    def to_json_string(self):
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def to_json_file(self, json_file_path):
        with open(json_file_path, "w", encoding='utf-8') as f:
            json.dump(f)

__cur_dir = path_parent(__file__)
_conf_file = path_join(__cur_dir, 'laok.conf')

# with open(_conf_file, 'r') as f:
#     conf = json.load(f)
conf = Config.from_json_file(_conf_file)

def get_subpath(name, fpath='', exist = True):
    fpath = path_abs(path_join(__cur_dir, conf[name], fpath))
    if exist :
        if os.path.exists(fpath):
            return fpath
    else:
        return fpath

def get_data(name, defVal = None):
    return conf[name] if name in conf else defVal

def path_model(fpath='', exist = True):
    return get_subpath('DATA_MODEL_PATH', fpath, exist)

def path_data2d(fpath='', exist = True):
    return get_subpath('DATA_2D_PATH', fpath, exist)

def path_data3d(fpath='', exist = True):
    return get_subpath('DATA_3D_PATH', fpath, exist)

def path_temp(fpath='', exist = True):
    return get_subpath('DATA_TEMP_PATH', fpath, exist)
