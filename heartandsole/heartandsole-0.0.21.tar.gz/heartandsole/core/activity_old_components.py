"""Things that made it into Activity at one point or another.

I'm keeping these for reference. Who knows if I'll put them back in.

"""


class Activity:
  def __init__(self, df):
    # Memoize for later
    self._default_sources = {}

    self.data = df.copy()

    # One way to register custom accessors for DataFrames (not used)
    #register_accessor('lat', ['latitude'], 'int64')

    # Verify that all desired accessors are registered.
    #print(pandas.DataFrame._accessors)

    # validate the data and then clean it up so the accessors do not
    # get angry.
    #self._validate(df)
    #self.data = self._cleanup(df) #  rename '_preclean()'?

    for accessor_name in self.data._accessors:
      # Just instantiating the accessor runs _validate, so
      # I do not need to explicitly check anything here.

      # Get the accessor class to clean up the data how it likes.
      accessor_cls = getattr(pd.DataFrame, accessor_name)
      self.data = accessor_cls.cleanup_data(self.data,
                                            source_name=source_name)
      
      # Instantiate the accessor now that data is clean.
      accessor = getattr(self.data, accessor_name)
      # accessor._validate()
      #self.data = accessor._cleanup(self.data)
      #self.data = accessor.cleanup_data(self.data)

      # Might be None, if there is no data!
      self._default_sources[accessor_name] = accessor.default_source

    if enforce_sequential_times:
      # TODO: Make this into a TimeAccessor method - add a column
      #       with sequential times. Or simply:
      self.data = self.data.time.add_col(range(len(self.data)), source='sequential')
      self._default_sources['time'] = SourceLabel('sequential')

    ## Calculate elapsed time before possibly removing data from
    ## stoppages.
    #self.elapsed_time = datetime.timedelta(
    #    seconds=self.data[time_src].iloc[-1].item())
    ##self.elapsed_time = self.data.index.get_level_values(
    ##    'offset')[-1].to_pytimedelta()

    # Calculated when needed and memoized here.
    # TODO: Move to accessors. Harmless here for now.
    self._moving_time = None
    self._elapsed_time = None
    self._norm_power = None

    #if self.has_position:
    
    # Assuming that missing lat-lon values happen exclusively at the
    # beginning and end of the file: extend the first non-null value
    # backward to the start of the DataFrame, and extend the last 
    # non-null value forward to the end of the DataFrame.
    # TODO: Test that has_position returns False at this point in the
    #       code, because the missing fields may not have been
    #       stripped yet. i.e. has_position returns true no matter if
    #       the file has latlons or not.
    self.data = self.data.lat.fillna(method='bfill')
    self.data = self.data.lat.fillna(method='ffill')
    self.data = self.data.lon.fillna(method='bfill')
    self.data = self.data.lon.fillna(method='ffill')

    # If speed is NaN, assume no movement.
    self.data = self.data.speed.fillna(0.)

    # if self.data.distance.has_data
    # if self.has_distance:

    # If distance is NaN, fill in with first non-NaN distance.
    # This assumes the dataframe has no trailing NaN distances.
    self.data = self.data.distance.fillna(method='bfill')

    self.data = self.data.displacement.fillna(0.)

    # If certain must-have fields are missing, calculate them from
    # other fields.

    # if self.has_speed and not self.has_distance:
    # if self.data.speed.has_data and not self.data.distance.has_data:
    #   self.data = self.data.distance.speed_calc(add_col=True)

    # if self.has_distance and not self.has_speed:
    #   self.data = self.data.speed.from_dist()

    # Calculate speed and distance directly from the coordinates,
    # and add them as columns in the DataFrame.
    # TODO: Do I want to add columns to the dataframe? Or do I want
    #       to calculate these things at runtime? For now, I say calc
    #       at runtime, until I really dig into the performance side,
    #       because that's when I'll make decisions about processing
    #       speed/time.

    #self.data = self.data.distance.from_latlon() # could calc both

    # Detect start/stop events based on stopped threshold speed.
    # TODO: Only run this if we have already added speeds to DF!
    if self.data.speed.has_data:
      pass
      #tmp
      #self.data = self.data.moving.detect(add_col=True)

    # Assume all null cadence data corresponds to no movement.
    self.data = self.data.cadence.fillna(0)

    # Infer null heart rate values by backfilling. The underlying
    # assumption is that null heart rate values will be at the beginning
    # of the file, but it will also backfill the odd missing value
    # within the file so long as it isn't at the end.
    self.data = self.data.hr.fillna(method='bfill')
 
    #if not self.has_elevation:
    if not self.data.elevation.has_data:
      self.data = self.data.elevation.flatten_series(add_col=True)
      self._default_sources['elevation'] = 'flat'

    # # Add an elevation series that is flat, at the average elevation
    # # of the Activity.
    # # 
    # # TODO: Remove from default init behavior?
    # self.data = self.data.elevation.flatten_series(add_col=True)

  def _validate(self, df):
    # TODO: Have accessors take over the validation whenever possible,
    #       and just run the validation in here or something. Or not at
    #       all. Why cleanup here, then cleanup there? I could just
    #       clean up the dataframe in Activity's init. Wonder why I
    #       chose to check everything up front. Will evolve, I'm sure.

    # Check if input DataFrame (row) index is correctly formatted.
    # TODO: Get this check into the accessor class? Why here? Speed?
    if not isinstance(df.index, pandas.Int64Index):
      raise(
          TypeError(
              'DataFrame index should be some form of pd.Int64Index, not %s.'
              % type(df.index).__name__
          )
      )
    #df.index.name = 'record'

    # Check DataFrame column structure.
    # TODO: Hand these checks off to the accessors, if possible.
    #       Is it possible to check once per DF, rather than once
    #       per accessor use?? (Consider in performance check).
    #       Consider the order of things, though. Is it possible
    #       to signal that the accessor's data has been cleaned?
    if isinstance(df.columns, pandas.MultiIndex):
      # Check that the column MultiIndex is correctly formatted.
      if df.columns.nlevels != 2:
        raise(HnsException(
            'Input DataFrame column MultiIndex may have no more than'  \
            ' 2 levels.'
        ))

      # TODO: Be able to infer which level is source and which is field.
      # if 'field' not in df.columns.names:
      #   raise(HnsException(
      #       'Input DataFrame MultiIndex missing "field" level.'))
      # if 'source' not in df.columns.names:
      #   raise(HnsException(
      #       'Input DataFrame MultiIndex missing "source" level.'))

  def _cleanup(self, df):
    """Ensure expected format and naming for row and col indices.

    TODO: Perhaps this should be called "pre-cleanup", because I would
          like the accessors to take over the majority of that duty.
    """
    # row index name
    df.index.name = 'record'

    # col index format
    if not isinstance(df.columns, pandas.MultiIndex):
      # Convert from Index to MultiIndex.
      df.columns = pandas.MultiIndex.from_tuples([
          (field_name, 'device') for field_name in df.columns
      ])

    # col index level names
    df.columns.set_names(['field', 'source'])

    return df

  def _cleanup_again(self, df):
    """Everything that happens after data has been cleanupd.

    This is the real cleanup method, the other one just gets the data
    READY to be cleaned!
    """
    for accessor_nm in df._accessors:
      # Be aware, we are working with a fresh DF in each loop.
      accessor = getattr(df, accessor_nm)
      df = accessor._cleanup()

    return df

  def _detect_stopped_periods(self, speed_source=None):
    """Detects periods of inactivity by comparing speed to a threshold value.

    Adds a boolean column to the self.data DataFrame corresponding
    to whether the user was moving or not.
    # TODO: Move this to the SpeedAccessor
    """
    # (A demo of how I expect it to work)
    # Add a column to the DataFrame corresponding to whether the user
    # was moving at each time step.
    self.data = self.data.moving.detect(speed=speed_source, add_col=True)

  def set_elevation_source(self, col, src_name):
    """Adds an alternate elevation column to the DataFrame.

    A MultiIndex distinguishes between columns containing fields 
    calculated using different elevation sources.

    Args:
      col: array of elevation values.
      name: a string to be used as the value of the 'source' index.

    Examples:
      >>> act.set_elevation_source([1600.0, 1601.0, 1602.0], 'google')

    TODO: Move this to the elevation accessor.
    TODO: Make this more general, as a way to add a series of any type.
    """
    elevation_column_name = self._elevation_column_name
    if isinstance(col, (pandas.Series, list, np.ndarray)):
      level = col
    elif hasattr(col, 'ndim') and col.ndim != 1:
      raise ValueError('Must pass array with one dimension only.')

    # Check that we are using a listlike of elevations
    level = _ensure_elevation(level)
    self.data[elevation_column_name, src_name] = level

    # TODO: Consider raising an error if the elevation source exists.
    self.data['elevation', name] = elev_list
    self.data['elevation', name].fillna(method='bfill', inplace=True)

  @property
  def source_data(self):
    """Returns a DataFrame consisting of data from the original source.

    The full DataFrame may have data from other sources. This property
    takes the full MultiIndexed DataFrame and distills it to a
    single-Indexed DataFrame.

    TODO: Make this able to return data from any source_name.
    """
    return self.data.xs(self._source_name, level='source', axis=1)

  @property
  def moving_time(self):
    if self._moving_time is None:
      self._moving_time = self.data.time.moving()

    return self._moving_time

  @property
  def elapsed_time(self):
    if self._elapsed_time is None:
      self._elapsed_time = self.data.time.elapsed()

    return self._elapsed_time

  def has_source(self, field_name, source_name):
    # TODO: Make sure this has been moved to accessors, then delete.
    # TODO: Consider generalizing to (field, source) tuples.
    #       and if so, change the name to something sensible.
    #return source_name in self.data.columns.get_level_values('source')
    return (field_name, source_name) in self.data.columns

  # example of old 'has_{field}' implementation.
  @property
  def has_elevation(self):
    # TODO: (Leave here for now) Evaluate if this is even needed.
    #       I think it makes sense to move it to the ElevationAccessor
    #       and keep it, but I also honestly cannot remember where this
    #       is used.
    
    #return 'elevation' in self.data.columns
    return self.data.elevation.has_data

  @property
  def has_distance(self):
    return ('distance', self._src_name) in self.data.columns

  def get_time_series(self, field=None, source=None, remove_stops=None):
    """Returns a pandas.Series of the corresponding DataFrame column.

    TODO: Move this to accessors...maybe? Do not know how it would look.
    """
    if source is None:
      source = self._src_name

    if not self.has_source(field, source):
      # TODO: Consider adding a hnserror class and raising it.
      return None

    # TODO: Add check/error for non-bool remove_stops value.
    if remove_stops is None:
      remove_stops = self._remove_stops

    # TODO: Add check/error for non-existent field name.
    # TODO: I guess I should have a backup case if there's no gps data.
    if remove_stops:
      return self.data[self.data['moving', 'gps']][field, source]

    return self.data[field, source]

  def cadence_series(self, remove_stops=None):
    if not self.has_cadence:
      return None

    return self.get_time_series('cadence', remove_stops=remove_stops)

  def heart_rate_series(self, remove_stops=None):
    if not self.has_heart_rate:
      return None

    return self.get_time_series('heart_rate', remove_stops=remove_stops)

  def speed_series(self, source=None, remove_stops=None):
    return self.get_time_series('speed', source, remove_stops=remove_stops)

  def displacement_series(self, source=None, remove_stops=None):
    return self.get_time_series('displacement', source,
                                remove_stops=remove_stops)

  def distance_series(self, source=None, remove_stops=None):
    if source is None:
      source = self._src_name

    #TODO: Consider alternate implementation, where we return distance
    #      or distance_calc columns if stops don't need to be removed.
    displacements = self.displacement_series(source=source,
                                             remove_stops=remove_stops)

    if displacements is None:
      return None

    return displacements.cumsum().rename(('distance', source))

  def elevation_series(self, source=None, remove_stops=None):
    # TODO: Ensure all functionality is brought over to accessor,
    #       then delete this (and related tests, references to it, ...)
    if source is None:
      source = self._default_elev_source

    return self.get_time_series('elevation', source,
                                remove_stops=remove_stops)


  # COMBINE WITH O2_POWER ACCESSOR?
  def _o2_power_tend_series(self, distance_source=None, elev_source=None):
    # TODO: Make this return an indexed, named pd.Series.
    speeds = self.speed_series(distance_source, remove_stops=False)
    grades = self.grade_series(distance_source, elev_source,
                               remove_stops=False)

    if speeds is None or grades is None:
      return None

    # Get the distance and elevation source names from the Series.
    distance_src = grades.name[1]
    elev_src = grades.name[2]

    return pu.o2_power_tendency(speeds, grades).rename(
               ('o2_power_tend', distance_src, elev_src))

  # THIS REPRESENTS A WHOLE ACCESSOR!!!
  def o2_power_series(self, distance_source=None, elev_source=None):
    #if elev_source is None:
    #  elev_source = self._default_elev_source

    #if distance_source is None:
    #  distance_source = self._src_name

    #if not self.has_source('elevation', elev_source):
    #  return None

    #if ('o2_power', source_name) not in self.data.columns:
    p = self._o2_power_tend_series(distance_source=distance_source,
                                   elev_source=elev_source)

    if p is None:
      return None

    #p.index = p.index.droplevel(level='block')

    #power_array = heartandsole.util.moving_average(p, 30)
    power_series = heartandsole.util.ewma(p, 20)

    #self.data['o2_power', source_name] = power_array

    # Get the distance and elevation source names from the Series.
    distance_src = p.name[1]
    elev_src = p.name[2]

    return power_series.rename(('o2_power', distance_src, elev_src))

  # BECOMES A SPEED METHOD
  def equiv_speed_series(self, distance_source=None, elev_source=None):
    """Calculates the flat-ground pace that would produce equal power.

    Takes moving average power, and inverts the pace-power equation to
    calculate equivalent pace.

    Rigorously speaking, the reported speeds are the flat-ground paces
    which, if run at steady-state for long enough, would elicit the
    same oxygen consumption as the instantaneous calculated oxygen
    consumption on a hill.

    TODO: Decide on missing-elevation-handling. Return smoothed pace,
          or return None?

    If elevation values aren't included in the file, the power values
    are simply a function of speed, and then are smoothed with a 
    moving average. In that case, equivalent paces shouldn't be too far
    off from actual paces.
    """
    equiv_speeds = pu.flat_speed(
        self.o2_power_series(distance_source=distance_source,
                             elev_source=elev_source))

    (_, distance_src, elev_src) = equiv_speeds.name

    return equiv_speeds.rename(('equiv_speed', distance_src, elev_src))

    #if source_name is None:
    #  source_name = self._default_source_name

    #if trust_device:
    #  if not (self.has_speed and self.has_source(source_name)):
    #    return None

    #  return pu.flat_speed(
    #      self.o2_power_series(source_name=source_name,
    #                           trust_device=trust_device)).rename(('equiv_speed',
    #                                                               source_name))
    #else:
    #  if not (self.has_position and self.has_source(source_name)):
    #    return None

    #  return pu.flat_speed(
    #      self.o2_power_series(source_name=source_name,
    #                           trust_device=trust_device)).rename(('equiv_speed_calc', source_name))

  def mean_cadence(self, remove_stops=None):
    if not self.has_cadence:
      return None

    return self.cadence_series(remove_stops=remove_stops).mean()

  def mean_heart_rate(self, remove_stops=None):
    if not self.has_heart_rate:
      return None

    return self.heart_rate_series(remove_stops=remove_stops).mean()

  def mean_speed(self, source=None, remove_stops=None):
    """Calculates distance traveled over time.

    There are two choices for how to calculate average speed: 
    - Divide total distance traveled (as reported by the GPS device)
      by the time it took to travel that distance.
    - Obtain total distance by numerically integrating the speed stream
      with respect to time, then divide this slightly different distance
      by the workout time.
    The first approach is applied here. The two approaches do not
    yield the same result because the smoothing algorithms employed by
    GPS devices smooth speed and distance streams differently. The
    distance stream is NOT simply the numerical integral of speed with
    respect to time, and the speed stream is NOT the numerical
    derivative of distance with respect to time.
    """
    distance = self.distance(source=source, remove_stops=remove_stops)

    if remove_stops is None:
      remove_stops = self._remove_stops

    if remove_stops:
      return distance / self.moving_time.total_seconds()
   
    return distance / self.elapsed_time.total_seconds()

    #time = self.time(remove_stops=remove_stops).total_seconds()

    #if self._remove_stopped_periods:
    #  return self.total_distance / self.moving_time.total_seconds()

    #return self.total_distance / self.elapsed_time.total_seconds()

  def distance(self, source=None, remove_stops=None):
    displacements = self.displacement_series(source=source,
                                             remove_stops=remove_stops)

    if displacements is None:
      return None

    return displacements.sum()

  def mean_equiv_speed(self, distance_source=None, elev_source=None):
    equiv_speeds = self.equiv_speed_series(distance_source=distance_source,
                                           elev_source=elev_source)

    if equiv_speeds is None:
      return None

    # Assumes each speed value was maintained for 1 second.
    return equiv_speeds.sum() / self.elapsed_time.total_seconds()

  def mean_power(self, distance_source=None, elev_source=None):
    powers = self.o2_power_series(distance_source=distance_source,
                                  elev_source=elev_source)

    if powers is None:
      return None

    return powers.mean()

  def norm_power(self, distance_source=None, elev_source=None):
    """Calculates the normalized power for the activity.

    See (Coggan, 2003) cited in README for details on the rationale behind the
    calculation.

    Normalized power is based on a 30-second moving average of power. Coggan's
    algorithm specifies that the moving average should start at the 30 second
    point in the data, but this implementation does not (it starts with the
    first value, like a standard moving average). This is an acceptable
    approximation because normalized power shouldn't be relied upon for efforts
    less than 20 minutes long (Coggan, 2012), so how the first 30 seconds are
    handled doesn't make much difference. Also, the values computed by this
    implementation are very similar to those computed by TrainingPeaks, so
    changing the moving average implementation doesn't seem to be critical.

    This function also does not specially handle gaps in the data. When a pause
    is present in the data (either from autopause on the recording device or
    removal of stopped periods in post-processing) the timestamp may jump by a
    large amount from one sample to the next. Ideally this should be handled in
    some way that takes into account the physiological impact of that rest, but
    currently this algorithm does not. But again, the values computed by this
    implementation are very similar to those computed by TrainingPeaks, so
    changing gap handling doesn't seem to be critical.

    Args:
      power_series: A pandas.Series of the run power values to average,
                    indexed with timestamps. Typical units are Watts/kg.

    Returns:
      Normalized power as a float.
    """
    powers = self.o2_power_series(distance_source=distance_source,
                                  elev_source=elev_source)

    if powers is None:
      return None

    return su.lactate_norm(powers)

  def power_intensity(self, threshold_power, distance_source=None,
                      elev_source=None):
    """Calculates the intensity factor of the activity.

    One definition of an activity's intensity factor is the ratio of
    normalized power to threshold power (sometimes called FTP). 
    See (Coggan, 2016) cited in README for more details.

    Args:
      threshold_power: Threshold power in Watts/kg.

    Returns:
      Intensity factor as a float.
    """
    np = self.norm_power(distance_source=distance_source, elev_source=elev_source)

    if np is None:
      return None

    return np / float(threshold_power)

  def power_training_stress(self, threshold_power, distance_source=None,
                            elev_source=None):
    """Calculates the power-based training stress of the activity.

    This is essentially a power-based version of Banister's 
    heart rate-based TRIMP (training impulse). Normalized power is 
    used instead of average power because normalized power properly 
    emphasizes high-intensity work. This and other training stress
    values are scaled so that a 60-minute effort at threshold intensity
    yields a training stress of 100. 

    Args:
      threshold_power: Threshold power in Watts/kg.

    Returns:
      Power-based training stress as a float.
    """
    intensity_factor = self.power_intensity(threshold_power,
                                            distance_source=distance_source,
                                            elev_source=elev_source)

    if intensity_factor is None:
      return None

    return su.training_stress(intensity_factor, self.moving_time.total_seconds())

  def heart_rate_intensity(self, threshold_heart_rate):
    """Calculates the heart rate-based intensity factor of the activity.

    One definition of an activity's intensity factor is the ratio of
    average heart rate to threshold heart rate. This heart rate-based
    intensity is similar to TrainingPeaks hrTSS value. This calculation
    uses lactate-normalized heart rate, rather than average heart rate.
    This intensity factor should agree with the power-based intensity
    factor, because heart rate behaves similarly to a 30-second moving
    average of power, this heart rate intensity factor should agree with
    the power-based intensity factor. Both calculations involve a
    4-norm of power (or of a proxy in this case).

    Args:
      threshold_heart_rate: Threshold heart rate in bpm.

    Returns:
      Heart rate-based intensity factor as a float.
    """
    if not self.has_heart_rate:
      return None

    return su.lactate_norm(self.heart_rate_series()) / threshold_heart_rate

  def heart_rate_training_stress(self, threshold_heart_rate):
    """Calculates the heart rate-based training stress of the activity.

    Should yield a value in line with power_training_stress. See the
    documentation for hr_intensity and power_training_stress. 

    Args:
      threshold_heart_rate: Threshold heart rate in bpm.

    Returns:
      Heart rate-based training stress as a float.
    """
    if not self.has_heart_rate:
      return None

    return su.training_stress(self.heart_rate_intensity(threshold_heart_rate),
                              self.moving_time.total_seconds())
