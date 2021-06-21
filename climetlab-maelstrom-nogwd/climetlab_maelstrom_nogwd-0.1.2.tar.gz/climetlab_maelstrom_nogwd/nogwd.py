#!/usr/bin/env python3# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset
from climetlab.normalize import normalize_args,DateListNormaliser
import pandas as pd
import xarray as xr

__version__ = "0.1.0"

URL = "https://storage.ecmwf.europeanweather.cloud"

PATTERN = "{url}/NOGWD_L91_PUBLIC/nc/{date}.nc"

class nogwd(Dataset):
    name = "NOGWD 91 level dataset"
    home_page = "https://github.com/mchantry/maelstrom-nogwd"
    licence = "-"
    documentation = "-"
    citation = "-"

    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/ecmwf-lab/climetlab_maelstrom_nogwd/LICENSE"
        "If you do not agree with such terms, do not download the data. "
    )
    dataset = None
    dataset_dates = {'minimal':'2015-01-01',
                     'training':pd.date_range(start='2015-01-01',
                                              end='2015-12-01',
                                              freq='30D'),
                     'validation':['2016-02-25','2016-06-24','2016-12-21'],
                     'testing':['2017-02-19','2017-07-19','2017-11-16']
                     }
    all_datelist = ['2015-01-01', '2015-01-31', '2015-03-02', '2015-04-01',
                    '2015-05-01', '2015-05-31', '2015-06-30', '2015-07-30',
                    '2015-08-29', '2015-09-28', '2015-10-28', '2015-11-27',
                    '2016-02-25','2016-06-24','2016-12-21',
                    '2017-02-19','2017-07-19','2017-11-16']
    default_datelist = '2015-01-01'

    def __init__(self, date=None,dataset=None):
        if dataset is None:
            self.date = self.parse_date(date)
        else:
            if dataset not in self.dataset_dates.keys():
                raise ValueError(f"{dataset} is not in {dataset_dates.keys()}")
            self.date = self.parse_date(self.dataset_dates[dataset])
        self._load()

    def _load(self):
        request = dict(url=URL, date=self.date)
        self.source = cml.load_source("url-pattern", PATTERN, request,merger=Merger())

    def parse_date(self, date):
        if date is None:
            date = self.default_datelist
        date = DateListNormaliser("%Y-%m-%d")(date)
        for d in date:
            if d not in self.all_datelist:
                raise ValueError(f"{d} is not in the available list of dates {self.all_datelist}")
        return date


class Merger:
    def __init__(self, engine='netcdf4', concat_dim="examples", options=None):
        self.engine = engine
        self.concat_dim = concat_dim
        self.options = options if options is not None else {}

    def merge(self, paths, **kwargs):
        return xr.open_mfdataset(
            paths,
            engine=self.engine,
            concat_dim=self.concat_dim,
            combine="nested",
            **self.options,
        )
