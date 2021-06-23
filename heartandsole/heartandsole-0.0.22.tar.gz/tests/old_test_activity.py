"""Vestigial tests for old/nixed Activity features."""

import datetime
import math

import fitparse
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose
import pandas
from pandas.util.testing import assert_frame_equal, assert_series_equal
import spatialfriend
import unittest

from heartandsole.activity import Activity  # , HnsException
from heartandsole.filereaders import FitFileReader, TcxFileReader
from heartandsole.labels import SourceLabel
import heartandsole.powerutils as pu
from heartandsole import source
import heartandsole.util
import config

 
class TestActivity(unittest.TestCase):
  # TODO: Separate into TestCases for input data handling,
  #       output data types, and output with missing fields.

  # @classmethod
  # def setUpClass(cls):
  def setUp(self):
    # Create a DataFrame that is formatted correctly for consumption
    # by Activity. This DataFrame has all available fields.
    nT = 60
    v = 3.0
    data = dict(
      #timestamp=[datetime.datetime(2019, 9, 1, second=i) for i in range(nT)],
      time=[i for i in range(nT)],
      distance=[i * 3.0 for i in range(nT)],
      displacement=[3.0 for i in range(nT)],
      speed=[3.0 for i in range(nT)],
      elevation=[1.0 * i for i in range(nT)],
      lat=[40.0 + 0.0001*i for i in range(nT)],
      lon=[-105.4 - 0.0001*i for i in range(nT)],
      heart_rate=[140.0 + 5.0 * math.sin(i * math.pi/10) for i in range(nT)],
      cadence=[170.0 + 5.0 * math.cos(i * math.pi/10) for i in range(nT)],
      moving=[bool(i > nT / 2) for i in range(nT)],
      grade=[0.2 * i / nT for i in range(nT)]
      #running_smoothness=[170.0 + 5.0 * math.cos(i * math.pi/10) for i in range(nT)],
      #stance_time=[250.0 + 25.0 * math.cos(i * math.pi/10) for i in range(nT)],
      #vertical_oscillation=[12.5 + 2.0 * math.cos(i * math.pi/10) for i in range(nT)],
    )

    self.df = pandas.DataFrame(data)
    #self.df = pandas.DataFrame(data, index=pandas.RangeIndex(nT))
    #self.df.index.name = 'record'

    # Create a MultiIndexed DataFrame to simulate data read from CSV etc.
    self.df_multi = self.df.copy()
    index_tups = [(field_name, 'device') for field_name in self.df.columns]
    # Worthwhile to test what happens when the csv file still uses
    # 'elev_source' instead of 'source', but not right here.
    self.df_multi.columns = pandas.MultiIndex.from_tuples(index_tups,
                                                          names=('field', 'source'))

    # Create an Activity with simulated input from a FileReader.
    self.act = Activity(self.df)

    #self.act_multi = Activity(df_multi)

    #print(cls.act.data.columns)
    #cls.act.data.time.set_default('device')
    #cls.act.data.time.set_default('momo')
    #print(cls.act.data.time._default_source_name)

    #geo = cls.act.geo

    ## Create an Activity with simulated input from a FileReader
    ## without elevation data.
    #df_single_noel = df_single.drop(columns=['elevation'])
    #cls.act_noel = Activity(df_single_noel, remove_stops=False)

    ## Create a MultiIndexed DataFrame to simulate data read from CSV etc.
    #index_tups = [(field_name, 'device') for field_name in df_single.columns]
    #df_double = df_single.copy()
    ## Worthwhile to test what happens when the csv file still uses
    ## 'elev_source' instead of 'source', but not right here.
    #df_double.columns = pandas.MultiIndex.from_tuples(index_tups,
    #                                                  names=('field', 'source'))

    ## Create an Activity with simulated input from a fully-formed 
    ## DataFrame.
    #cls.act_double = Activity(df_double, remove_stops=False)

    # Integration test: add a new elevation source to an 
    # existing activity.
    # TODO: Figure out where this really makes sense.
    elevs = self.act.data.elevation.get_series()
    #self.act.add_elevation_source(elevs, 'test_src')
    self.act.data = self.act.data.elevation.add_col('test_src', elevs + 1.0)
  
  def test_create(self):
    df = self.df.copy()

    # Create a MultiIndexed DataFrame to simulate data read from CSV etc.
    index_tups = [(field_name, 'device') for field_name in df.columns]
    df_multi = df.copy()

    # Worthwhile to test what happens when the csv file still uses
    # 'elev_source' instead of 'source', but not right here.
    df_multi.columns = pandas.MultiIndex.from_tuples(index_tups,
                                                     names=('field', 'source'))

    act = Activity(df)
    act_multi = Activity(df_multi)

    assert_frame_equal(act.data, act_multi.data)

  def test_moving_time(self):
    self.assertIsInstance(self.act.moving_time,
                          datetime.timedelta)
    self.assertIsInstance(self.act.data.time.moving(),
                          datetime.timedelta)
    # TODO: Not sure.
    self.assertEqual(self.act.moving_time.total_seconds(),
                     59)

  def test_elapsed_time(self):
    self.assertIsInstance(self.act.elapsed_time,
                          datetime.timedelta)

  def test_mean_cadence(self):
    # Best we got right now. We will see whether a method is called for.
    #self.assertIsInstance(self.act.mean_cadence(),
    self.assertIsInstance(self.act.data.cadence.get_series().mean(),
                          float)

  def test_elevation(self):
    df = pandas.DataFrame.from_dict({
        ('elevation', 'device'): [0., 0.1, 0.3, 0.],
        ('elevation', 'alt_src'): [0., 0.2, 0.6, 0.4]
        })

    act = Activity(df)

    # The algorithms are not the ones on trial here today, sir!
    self.assertIsInstance(
      act.data.elevation.threshold_filter(),
      pandas.Series)

    self.assertIsInstance(
      act.data.elevation.flatten_series(),
      pandas.Series)

    self.assertIsInstance(
      act.data.elevation.gain(),
      float)

    self.assertIsInstance(
      act.data.elevation.loss(),
      float)

    # Accomplish two things (indirectly):
    #   - Demonstrate usage of the elevation smoothing method, which
    #     is finicky about the interactions of parameters and array
    #     lengths.
    #   - Verify that the function underlying the method can
    #     successfully receive any stray kwargs (anything not 'source'
    #     or a field name).
    self.assertIsInstance(
      act.data.elevation.time_smooth(window_len=3),
      pandas.Series)

    self.assertAlmostEqual(act.data.elevation.gain(), 0.3)
    self.assertAlmostEqual(act.data.elevation.gain(source='alt_src'), 0.6)
    self.assertAlmostEqual(act.data.elevation.loss(), 0.3)
    self.assertAlmostEqual(act.data.elevation.loss(source='alt_src'), 0.2)

  def test_accessor_methods(self):
    """Test representative behavior for registered accessor methods."""

    df = pandas.DataFrame.from_dict(dict(
      lat=[0., 0., 0.],
      lon=[0., 1., 2.],
      elevation=[1600., 1700., 1800.]
      ))

    act = Activity(df)

    data_before = act.data.copy()

    # Raise a KeyError since no grade column exists yet.
    self.assertRaises(AttributeError, self.act.data.grade.get_series)

    #grade_series = act.data.grade.calc()  # I want this to work!
    
    # Well that actually works pretty slick!
    #                     act.data.grade.calc(displacement=SourceLabel('from_latlon'))
    self.assertIsInstance(act.data.grade.calc(displacement='from_latlon'),
                          pandas.Series)

    # This is technically equivalent. Disgusting!
    grade_label = SourceLabel('calc',
                              displacement=SourceLabel('from_latlon',
                                                       lat='device',
                                                       lon='device'),
                              elevation='device')
    self.assertIsInstance(
      act.data.grade.get_series(source=grade_label),
      pandas.Series)

    # Ensure the underlying data remains unchanged.
    assert_frame_equal(act.data, data_before)

    # Now use the same method to create a new DF with the calcd col.
    data_after = act.data.grade.calc(displacement='from_latlon', add_col=True)
    self.assertIsInstance(data_after, pandas.DataFrame)

    # Equivalent tests, I think.
    self.assertIn('grade', data_after.columns.get_level_values(0))
    self.assertTrue(data_after.grade.has_data)

    self.assertTrue(
        data_after.grade.has_source(grade_label))

  def test_grade_calc(self):
    df = pandas.DataFrame.from_dict(dict(
      displacement=[0., 1., 2.],
      elevation=[0., 0.1, 0.3]))

    self.assertIsInstance(
      self.act.data.grade.calc(elevation='device',
                               displacement='device',
      ),
      pandas.Series)

  def test_speed_type(self):
    self.assertIsInstance(self.act.data.speed.get_series(),
                          pandas.Series)

  def test_o2_power_tend_type(self):
    self.assertIsInstance(self.act._o2_power_tend_series(),
                          pandas.Series,
                          'o2 power should be a pandas.Series.')

  def test_o2_power_tend_alt_type(self):
    self.assertIsInstance(self.act._o2_power_tend_series(elev_source='test_src'),
                          pandas.Series,
                          'o2 power should be a pandas.Series.')

  def test_o2_power_type(self):
    self.assertIsInstance(self.act.o2_power_series(),
                          pandas.Series,
                          'o2 power should be a pandas.Series.')

  def test_o2_power_alt_type(self):
    self.assertIsInstance(self.act.o2_power_series(elev_source='test_src'),
                          pandas.Series,
                          'o2 power should be a pandas.Series.')

  def test_mean_power_type(self):
    self.assertIsInstance(self.act.mean_power(),
                          float,
                          'Mean power should be a float')

  def test_mean_power_alt_type(self):
    self.assertIsInstance(self.act.mean_power(elev_source='test_src'),
                          float,
                          'Mean power should be a float')

  def test_norm_power_type(self):
    self.assertIsInstance(self.act.norm_power(),
                          float,
                          'Normalized power should be a float')

  def test_norm_power_alt_type(self):
    self.assertIsInstance(self.act.norm_power(elev_source='test_src'),
                          float,
                          'Normalized power should be a float')

  def test_power_intensity_type(self):
    pwr = pu.flat_run_power('6:30')
    self.assertIsInstance(self.act.power_intensity(pwr),
                          float,
                          'Power-based intensity should be a float')

  def test_power_intensity_alt_type(self):
    pwr = pu.flat_run_power('6:30')
    self.assertIsInstance(self.act.power_intensity(pwr,
                                                   elev_source='test_src'),
                          float,
                          'Power-based intensity should be a float')

  def test_power_training_stress_type(self):
    pwr = pu.flat_run_power('6:30')
    self.assertIsInstance(self.act.power_training_stress(pwr),
                          float,
                          'Power-based training stress should be a float')

  def test_power_training_stress_alt_type(self):
    pwr = pu.flat_run_power('6:30')
    self.assertIsInstance(self.act.power_training_stress(pwr,
                                                         elev_source='test_src'),
                          float,
                          'Power-based training stress should be a float')

  def test_mean_heart_rate_type(self):
    self.assertIsInstance(self.act.mean_heart_rate(),
                          float,
                          'Mean heart rate should be a float')

  def test_heart_rate_intensity_type(self):
    self.assertIsInstance(self.act.heart_rate_intensity(160),
                          float,
                          'HR-based intensity should be a float')

  def test_heart_rate_training_stress_type(self):
    self.assertIsInstance(self.act.heart_rate_training_stress(160),
                          float,
                          'HR-based training stress should be a float')

  def test_source(self):
    self.assertTrue(self.act.has_source('elevation', 'test_src'))

  def test_equiv_speed_type(self):
    self.assertIsInstance(self.act.equiv_speed_series(),
                          pandas.Series,
                          'Equivalent pace should be a pandas.Series.')

  def test_equiv_speed_alt_type(self):
    self.assertIsInstance(self.act.equiv_speed_series(elev_source='test_src'),
                          pandas.Series,
                          'Equivalent pace should be a pandas.Series.')

  def test_mean_speed_type(self):
    self.assertIsInstance(self.act.mean_speed(),
                          float,
                          'Mean speed should be a float')

  def test_mean_equiv_speed_type(self):
    self.assertIsInstance(self.act.mean_equiv_speed(),
                          float,
                          'Mean equivalent speed should be a float')

  def test_mean_equiv_speed_alt_type(self):
    self.assertIsInstance(self.act.mean_equiv_speed(elev_source='test_src'),
                          float,
                          'Mean equivalent speed should be a float')


class TestDataFrameFormat(unittest.TestCase):
  """Test proper handling of the DataFrame passed as input."""

  @classmethod
  def setUpClass(cls):
    # Create a DataFrame that is formatted correctly for consumption
    # by Activity. This DataFrame has all available fields.
    nT = 60
    v = 3.0
    data = dict(
      #timestamp=[datetime.datetime(2019, 9, 1, second=i) for i in range(nT)],
      time=[i for i in range(nT)],
      distance=[i * 3.0 for i in range(nT)],
      speed=[3.0 for i in range(nT)],
      elevation=[1.0 * i for i in range(nT)],
      lat=[40.0 + 0.0001*i for i in range(nT)],
      lon=[-105.4 - 0.0001*i for i in range(nT)],
      heart_rate=[140.0 + 5.0 * math.sin(i * math.pi/10) for i in range(nT)],
      cadence=[170.0 + 5.0 * math.cos(i * math.pi/10) for i in range(nT)],
      moving=[bool(i % 2) for i in range(nT)],
      #running_smoothness=[170.0 + 5.0 * math.cos(i * math.pi/10) for i in range(nT)],
      #stance_time=[250.0 + 25.0 * math.cos(i * math.pi/10) for i in range(nT)],
      #vertical_oscillation=[12.5 + 2.0 * math.cos(i * math.pi/10) for i in range(nT)],
    )

    cls.df = pandas.DataFrame(data, index=pandas.RangeIndex(nT))

    # Create a MultiIndexed DataFrame to simulate data read from CSV etc.
    index_tups = [(field_name, 'device') for field_name in cls.df.columns]
    cls.df_multi = cls.df.copy()
    # Worthwhile to test what happens when the csv file still uses
    # 'elev_source' instead of 'source', but not right here.
    cls.df_multi.columns = pandas.MultiIndex.from_tuples(index_tups,
                                                         names=('field', 'source'))

  #def setUp(self):
  #  # Hopefully prevents the underlying dataframes from being messed
  #  # up from test to test.
  #  self.df = self.df.copy()

  #def tearDown(self):
  #  # self.df = None
  #  pass

  def test_no_exception(self):
    """Verify the DataFrames work as-is."""
    
    def verify_no_exc(df_test):
      try:
        act = Activity(df_test)
      except:
        self.fail('Activity creation with appropriate DF raised'  \
                  ' exception unexpectedly!')

    df = self.df.copy()
    df_multi = self.df_multi.copy()

    verify_no_exc(df)
    verify_no_exc(df_multi)
    df_multi.columns.rename(('fld', 'source'), inplace=True)
    verify_no_exc(df_multi)
    df_multi.columns.rename(('fld', 'source'), inplace=True)
    verify_no_exc(df_multi)


  def test_column_level_single(self):
    df = self.df.copy()
    self.assertIsNone(df.columns.name)

    # Default behavior with a single-level column structure:
    # assume all sources are 'device'
    act = Activity(df)
    self.assertEqual(act.data.columns.names, ('field', 'source'))
    self.assertIn(SourceLabel('device'),
                  act.data.columns.get_level_values('source'))    

    # Check that user-specified source name works.
    act = Activity(df, source_name='strava')
    self.assertIn(SourceLabel('strava'),
                  act.data.columns.get_level_values('source'))

  def test_row_name(self):
    df = self.df.copy()
    self.assertIsNone(df.index.name)

    act = Activity(df)
    self.assertEqual(act.data.index.name, 'record')

  def test_row_format(self):
    df = self.df.copy()

    # Verify the DataFrame index may be an IntegerIndex as well.
    df.index = pandas.Int64Index(range(len(df.index)))
    try:
      act = Activity(df)
    except:
      self.fail('Activity creation with appropriate DF index raised'  \
                ' exception unexpectedly!')

    # Verify an exception is raised when a MultiIndex is used.
    df.index = pandas.MultiIndex.from_arrays(
        [
            [0 for i in range(len(df.index))],
            [i for i in range(len(df.index))]
        ],
        names=('block', 'record')
    )
    self.assertRaisesRegex(TypeError,
        'DataFrame index should be some form of pd.Int64Index, not *',
        Activity, df)


class TestCsv(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.act = Activity.from_csv('activity_files/4057357331.csv')

  def test_1(self):
    pass


# classTestDuplicateTimestamp(unittest.TestCase):
#   """Now-unused diagnostic test for when timestamps aren't sequential."""
# 
#   def print_diffs(self, vals):
#     sum_diffs = 0
#     for i in range(len(vals)-1):
#       time_diff = vals[i+1] - vals[i]
#       if time_diff.total_seconds() != 1:
#         print('%s: %s' % (vals[i+1], time_diff.total_seconds() - 1))
#         sum_diffs += time_diff.total_seconds() - 1
#     print(sum_diffs)
# 
#   #def setUp(self):
#   @classmethod
#   def setUpClass(cls):
#     # Start with a typical file with duplicated timestamps.
#     reader = FitFileReader('activity_files/lexsort_4318998849.fit')
#     #reader = FitFileReader('activity_files/lexsort_4318995334.fit')
#     #reader = FitFileReader('activity_files/running_4390094641.fit')
#     #reader = FitFileReader('activity_files/runningmo_4386919092.fit')
# 
#     #heartandsole.util.print_full(reader.data)
#     #self.print_diffs(reader.data.index.get_level_values('offset'))
# 
#     activity = heartandsole.Activity(reader.data)
#     #self.print_diffs(activity.data.index.get_level_values('offset'))
# 
#   def test_create(self):
#     pass


if __name__ == '__main__':
  unittest.main()
