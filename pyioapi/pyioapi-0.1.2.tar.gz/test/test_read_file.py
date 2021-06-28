# !/usr/bin/env python
# coding: utf-8
# version: 1.0
# author: Fennel
# contact: gongkangjia@gmail.com
# date: 2021/5/28
import os
import netCDF4 as nc

print(os.getcwd())
data = nc.Dataset("./test/METCRO3D_2019-05-01")
print(data.data_model)


class DataArray:
    def __init__(self, filename=None, **kwargs):
        self.attrs =
        self.data = None
        self.kwargs = kwargs


class Dataset:
    def __init__(self, dims=None, data_vars=None, attrs=None):
        self.dims = dims if dims else {}
        self.data_vars = data_vars if data_vars else {}
        self.attrs = attrs if attrs else {}


def open_dataset(filename=None, **kwargs):
    ncobj = nc.Dataset(filename, **kwargs)
    ds = Dataset(
            dims = {v.name:v.size for v in data.dimensions.values()},
            data_vars

    )
