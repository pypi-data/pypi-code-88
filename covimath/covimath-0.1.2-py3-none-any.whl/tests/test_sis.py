from math import floor, ceil
from covimath.models import sis

def test_inf():
    model = sis.SIS(N=1000, lam=0.05, mu = 0.15, 
                gamma=1./10, I0=1, tau=150)
    i = model.i(20) # should be around 1.8%
    assert ceil(i * 100) == 2.0

def test_sus():
    model = sis.SIS(N=1000, lam=0.05, mu = 0.15, 
                gamma=1./10, I0=1, tau=150)
    s = model.s(20) # should be around 98%
    assert floor(s * 100) == 98