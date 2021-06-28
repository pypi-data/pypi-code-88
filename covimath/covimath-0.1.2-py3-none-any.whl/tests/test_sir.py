from covimath.models import sir
import pytest

def test_peak():
    N = 2000
    I0 = 1
    R0 = 0

    model = sir.SIR(N=N, beta=0.2, gamma=0.1, I0=I0, R0=R0, tau=150)
    
    model.solve()
    
    p = model.peak()[1]
    
    assert pytest.approx(307, 1) == p
    
def test_method_seq1():
    with pytest.raises(ValueError):
        N = 2000
        I0 = 1
        R0 = 0
        model = sir.SIR(N=N, beta=0.2, gamma=0.1, I0=I0, R0=R0, tau=150)
        model.peak()
    
def test_method_seq2():
    with pytest.raises(ValueError):
        N = 2000
        I0 = 1
        R0 = 0
        model = sir.SIR(N=N, beta=0.2, gamma=0.1, I0=I0, R0=R0, tau=150)
        model.plot()