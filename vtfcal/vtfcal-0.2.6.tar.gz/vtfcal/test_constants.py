from pathlib import Path

import numpy as np

# TODO Move all of this to utils

TEST_DATA_SIZE = (1024, 1024)
TEST_PIXEL0 = (125, 50)

## This will just return the unrotated test pixel
## TODO TEST_PIXEL should be a dict that uses the actual per-channel rotation values
rot = 0
c = np.cos(np.deg2rad(rot))
s = np.sin(np.deg2rad(rot))
rm = np.array([[c, -s, 0], [s, c, 0]])
array_centre = np.array(TEST_DATA_SIZE) / 2.0
displacement = np.dot(rm[:2, :2], array_centre) - array_centre
rm[:2, 2] = -displacement
# TEST_PIXEL = np.dot(np.array(TEST_PIXEL0), rmatrix).astype(int)
TEST_PIXEL = (
    int((rm[0, 0] * TEST_PIXEL0[0]) + (rm[0, 1] * TEST_PIXEL0[1]) + rm[0, 2]),
    int((rm[1, 0] * TEST_PIXEL0[0]) + (rm[1, 1] * TEST_PIXEL0[1]) + rm[1, 2]),
)

TEST_WL_IDX = 10
RADIUS = 32
