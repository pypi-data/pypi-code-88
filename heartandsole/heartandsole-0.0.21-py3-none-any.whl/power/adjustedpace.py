"""Grade-based pace adjustments as defined by Strava and TrainingPeaks."""

_docstring_param = """
Args:
  grade (float): decimal grade, ie 20% = 0.2
Returns:
  float: The factor to scale up or down the real speed based on grade.
    If greater than 1.0, the adjusted pace is faster than the real pace.
    
"""


def ngp_factor(grade):
  raise NotImplementedError


def gap_factor(grade):
  raise NotImplementedError


def ngp(speed, grade=0.0):
  return speed * ngp_factor(grade)


def gap(speed, grade=0.0):
  return speed * gap_factor(grade)