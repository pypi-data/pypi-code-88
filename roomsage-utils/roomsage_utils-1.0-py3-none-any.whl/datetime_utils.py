# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:16:33 2017

@author: Piotr Zioło
"""

from datetime import datetime
from datetime import timedelta
import pytz
from dateutil.relativedelta import relativedelta


def is_dst_now(tz):
    now = pytz.utc.localize(datetime.utcnow())
    return now.astimezone(tz).dst() != timedelta(0)
    
    
def is_dst_aware_dt(aware_dt):
    assert aware_dt.tzinfo is not None
    assert aware_dt.tzinfo.utcoffset(aware_dt) is not None
    return bool(aware_dt.dst())
    
    
def is_dst_unaware_dt(unaware_dt, tz):
    aware_tz = tz.localize(unaware_dt)
    return aware_tz.dst() != timedelta(0)
    

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    return from_date - relativedelta(years=years)
