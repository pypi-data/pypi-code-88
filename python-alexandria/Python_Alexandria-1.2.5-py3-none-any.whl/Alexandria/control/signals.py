import numpy as np
from math import floor


class ControlSignals:

    def __init__(self, total, dt):
        """
        :param total: Total maneuver time
        :param dt: Time step
        """
        self.dt = dt
        self.total = total

    def t(self):
        """
        :return: Maneuver time vector
        """
        t = np.arange(0, self.total, self.dt)
        return t

    def seconds_to_n(self, t0, t1):
        """
        :param t0: Start time of action
        :param t1: End time of action
        :return: Vector size for action lasting from t0 to t1, calculated from previously
                 provided total maneuver time and time step
        """
        n = self.t().size*(t1-t0)/self.total
        return floor(n)

    def u_step(self, value, t0, t1):
        """
        :param value: Value of step control input
        :param t0: Start time of step control input
        :param t1: End time of step control input
        :return: Step control input vector for SSS force response calculation
        """
        control_input = value*np.ones(self.seconds_to_n(t0, t1))
        u = self.merge(control_input, t0, t1)
        return u

    def u_ramp(self, v0, v1, t0, t1):
        """
        :param v0: Initial value of linear control input
        :param v1: End value of linear control input
        :param t0: Start time of linear control input
        :param t1: End time of linear control input
        :return: Linear control input vector for SSS force response calculation
        """
        control_input = np.linspace(v0, v1, self.seconds_to_n(t0, t1))
        u = self.merge(control_input, t0, t1)
        return u

    def merge(self, control_input, t0, t1):
        """
        :param control_input: Control input to be merged
        :param t0: Control input start time
        :param t1: Control input end time
        :return: Control time vector: merged input and release time
        """

        if t0 == 0:
            control_release = np.zeros(self.seconds_to_n(t1, self.total))
            u = np.concatenate((control_input,
                                control_release))
        elif t0 > 0:
            control_hold = np.zeros(self.seconds_to_n(0, t0))
            control_release = np.zeros(self.seconds_to_n(t1, self.total))
            u = np.concatenate((control_hold,
                                control_input,
                                control_release))
        else:
            raise Exception(f"Invalid t0 ({t0})")
        return u
