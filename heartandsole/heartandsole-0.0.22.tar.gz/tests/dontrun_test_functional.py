"""These functional tests pass once their corresponding features are built."""

import pytest

import json
import math
import pandas as pd

#from heartandsole



def test_calculate_field():
  nT = 60
  data = dict(
    time=[i for i in range(nT)],
    distance=[i * 3.0 for i in range(nT)],
    speed=[3.0 for i in range(nT)],
    lon=[-105.4 - 0.0001*i for i in range(nT)],
    lat=[40.0 + 0.0001*i for i in range(nT)],
  )
  df = pd.DataFrame.from_dict(data)

  # Convert the DataFrame columns to a MultiIndex, making room for the
  # source label.
  df.columns = [(col, 'strava') for col in df.columns]
  # 
  # could also specify expected (normal) dtype and expected (pint) dtype and alt names??
  # heartandsole.register_field('speed')
  # heartandsole.register_field('distance')
  # heartandsole.register_field('time')
  #
  # Equivalent implementation of the above:
  # Using the input column labels: register each as a distinct field,
  # and convert them to level 0 of a (field, source) MultiIndex with a
  # default source name.
  # df = heartandsole.make_df(df, source='strava')

  speed_alt = df[('distance', 'strava')].diff() / df[('time', 'strava')].diff()
  #
  # New implementation:
  # @heartandsole.register_method('speed', inputs=['distance', 'time'])
  # def naive(distance, time):
  #   return distance.diff() / time.diff()
  #
  # speed_alt = df.act.speed.naive(distance='strava', time='strava')

  # Some other ways I could see it go:
  # speed_alt = df.field('distance').diff() / df.field('time').diff()
  # speed_alt = df.act.field('distance').diff() / df.act.field('time').diff()
  # speed_alt = df.act['distance'].diff() / df.act['time'].diff()

  # Core behavior of series produced by HNS:
  # assert speed_alt.act.field == 'speed'
  #
  # def assert_dicts_equal(dict1, dict2):
  #   assert set(dict1.items()) == set(dict2.items())
  #
  # assert isinstance(speed_alt.act.source, dict)
  # assert assert_dicts_equal(speed_alt.act.source.items()) == set(('distance', 'strava'), ('time', 'strava'))
  
  # Pint units: nice-to-have.
  # assert speed_alt.dtype == 'pint[m/s]' 

  # These are actually tests for in-the-weeds func, not core behavior.
  # (I could probably look to pandas for functional testing ideas.)
  assert isinstance(speed_alt.name, tuple)
  assert speed_alt.name[0] == 'speed'
  assert isinstance(speed_alt.name[1], dict)
  assert set(speed_alt.name[1].items()) == set(('distance', 'strava'), ('time', 'strava'))

  # I would love love love if somehow speed_alt would KNOW it was a
  # calculated quantity that came from these specific sources. The units
  # could track, and the sources could track, and it would all be great.
  # Basically: `sources = {'distance': 'strava', 'time': 'strava'}`
  # Why did I have it as a separate source class? JSON is all I need.
  # But to WHAT do I attach it?