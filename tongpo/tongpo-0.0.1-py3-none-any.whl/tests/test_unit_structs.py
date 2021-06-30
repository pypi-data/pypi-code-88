from tongpo.structs import LifoQueue
import pytest

@pytest.fixture
def lifo():
    q = LifoQueue(maxsize=5)
    q.put(1)
    q.put(2)
    return q

def test_1(lifo):
    assert lifo.get() == 2
    assert lifo.get() == 1

