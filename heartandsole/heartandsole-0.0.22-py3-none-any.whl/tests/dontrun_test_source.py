import datetime
import math

import numpy as np
from numpy.testing import assert_array_equal, assert_allclose
import pandas
from pandas.util.testing import assert_frame_equal, assert_series_equal
import unittest

from heartandsole.source import (
    LatlonSource, DistanceSource, TimeSource, ElevationSource,
    HeartRateSource, GradeSource, SpeedSource, CadenceSource,
    CadenceSource, MovingSource)
import config

class BaseTestCases:
  """Wrap base test class in a blank class so unittest doesnt run it."""

  class BaseSourceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
      # Simple named source
      cls.instances = {
        'name': cls.SOURCE('device'),
        #'mapmatch': self.SOURCE(mapmatch='alg_1', latlon_source='device'),
      }
  
      # Iterate through all sets of admissable kwargs and use them to
      # create an instance of the source class.
      for method_nm, src_dict in cls.ATTRS.items():
        #cls.instances['mapmatch'] = LatlonSource(mapmatch='alg_1',
        #                                         latlon_source='device')
        kwarg_dict = {method_nm: 'alg_1'}
        for attr_nm in src_dict.keys():
          kwarg_dict[attr_nm] = 'device'
  
        cls.instances[method_nm] = cls.SOURCE(**kwarg_dict)
  
    def test_units(self):
  
      # Verify that units are set to default without user input.
      self.assertEqual(self.instances['name'].units, self.SOURCE.DEFAULT_UNITS)
  
      def check_equal(list_check):
        iterator = iter(list_check)
        try:
          first = next(iterator)
        except StopIteration:
          return True
        return all(first == rest for rest in iterator)
  
      ins_list = []
      for default_units, alt_units_list in self.SOURCE.RECOGNIZED_UNITS.items():
  
        ins_list.append(self.SOURCE('device', units=default_units))
  
        for alt_units in alt_units_list:
          # Confirm that alternate units are recognized and converted to
          # the default type.
          ins = self.SOURCE('device', units=alt_units)
          self.assertEqual(ins.units, default_units)
  
          ins_list.append(ins)
  
      # Confirm each *Source is equal to all others, regardless of units.
      self.assertTrue(check_equal(ins_list))
  
    def test_attrs(self):
      def verify_attr(instance, name, value):
        self.assertTrue(hasattr(instance, name))
  
        if value is None:
          self.assertIsNone(getattr(instance, name))
        else:
          self.assertEqual(getattr(instance, name), value)
  
      # Is it necessary to have a 'source_name' attribute? I think?
      verify_attr(self.instances['name'], 'source_name', 'device')
  
      verify_attr(self.instances['name'], 'method_name', 'name')
  
      for method_nm, src_dict in self.ATTRS.items():
        verify_attr(self.instances['name'], method_nm, None)
  
        verify_attr(self.instances[method_nm], 'source_name', None)
        verify_attr(self.instances[method_nm], 'method_name', method_nm)
        verify_attr(self.instances[method_nm], method_nm, 'alg_1')
   
  
        # Confirm all other instances in the dict have this `method_nm`
        # attribute (eg `speed_calc`), but it is None.
        for method_nm_other, instance in self.instances.items():
          if method_nm_other != method_nm:
            verify_attr(instance, method_nm, None)
  
        for src_nm, src_type in src_dict.items():
          verify_attr(self.instances['name'], src_nm, None)
  
          verify_attr(self.instances[method_nm], src_nm, src_type('device'))
  
          # TODO: Confirm all other instances in the dict have this
          #       src_nm attribute (eg 'latlon_source'), but it is None.
          #       Hmm...realizing that isn't necessarily gonna be true.
  
    def test_equality(self):
      self.assertNotEqual(self.instances['name'],
                          self.SOURCE('strava'))
  
      # Verify no two instances are equal.
      for instance in self.instances.values():
        instances_other = list(self.instances.values())
        instances_other.remove(instance)
        for instance_other in instances_other:
          self.assertNotEqual(instance, instance_other)
  
      # TODO: Find a way to verify inequality when any parameter is
      #       different, eg Source(mapmatch='tz', latlon_source='device')
      #                     Source(mapmatch='tz', latlon_source='device2')
  
      # Verify that providing an argument negates the effects of kwargs.
      kwarg_dict = {method_nm: 'alg_1' for method_nm in self.ATTRS.keys()}
      for src_dict in self.ATTRS.values():
        for src_nm in src_dict:
          kwarg_dict[src_nm] = 'device'
      instance_all = self.SOURCE('device', **kwarg_dict)
      self.assertEqual(self.instances['name'], instance_all)
  
    def test_errors(self):
      with self.assertRaises(TypeError) as cm:
        ins = self.SOURCE()
  
      # TODO: Finish implementing logic from other tests.

class TestLatlonSource(BaseTestCases.BaseSourceTest):
  SOURCE = LatlonSource
  ATTRS = {
      'mapmatch': {'latlon_source': LatlonSource,},
  }
  #ATTRS = {
  #    'mapmatch': ('latlon_source',),
  #}
  #ATTRS = [
  #    ('mapmatch', 'latlon_source'),
  #]
  UNITS = {
      '180': [180],
      '360': [360]
  }
  #UNITS = {
  #    'decimal': ['dec'],
  #    'percent': ['%'],
  #}

class TestLatlonSourceTmp(unittest.TestCase):

  def test_errors(self):
    # a simple named source
    ll = LatlonSource('device')
    #self.assertEqual(ll.source_name, 'device')
    #self.assertIsNone(ll.mapmatch)
    #self.assertIsNone(ll.latlon_source)
    #self.assertEqual(ll.units, '180')
    #self.assertNotEqual(ll.units, '360')
    #self.assertEqual(ll.method_name, 'name')

    # an equivalent source, with different units
    ll_2 = LatlonSource('device', units='360')
    #self.assertEqual(ll, ll_2)

    # a non-equal source
    ll_un = LatlonSource('strava')
    #self.assertNotEqual(ll, ll_un)

    # a mapmatched source (2 equivalent constuctors)
    ll_3 = LatlonSource(mapmatch='tz', latlon_source=LatlonSource('device'))
    ll_4 = LatlonSource(mapmatch='tz', latlon_source='device')
    #self.assertNotEqual(ll_3, ll_2)
    #self.assertEqual(ll_3, ll_4)

    # What is this?
    self.assertIsNone(ll_3.source_name)

    #self.assertEqual(ll_3.mapmatch, 'tz')
    #self.assertEqual(ll_3.latlon_source, LatlonSource('device'))
    #self.assertEqual(ll_3.units, '180')
    #self.assertNotEqual(ll_3.units, '360')
    #self.assertEqual(ll_3.method_name, 'mapmatch')

    # 2 non-equivalent constructors
    ll_3_un_a = LatlonSource(mapmatch='mapbox', latlon_source='device')
    ll_3_un_b = LatlonSource(mapmatch='tz', latlon_source='strava')
    #self.assertNotEqual(ll_3, ll_3_un_a)
    #self.assertNotEqual(ll_3, ll_3_un_b)

    # now one with a source_name arg, so all kwargs should not matter
    ll_5 = LatlonSource('device', mapmatch='tz',
                        latlon_source=LatlonSource('device'))
    #self.assertEqual(ll_5.source_name, 'device')
    #self.assertEqual(ll_5.method_name, 'name')
    #self.assertIsNone(ll_5.mapmatch)
    #self.assertIsNone(ll_5.latlon_source)


    # ADS HERE: We are going through the old tests and putting the
    #           logic into the new test class.

    # TODO: Transcribe to test_errors.
    print_ex = False

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(mapmatch='tz', latlon_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(mapmatch=None, latlon_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(mapmatch=LatlonSource('tz'), latlon_source='tz')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      ll = LatlonSource(mapmatch='tz', latlon_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      ll = LatlonSource('device', units='one_eighty')
    if print_ex:
      print(cm.exception)


class TestDistanceSource(BaseTestCases.BaseSourceTest):
  SOURCE = DistanceSource
  ATTRS = {
      'pos_calc': {'latlon_source': LatlonSource},
      'speed_calc': {
          'speed_source': SpeedSource,
          'time_source': TimeSource,
      },
  }
  UNITS = {
      'meters': ['m', 'meter', 'metre', 'metres', 'metric', 'si'],
      'feet': ['ft', 'foot'],
      'miles': ['mi', 'mile', 'imperial'],
      'kilometers': ['kilometer', 'km', 'kilometre', 'kilometres']
  }

  def test_whatever(self):
    #print(dir(self.instances['name']))
    pass

class TestDistanceSourceTmp(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.ins_name = DistanceSource('device')
    cls.ins_pos_calc = DistanceSource(pos_calc='default',
                                      latlon_source='device')
    cls.ins_speed_calc = DistanceSource(speed_calc='default',
                                        speed_source='device', time_source='device')
    cls.ins_all = DistanceSource('device', pos_calc='default',
                                 latlon_source='device', 
                                 speed_calc='proprietary',
                                 speed_source='strava', time_source='device')

  def test_units(self):
    self.assertEqual(self.ins_name.units, 'meters')

    unit_tup_list = [('meters', 'm', 'meter', 'metre', 'metres', 'metric', 'si'),
                     ('feet', 'ft', 'foot'),
                     ('miles', 'mi', 'mile', 'imperial'),
                     ('kilometers', 'km', 'kilometer', 'kilometre',
                      'kilometres')]
    for unit_tup in unit_tup_list:
      default_units = unit_tup[0]
      for unit in unit_tup:
        # Confirm that the units are recognized and converted to the
        # default type.
        ins = DistanceSource('device', units=unit)
        self.assertEqual(ins.units, default_units)

        # Confirm this DistanceSource is equal to all others,
        # regardless of units.
        for unit_other in [item for sublist in unit_tup_list for item in sublist]:
          self.assertEqual(ins, DistanceSource('device', units=unit_other))

  def test_attribs(self):
    self.assertEqual(self.ins_name.source_name, 'device')
    self.assertIsNone(self.ins_pos_calc.source_name)
    self.assertIsNone(self.ins_speed_calc.source_name)
    
    self.assertIsNone(self.ins_name.pos_calc)
    self.assertEqual(self.ins_pos_calc.pos_calc, 'default')
    self.assertIsNone(self.ins_speed_calc.pos_calc)

    self.assertIsNone(self.ins_name.latlon_source)
    self.assertEqual(self.ins_pos_calc.latlon_source, LatlonSource('device'))
    self.assertIsNone(self.ins_speed_calc.latlon_source)

    self.assertIsNone(self.ins_name.speed_calc)
    self.assertIsNone(self.ins_pos_calc.speed_calc)
    self.assertEqual(self.ins_speed_calc.speed_calc, 'default')

    self.assertIsNone(self.ins_name.speed_source)
    self.assertIsNone(self.ins_pos_calc.speed_source)
    self.assertEqual(self.ins_speed_calc.speed_source, SpeedSource('device'))

  def test_equality(self):

    self.assertNotEqual(self.ins_name, DistanceSource('strava'))
    self.assertNotEqual(self.ins_pos_calc,
                        DistanceSource(pos_calc='default',
                                       latlon_source='strava'))
    self.assertNotEqual(self.ins_pos_calc,
                        DistanceSource(pos_calc='proprietary',
                                       latlon_source='device'))
    self.assertNotEqual(self.ins_speed_calc,
                        DistanceSource(speed_calc='default',
                                       speed_source='strava', time_source='device'))
    self.assertNotEqual(self.ins_speed_calc,
                        DistanceSource(speed_calc='proprietary',
                                       speed_source='device', time_source='device'))

    self.assertNotEqual(self.ins_speed_calc,
                        DistanceSource(speed_calc='default',
                                       speed_source='device', time_source='mine'))

    self.assertNotEqual(self.ins_name, self.ins_pos_calc)
    self.assertNotEqual(self.ins_name, self.ins_speed_calc)
    self.assertNotEqual(self.ins_pos_calc, self.ins_speed_calc)

    self.assertEqual(self.ins_pos_calc,
                     DistanceSource(pos_calc='default',
                                    latlon_source=LatlonSource('device')))

    self.assertEqual(self.ins_speed_calc,
                     DistanceSource(speed_calc='default',
                                    speed_source=SpeedSource('device'),
                                    time_source='device'))

    self.assertEqual(self.ins_name, self.ins_all)

  def test_errors(self):
    # a simple named source
    ins = DistanceSource('device')
    self.assertEqual(ins.source_name, 'device')
    self.assertIsNone(ins.pos_calc)
    self.assertIsNone(ins.latlon_source)
    self.assertEqual(ins.method_name, 'name')

    print_ex = False

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(pos_calc='default', latlon_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(pos_calc=None, latlon_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(pos_calc=1, latlon_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(pos_calc='default', latlon_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(speed_calc='default', speed_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(speed_calc=None, speed_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(speed_calc=1, speed_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(speed_calc='default', speed_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = DistanceSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = DistanceSource('device', units='lsajfdlsa')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = DistanceSource('device', units=1)
    if print_ex:
      print(cm.exception)


class TestSpeedSource(BaseTestCases.BaseSourceTest):
  SOURCE = SpeedSource
  ATTRS = {
      'dist_calc': {
          'dist_source': DistanceSource,
          'time_source': TimeSource,
      },
  }
  UNITS = {
      'ms': ['m/s', 'meters per second', 'meter per second',
             'metres per second', 'metre per second', 'metric', 'si'],
      'mph': ['miles per hour', 'mile per hour', 'mi per hour', 'miles per hr',
              'mile per hr', 'mi per hr', 'imperial']
  }

  def test_whatever(self):
    #print(dir(self.instances['name']))
    pass

class TestSpeedSourceTmp(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.ins_name = SpeedSource('device')
    cls.ins_dist_calc = SpeedSource(dist_calc='default',
                                    dist_source='device', time_source='device')
    cls.ins_all = SpeedSource('device', dist_calc='proprietary',
                              dist_source='strava', time_source='device')

  def test_units(self):
    self.assertEqual(self.ins_name.units, 'ms')

    unit_tup_list = [('ms', 'm/s', 'meters per second', 'meter per second',
                      'metres per second', 'metre per second', 'metric', 'si'),
                     ('mph', 'miles per hour', 'mile per hour', 'mi per hour',
                      'miles per hr', 'mile per hr', 'mi per hr', 'imperial')]

    for unit_tup in unit_tup_list:
      default_units = unit_tup[0]
      for unit in unit_tup:
        # Confirm that the units are recognized and converted to the
        # default type.
        ins = SpeedSource('device', units=unit)
        self.assertEqual(ins.units, default_units)

        # Confirm this SpeedSource is equal to all others,
        # regardless of units.
        for unit_other in [item for sublist in unit_tup_list for item in sublist]:
          self.assertEqual(ins, SpeedSource('device', units=unit_other))

  def test_attribs(self):
    self.assertEqual(self.ins_name.source_name, 'device')
    self.assertIsNone(self.ins_dist_calc.source_name)
    
    self.assertEqual(self.ins_name.method_name, 'name')
    self.assertEqual(self.ins_dist_calc.method_name, 'dist_calc')

    self.assertIsNone(self.ins_name.time_source)
    self.assertEqual(self.ins_dist_calc.time_source, TimeSource('device'))

    self.assertIsNone(self.ins_name.dist_calc)
    self.assertEqual(self.ins_dist_calc.dist_calc, 'default')

    self.assertIsNone(self.ins_name.dist_source)
    self.assertEqual(self.ins_dist_calc.dist_source, DistanceSource('device'))

  def test_equality(self):
    self.assertNotEqual(self.ins_name, SpeedSource('strava'))
    self.assertNotEqual(self.ins_dist_calc,
                        SpeedSource(dist_calc='default',
                                    dist_source='strava', time_source='device'))
    self.assertNotEqual(self.ins_dist_calc,
                        SpeedSource(dist_calc='proprietary',
                                    dist_source='device', time_source='device'))

    self.assertNotEqual(self.ins_dist_calc,
                        SpeedSource(dist_calc='default',
                                    dist_source='device', time_source='mine'))

    self.assertNotEqual(self.ins_name, self.ins_dist_calc)

    self.assertEqual(self.ins_dist_calc,
                     SpeedSource(dist_calc='default',
                                 dist_source=DistanceSource('device'),
                                 time_source='device'))

    self.assertEqual(self.ins_name, self.ins_all)

  def test_errors(self):
    # a simple named source
    ins = SpeedSource('device')

    print_ex = False

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(dist_calc='default', dist_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(dist_calc=None, dist_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(dist_calc=1, dist_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(dist_calc='default', dist_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = SpeedSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = SpeedSource('device', units='lsajfdlsa')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = SpeedSource('device', units=1)
    if print_ex:
      print(cm.exception)


class TestTimeSource(BaseTestCases.BaseSourceTest):
  SOURCE = TimeSource
  ATTRS = {}
  UNITS = {
      'seconds': ['s', 'sec', 'secs'],
  }

class TestTimeSourceTmp(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = TimeSource('device')

  def test_units(self):
    self.assertEqual(self.ins_name.units, 'seconds')

    unit_tup_list = [('seconds', 's', 'sec', 'secs'),]

    for unit_tup in unit_tup_list:
      default_units = unit_tup[0]
      for unit in unit_tup:
        # Confirm that the units are recognized and converted to the
        # default type.
        ins = TimeSource('device', units=unit)
        self.assertEqual(ins.units, default_units)

        # Confirm this SpeedSource is equal to all others,
        # regardless of units.
        for unit_other in [item for sublist in unit_tup_list for item in sublist]:
          self.assertEqual(ins, TimeSource('device', units=unit_other))

  def test_attribs(self):
    self.assertEqual(self.ins_name.source_name, 'device')

    self.assertEqual(self.ins_name.method_name, 'name')

  def test_equality(self):
    self.assertNotEqual(self.ins_name, TimeSource('strava'))

  def test_errors(self):
    print_ex = False

    with self.assertRaises(TypeError) as cm:
      d = TimeSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = TimeSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = TimeSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = TimeSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = TimeSource('device', units='lsajfdlsa')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = TimeSource('device', units=1)
    if print_ex:
      print(cm.exception)


class TestElevationSource(BaseTestCases.BaseSourceTest):
  SOURCE = ElevationSource
  ATTRS = {
      'dem': {'latlon_source': LatlonSource},
      'smoothing': {
          'elevation_source': ElevationSource,
          'time_source': TimeSource,
      },
  }
  UNITS = {
      'meters': ['m', 'meter', 'metre', 'metres', 'metric', 'si'],
      'feet': ['ft', 'foot', 'imperial'],
  }

  def test_whatever(self):
    #print(dir(self.instances['name']))
    pass

class TestElevationSource(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = ElevationSource('device')
    cls.ins_dem = ElevationSource(dem='default', # lidar?
                                  latlon_source='device')
    cls.ins_smoothing = ElevationSource(smoothing='default',
                                        elevation_source='device', time_source='device')
    cls.ins_all = ElevationSource('device', dem='default',
                                  latlon_source='device',
                                  smoothing='proprietary',
                                  elevation_source='strava', time_source='device')

  def test_units(self):
    self.assertEqual(self.ins_name.units, 'meters')

    unit_tup_list = [('meters', 'm', 'meter', 'metre', 'metres', 'metric', 'si'),
                     ('feet', 'ft', 'foot', 'imperial')]
    for unit_tup in unit_tup_list:
      default_units = unit_tup[0]
      for unit in unit_tup:
        # Confirm that the units are recognized and converted to the
        # default type.
        ins = ElevationSource('device', units=unit)
        self.assertEqual(ins.units, default_units)

        # Confirm this ElevationSource is equal to all others,
        # regardless of units.
        for unit_other in [item for sublist in unit_tup_list for item in sublist]:
          self.assertEqual(ins, ElevationSource('device', units=unit_other))

    self.assertNotEqual(self.ins_name, self.ins_dem)
    self.assertNotEqual(self.ins_name, self.ins_smoothing)
    self.assertNotEqual(self.ins_dem, self.ins_smoothing)

    self.assertEqual(self.ins_dem,
                     ElevationSource(dem='default',
                                    latlon_source=LatlonSource('device')))

    self.assertEqual(self.ins_smoothing,
                     ElevationSource(smoothing='default',
                                     elevation_source=ElevationSource('device'),
                                     time_source='device'))

    self.assertEqual(self.ins_name, self.ins_all)

  def test_attribs(self):
    self.assertEqual(self.ins_name.source_name, 'device')
    self.assertIsNone(self.ins_dem.source_name)
    self.assertIsNone(self.ins_smoothing.source_name)

    self.assertIsNone(self.ins_name.dem)
    self.assertEqual(self.ins_dem.dem, 'default')
    self.assertIsNone(self.ins_smoothing.dem)

    self.assertIsNone(self.ins_name.latlon_source)
    self.assertEqual(self.ins_dem.latlon_source, LatlonSource('device'))
    self.assertIsNone(self.ins_smoothing.latlon_source)

    self.assertIsNone(self.ins_name.smoothing)
    self.assertIsNone(self.ins_dem.smoothing)
    self.assertEqual(self.ins_smoothing.smoothing, 'default')

    self.assertIsNone(self.ins_name.elevation_source)
    self.assertIsNone(self.ins_dem.elevation_source)
    self.assertEqual(self.ins_smoothing.elevation_source, ElevationSource('device'))

  def test_equality(self):

    self.assertNotEqual(self.ins_name, ElevationSource('strava'))
    self.assertNotEqual(self.ins_dem,
                        ElevationSource(dem='default',
                                       latlon_source='strava'))
    self.assertNotEqual(self.ins_dem,
                        ElevationSource(dem='proprietary',
                                       latlon_source='device'))
    self.assertNotEqual(self.ins_smoothing,
                        ElevationSource(smoothing='default',
                                       elevation_source='strava', time_source='device'))
    self.assertNotEqual(self.ins_smoothing,
                        ElevationSource(smoothing='proprietary',
                                       elevation_source='device', time_source='device'))

    self.assertNotEqual(self.ins_smoothing,
                        ElevationSource(smoothing='default',
                                       elevation_source='device', time_source='mine'))

  def test_errors(self):
    # a simple named source
    ins = ElevationSource('device')
    self.assertEqual(ins.source_name, 'device')
    self.assertIsNone(ins.dem)
    self.assertIsNone(ins.latlon_source)
    self.assertEqual(ins.method_name, 'name')

    print_ex = False

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(dem='default', latlon_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(dem=None, latlon_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(dem=1, latlon_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(dem='default', latlon_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(smoothing='default', elevation_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(smoothing=None, elevation_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(smoothing=1, elevation_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(smoothing='default', elevation_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = ElevationSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = ElevationSource('device', units='lsajfdlsa')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = ElevationSource('device', units=1)
    if print_ex:
      print(cm.exception)


class TestGradeSource(BaseTestCases.BaseSourceTest):
  SOURCE = GradeSource
  ATTRS = {
      'calc': {
          'elevation_source': ElevationSource,
          'dist_source': DistanceSource,
          #'time_source': TimeSource,  # later
      },
  }
  UNITS = {
      'decimal': ['dec'],
      'percent': ['%'],
  }

  def test_whatever(self):
    #print(dir(self.instances['name']))
    pass

class TestGradeSourceTmp(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = GradeSource('device')
    cls.ins_calc = GradeSource(calc='default', elevation_source='device',
                               dist_source='device')
    cls.ins_all = GradeSource('device', calc='proprietary', 
                              elevation_source='device', dist_source='strava')

  def test_units(self):
    self.assertEqual(self.ins_name.units, 'decimal')

    unit_tup_list = [('decimal', 'dec'), ('percent', '%')]

    for unit_tup in unit_tup_list:
      default_units = unit_tup[0]
      for unit in unit_tup:
        # Confirm that the units are recognized and converted to the
        # default type.
        ins = GradeSource('device', units=unit)
        self.assertEqual(ins.units, default_units)

        # Confirm this GradeSource is equal to all others,
        # regardless of units.
        for unit_other in [item for sublist in unit_tup_list for item in sublist]:
          self.assertEqual(ins, GradeSource('device', units=unit_other))

  def test_attribs(self):
    self.assertEqual(self.ins_name.source_name, 'device')
    self.assertIsNone(self.ins_calc.source_name)

    self.assertEqual(self.ins_name.method_name, 'name')
    self.assertEqual(self.ins_calc.method_name, 'calc')

    self.assertIsNone(self.ins_name.calc)
    self.assertEqual(self.ins_calc.calc, 'default')

    self.assertIsNone(self.ins_name.elevation_source)
    self.assertEqual(self.ins_calc.elevation_source, ElevationSource('device'))

    self.assertIsNone(self.ins_name.dist_source)
    self.assertEqual(self.ins_calc.dist_source, DistanceSource('device'))

  def test_equality(self):
    self.assertNotEqual(self.ins_name, GradeSource('strava'))
    self.assertNotEqual(self.ins_calc,
                        GradeSource(calc='default',
                                    dist_source='strava', elevation_source='device'))
    self.assertNotEqual(self.ins_calc,
                        GradeSource(calc='proprietary',
                                    dist_source='device', elevation_source='device'))

    self.assertNotEqual(self.ins_calc,
                        GradeSource(calc='default',
                                    dist_source='device', elevation_source='mine'))

    self.assertNotEqual(self.ins_name, self.ins_calc)

    self.assertEqual(self.ins_calc,
                     GradeSource(calc='default',
                                 dist_source=DistanceSource('device'),
                                 elevation_source=ElevationSource('device')))

    self.assertEqual(self.ins_name, self.ins_all)

  def test_errors(self):
    # a simple named source
    ins = GradeSource('device')

    print_ex = False

    with self.assertRaises(TypeError) as cm:
      d = GradeSource()
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(calc='default', dist_source=None)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(calc=None, dist_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(calc=1, dist_source='device')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(calc='default', dist_source=1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(1)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(TypeError) as cm:
      d = GradeSource(1.0)
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = GradeSource('device', units='lsajfdlsa')
    if print_ex:
      print(cm.exception)

    with self.assertRaises(ValueError) as cm:
      d = GradeSource('device', units=1)
    if print_ex:
      print(cm.exception)


class TestMovingSource(BaseTestCases.BaseSourceTest):
  SOURCE = MovingSource
  ATTRS = {}
  UNITS = {
      None: [None,],
  }

class TestMovingSourceTmp(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = MovingSource('device')

  def test_tmp(self):
    self.assertIsNone(self.ins_name.units)
    self.assertEqual(self.ins_name.method_name, 'name')
    self.assertEqual(self.ins_name.source_name, 'device')

class TestCadenceSource(BaseTestCases.BaseSourceTest):
  SOURCE = CadenceSource
  ATTRS = {}
  UNITS = {
      'spm': ['strides per minute',],
      'rpm': ['revolutions per minute',],
  }

class TestCadenceSourceTmp(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = CadenceSource('device')

  def test_tmp(self):
    self.assertEqual(self.ins_name.units, 'spm')
    self.assertEqual(self.ins_name.method_name, 'name')
    self.assertEqual(self.ins_name.source_name, 'device')


class TestHeartRateSource(BaseTestCases.BaseSourceTest):
  SOURCE = HeartRateSource
  ATTRS = {}
  UNITS = {
      'bpm': ['beats per minute',],
  }

class TestHeartRateSourceTmp(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.ins_name = HeartRateSource('device')

  def test_tmp(self):
    self.assertEqual(self.ins_name.units, 'bpm')
    self.assertEqual(self.ins_name.method_name, 'name')
    self.assertEqual(self.ins_name.source_name, 'device')


#    print(TimeSource('device'))
#
#    print(ElevationSource('device'))
#    print(ElevationSource(latlon, dem='lidar'))
#    elev_src = ElevationSource(ElevationSource('device'), time_source='strava')
#    #print(ElevationSource(latlon))
#
#    print(GradeSource('device'))
#    print(GradeSource(distance_source='device', elevation_source='device'))
#    print(GradeSource(distance_source=dist_src_ll, elevation_source=elev_src))
#
#    print(HeartRateSource('device'))
#    print(CadenceSource('device'))
#    print(MovingSource('strava'))    
#
