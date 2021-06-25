# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from typing import Any, Sequence

import numpy as nmpy
import skimage.measure as msre
from cell_tracking_BC.type.cell import cell_t


array_t = nmpy.ndarray


SKIMAGE_MORPHOLOGICAL_FEATURES: Sequence[str]  # Set below


def CellArea(cell: cell_t) -> int:
    """"""
    bb_map = cell.BBMap()
    output = nmpy.count_nonzero(bb_map)

    return output


def CellSKImageMorphologicalFeatures(cell: cell_t) -> Sequence[Any]:
    """"""
    output = []

    bb_map = cell.BBMap().astype(nmpy.int8)
    features = msre.regionprops(bb_map)[0]
    for name in SKIMAGE_MORPHOLOGICAL_FEATURES:
        output.append(features[name])

    return output


def AverageIntensityInCell(cell: cell_t, frame: array_t) -> float:
    """"""
    map_ = cell.Map(frame.shape)
    output = nmpy.mean(frame[map_]).item()

    return output


def _CellSKImageMorphologicalFeatureNames() -> Sequence[str]:
    """"""
    output = []

    dummy = nmpy.zeros((10, 10), dtype=nmpy.int8)
    dummy[4:7, 4:7] = 1
    features = msre.regionprops(dummy)[0]

    for name in dir(features):
        if (not name.startswith("_")) and hasattr(features, name):
            output.append(name)

    return output


SKIMAGE_MORPHOLOGICAL_FEATURES = _CellSKImageMorphologicalFeatureNames()
