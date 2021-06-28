from covimath.paramest import sirparams
import numpy as np
import pytest

def test_beta():
    ni = np.array([5, 7, 11, 20, 30, 45, 75, 115, 155, 
                   220, 315, 540, 720, 950])
    _beta = sirparams.findbeta(ni)
    
    pytest.approx(0.4, 0.01) == _beta

