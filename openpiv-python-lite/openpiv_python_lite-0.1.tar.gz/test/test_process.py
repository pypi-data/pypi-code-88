from openpiv_python_lite import extended_search_area_piv as piv, get_coordinates, random_noise

# %%
import numpy as np

frame_a = np.zeros((32, 32))
frame_a = random_noise(frame_a)
frame_b = np.roll(np.roll(frame_a, 3, axis=1), 2, axis=0)
threshold = 0.1

def test_piv_32():
    """ test of the simplest PIV run 32 x 32 """
    u, v = piv(frame_a, frame_b, window_size=32)
    assert(np.abs(u-3) < threshold)
    assert(np.abs(v+2) < threshold)


def test_piv_16_32():
    """ test of the search area larger than the window """
    u, v = piv(frame_a, frame_b, window_size=16, search_area_size=32)
    assert(np.abs(u[0,0]-3) < threshold)
    assert(np.abs(v[0,0]+2) < threshold)