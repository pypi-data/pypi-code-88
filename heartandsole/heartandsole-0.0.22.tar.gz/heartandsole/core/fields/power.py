"""Stub file to collect power algorithms from my other packages."""

import pandas as pd
from scipy.interpolate import interp1d

from heartandsole.fields.base import ActivityField
from heartandsole.power import util


class PowerField(ActivityField):
    
  FIELD_NAME = 'power'

  def ngp(self): 
    interp_fn = interp1d(self.records['time'], self.records['speed_ngp'], kind='linear')
    ngp_1sec = interp_fn([i for i in range(self.records['time'].max())])

    # Apply a 30-sec rolling average.   
    window = 30
    ngp_rolling = pd.Series(ngp_1sec).rolling(window).mean()
    
    # ngp_sma = putil.sma(
    #   df['NGP'], 
    #   window,
    #   time_series=df['time']
    # )

    return util.lactate_norm(ngp_rolling[29:])
