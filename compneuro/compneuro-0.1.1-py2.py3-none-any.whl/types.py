"""Comp Neuro Type Definitions

Defines custom type definitions to help with documentation and sphinx resolution
"""

import typing as tp
import scipy

solvers = tp.Union["Euler", "scipy.integrate.odeint", str, scipy.integrate.OdeSolver]
