"""Equations for run power and cost based on physiological studies."""

import math


def cost_of_inclined_treadmill_running(grade):
  """Calculates the cost of inclined running according to Minetti.

  This is how much metabolic energy it costs (J) to move a unit 
  body mass (kg) a unit distance (m) along a treadmill belt surface
  at a steady-state (after running on this treadmill for 4 minutes).
  This metabolic energy cost is estimated based on the amount of
  oxygen you are consuming, and assumes a specific type of fuel is
  being used (mostly carbohydrate, with a dash of fat, and no protein).
  This gives an estimate of 20.9 kJ of energy per liter of oxygen
  consumed.

  For more info, see `heartandsole_local/heartandsole/powerutils.py`,
  specifically the documentation for `o2_power_tendency`.

  Args:
    grade (float): Decimal grade, i.e. 20% = 0.20.

  Returns:
    float: Cost of running, in Joules/kg/m according to Minetti curve.
  """
  # Clip the grade value so we don't use the curve outside its limits
  # of applicability. 
  # TODO: Find a better way to handle the shittiness of the Minetti
  # curve. Maybe find a way to extrapolate for steeper grades based
  # on an assumed efficiency of lifting/lowering...0.25??
  grade = max(-0.45, min(grade, 0.45))

  # Calculate metabolic cost of running (neglecting air resistance),
  # in Joules per meter traveled per kg of body weight, as a function of
  # decimal grade (on a treadmill, technically). From (Minetti, 2002).
  # Valid for grades shallower than 45% (0.45 in decimal form).
  c_i = 155.4 * grade ** 5 - 30.4 * grade ** 4 - 43.3 * grade ** 3  \
    + 46.3 * grade ** 2 + 19.5 * grade + 3.6

  return c_i


def cost_of_wind_running(speed):
  """Calculate metabolic cost of running against wind resistance.
  
  Assumes zero wind speed. From (Pugh, 1971) & (Di Prampero, 1993).
  eta_aero is the efficiency of conversion of metabolic energy into
  mechanical energy when working against a headwind. 

  k is the air friction coefficient, in J s^2 m^-3 kg^-1,
  which makes inherent assumptions about the local air density
  and the runner's projected area and body weight.

  Args:
    speed (float): Running speed in meters per second.

  Returns:
    float: Aerodynamic cost of running, in Joules per meter traveled
    per kg of body weight, as a function
    
  TODO: 
    * Revisit whether 0.5 is an appropriate efficiency value...
      I recall it might have something to do with the speed at which
      the work is being done.
  """
  eta_aero = 0.5
  k = 0.01
  c_aero = k * speed ** 2 / eta_aero

  return c_aero


def run_cost(speed, grade=0.0):
  """Calculates the metabolic cost of running.

  See the documentation for powerutils.o2_power_ss for information
  on the scientific basis for this calculation.

  Args:
    speed (float): Running speed in meters per second. 
    grade (float): Decimal grade, i.e. 45% = 0.45.

  Returns:
    float: Cost of running on an incline in still air, in Joules/kg/m,
      with distance measured along the incline slope.
  """
  # grade = grade or 0.0

  # Use that Minetti curve.
  c_i = cost_of_inclined_treadmill_running(grade)

  # Pugh and Di Prampero tell us the cost of resisting wind.
  c_aero = cost_of_wind_running(speed)

  return c_i + c_aero


def run_power(speed, grade=0.0):
  return run_cost(speed, grade=grade) * speed / math.cos(math.atan(grade))