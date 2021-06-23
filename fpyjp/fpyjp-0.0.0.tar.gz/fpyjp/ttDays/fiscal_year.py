#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fiscal year

@author: WeLLiving@well-living

"""
import pandas as pd

class FiscalYear:
    def __init__(self, ts, closing_month):
        if type(closing_month) != int:
            print('closing_month must be int')
            pass
        if (self.closing_month < 1) or (self.closing_month > 12):
            print('closing_month must be greater than or equal to 1 and less than or equal to 12')
            pass
        self.ts = ts  # pandas._libs.tslibs.timestamps.Timestamp or pandas.core.series.Series(dtype: datetime64[ns])
        self.closing_month = closing_month
    
    def year(self):
        if self.closing_month == 12:
            return self.ts.dt.year
        else:
            return (self.ts - pd.offsets.MonthOffset(self.closing_month)).dt.year
    
    def quarter(self):
        if self.closing_month == 12:
            return self.ts.dt.quarter
        else:
            return (self.ts - pd.offsets.MonthOffset(self.closing_month)).dt.quarter



