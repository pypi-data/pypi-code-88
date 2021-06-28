from covimath.models import seir
import pytest

def test_peak():
    N = 1000
    E0 = 1
    I0 = 1
    R0 = 0

    model = seir.SEIR(N=N, beta=1.38, sigma = 0.19, gamma=0.34, 
                       E0=E0, I0=I0, R0=R0, tau=150)
    
    model.solve()
    
    p = model.peak()[1]
    
    assert pytest.approx(141, 1) == p
    
def test_method_seq():
    with pytest.raises(ValueError):
        N = 1000
        E0 = 1
        I0 = 1
        R0 = 0
        model = seir.SEIR(N=N, beta=1.38, sigma = 0.19, gamma=0.34, 
                           E0=E0, I0=I0, R0=R0, tau=150)
        model.plot()