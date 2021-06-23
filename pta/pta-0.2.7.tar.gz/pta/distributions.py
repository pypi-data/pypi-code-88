"""Descriptions of probability distributions.
"""

from copy import deepcopy
from typing import Any

from .commons import Q


class UniformDistribution:
    """Uniform distribution in a given interval.

    Parameters
    ----------
    lb : float, optional
        Lower bound of the interval, by default 0.0
    ub : float, optional
        Upper bound of the interval, by default 1.0
    """

    def __init__(self, lb: float = 0.0, ub: float = 1.0):
        self.lb = lb
        self.ub = ub

    @property
    def lb(self) -> float:
        """Gets the lower bound of the distribution."""
        return self._lb

    @lb.setter
    def lb(self, value: float):
        """Sets the lower bound of the distribution."""
        self._lb = value

    @property
    def ub(self) -> float:
        """Gets the upper bound of the distribution."""
        return self._ub

    @ub.setter
    def ub(self, value: float):
        """Sets the upper bound of the distribution."""
        self._ub = value

    def copy(self) -> "UniformDistribution":
        """Creates a copy of this object.

        Returns
        -------
        UniformDistribution
            Copy of this object.
        """
        return UniformDistribution(self.lb, self.ub)


class NormalDistribution:
    """Normal distribution with given mean and standard deviation.

    Parameters
    ----------
    mean : float, optional
        Mean of the distribution, by default 0.0
    std : float, optional
        Standard deviation, by default 1.0
    """

    def __init__(self, mean: float = 0.0, std: float = 1.0):
        self.mean = mean
        self.std = std

    @property
    def mean(self) -> float:
        """Gets the mean of the distribution."""
        return self._mean

    @mean.setter
    def mean(self, value: float):
        """Sets the mean of the distribution."""
        self._mean = value

    @property
    def std(self) -> float:
        """Gets the standard deviation of the distribution."""
        return self._std

    @std.setter
    def std(self, value: float):
        """Sets the standard deviation of the distribution."""
        self._std = value

    def copy(self):
        """Creates a copy of this object.

        Returns
        -------
        NormalDistribution
            Copy of this object.
        """
        return NormalDistribution(self.mean, self.std)


class LogUniformDistribution:
    """Log-uniform distribution in a given interval.

    Parameters
    ----------
    lb : float, optional
        Lower bound of the interval, by default 0.0
    ub : float, optional
        Upper bound of the interval, by default 1.0
    """

    def __init__(self, lb: float = 0.0, ub: float = 1.0):
        self.lb = lb
        self.ub = ub

    @property
    def lb(self) -> float:
        """Gets the lower bound of the distribution."""
        return self._lb

    @lb.setter
    def lb(self, value: float):
        """Sets the lower bound of the distribution."""
        self._lb = value

    @property
    def ub(self) -> float:
        """Gets the upper bound of the distribution."""
        return self._ub

    @ub.setter
    def ub(self, value: float):
        """Sets the upper bound of the distribution."""
        self._ub = value

    def copy(self):
        """Creates a copy of this object.

        Returns
        -------
        LogUniformDistribution
            Copy of this object.
        """
        return LogUniformDistribution(self.lb, self.ub)


class LogNormalDistribution:
    """Log-normal distribution with given mean and standard deviation.

    Parameters
    ----------
    log_mean : float, optional
        Natural logarithm of the mean of the distribution, by default 0.0
    log_std : float, optional
        Standard deviation of the distribution on the log scale, by default 1.0
    """

    def __init__(self, log_mean: float = 0.0, log_std: float = 1.0):
        self.log_mean = log_mean
        self.log_std = log_std

    @property
    def log_mean(self) -> float:
        """Gets the log-mean of the distribution."""
        return self._log_mean

    @log_mean.setter
    def log_mean(self, value: float):
        """Sets the log-mean of the distribution."""
        self._log_mean = value

    @property
    def log_std(self) -> float:
        """Gets the log-standard deviation of the distribution."""
        return self._log_std

    @log_std.setter
    def log_std(self, value: float):
        """Sets the log-standard deviation of the distribution."""
        self._log_std = value

    def copy(self):
        """Creates a copy of this object.

        Returns
        -------
        LogNormalDistribution
            Copy of this object.
        """
        return LogNormalDistribution(self.log_mean, self.log_std)


def distribution_from_string(parameters_string: str) -> Any:
    """Parses a distribution from a string. The format of the string is
    <distribution>|<data1>|<...>, where distribution is the type of the distribution and
    the remaining elements the arguments of the constructor of the distribution. For
    example, "Uniform|1.0|2.0".

    Parameters
    ----------
    parameters_string : str
        String describing the distribution.

    Returns
    -------
    Any
        The constructed distribution object.

    Raises
    ------
    Exception
        If the type of the distribution is not recognized.
    """
    parameters = parameters_string.split('|')
    if parameters[0] == 'Uniform':
        assert len(
            parameters) == 3, 'A uniform distribution requires two parameters'
        return UniformDistribution(float(parameters[1]), float(parameters[2]))
    elif parameters[0] == 'Normal':
        assert len(
            parameters) == 3, 'A normal distribution requires two parameters'
        return NormalDistribution(float(parameters[1]), float(parameters[2]))
    elif parameters[0] == 'LogUniform':
        assert len(parameters) == 3, \
            'A log-uniform distribution requires two parameters'
        return LogUniformDistribution(float(parameters[1]), float(parameters[2]))
    elif parameters[0] == 'LogNormal':
        assert len(parameters) == 3, \
            'A log-normal distribution requires two parameters'
        return LogNormalDistribution(float(parameters[1]), float(parameters[2]))
    else:
        raise Exception(f'Unsupported distribution: {parameters[0]}')


def distribution_to_string(distribution: Any) -> str:
    """Encodes a distribution in a string. The format of the string is
    <distribution>|<data1>|<...>, where distribution is the type of the distribution and
    the remaining elements the arguments of the constructor of the distribution. For
    example, "Uniform|1.0|2.0".

    Parameters
    ----------
    distribution : Any
        Distribution object to be converted.

    Returns
    -------
    str
        String describing the distribution.

    Raises
    ------
    Exception
        If the specified distribution is not supported by this method.
    """
    if isinstance(distribution, UniformDistribution):
        return f'Uniform|{distribution.lb}|{distribution.ub}'
    elif isinstance(distribution, NormalDistribution):
        return f'Normal|{distribution.mean}|{distribution.std}'
    elif isinstance(distribution, LogUniformDistribution):
        return f'LogUniform|{distribution.lb}|{distribution.ub}'
    elif isinstance(distribution, LogNormalDistribution):
        return f'LogNormal|{distribution.log_mean}|{distribution.log_std}'
    else:
        raise Exception(f'Unsupported distribution')
