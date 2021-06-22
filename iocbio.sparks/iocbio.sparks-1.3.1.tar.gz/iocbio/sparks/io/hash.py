# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  Authors: Martin Laasmaa and Marko Vendelin
#  This file is part of project: IOCBIO Sparks
#

import numpy as np
from tifffile.tifffile import TiffFile
import hashlib


def calcid(tiffile=None, fname=None):
    if tiffile is not None: return _hash_tiff(tiffile)
    return _hash_tiff(TiffFile(file_name))


# implementation
def _hash_tiff(tif):
    data = np.squeeze(tif.asarray())
    return hashlib.sha256(data.tostring()).hexdigest()
