#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/07/18"

import numpy as np


def is_diagonal(a: np.ndarray):
    b = np.zeros(a.shape)
    np.fill_diagonal(b, a.diagonal())
    return np.all([a == b])
