#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:48:00'

from configparser import ConfigParser, NoOptionError, NoSectionError


def get_cofig(section, option, fpath):
    cp = ConfigParser()
    cp.read(fpath)
    try:
        value = cp.get(section, option)
    except NoOptionError as e:
        print(e.message)
        return None
    except NoSectionError as e:
        print(e.message)
        return None
    return value


def set_config(section, option, value, fpath, head_infi=''):
    if value is None:
        value = ''

    if not type(value) is str:
        value = str(value)

    cp = ConfigParser()
    cp.read(fpath)
    if section not in cp.sections():
        cp.add_section(section)
    cp.set(section, option, value)

    with open(fpath, 'w+') as f:
        if head_infi:
            f.write(head_infi)
        cp.write(f)



