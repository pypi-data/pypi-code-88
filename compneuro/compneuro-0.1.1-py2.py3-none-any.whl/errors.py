"""Comp Neuro Exception Classes

.. note::

    All anticipated exceptions should raise custom Exceptions so that user
    can identify when an error is not anticipated and help with debugging.
"""


class CompNeuroError(Exception):
    """Base Comp Neuro Exceptions"""


class CompNeuroUtilsError(CompNeuroError):
    """Base Comp Neuro Utility Exceptions"""


class CompNeuroPlotError(CompNeuroUtilsError):
    """Comp Neuro Plotter Exceptions"""


class CompNeuroSignalError(CompNeuroUtilsError):
    """Comp Neuro Signal Exceptions"""


class CompNeuroModelError(CompNeuroError):
    """Comp Neuro Model Exceptions"""
