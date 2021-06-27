# Copyright (c) 2021, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide helper functions for manipulating InChI and InChIKey strings."""


import re
from typing import Union

import pandas as pd


Column = Union[pd.Series, pd.Index]


# Match the proton sublayer until the next layer or until the end of the string.
proton_layer = re.compile(r"/p.*?(/|$)")


def drop_proton_layer(inchi: str) -> str:
    """Remove the proton layer from an InChI string."""
    assert inchi.startswith(
        "InChI=1"
    ), f"The given string '{inchi}' does not look like an InChI."
    return proton_layer.sub(repl=r"\g<1>", string=inchi, count=1)


def drop_column_proton_layer(inchi: Column) -> Column:
    """Remove the proton layer from every InChI in a pandas series or index."""
    return inchi.str.replace(pat=proton_layer, repl=r"\g<1>", n=1)


def drop_protonation(inchikey: str) -> str:
    """Remove any protonation from an InChIKey."""
    assert (
        len(inchikey) == 27
    ), f"The given string '{inchikey}' does not look like an InChIKey."
    return inchikey[:-1] + "N"


def drop_column_protonation(inchikey: Column) -> Column:
    """Remove any protonation from every InChIKey in a pandas series or index."""
    return inchikey.str[:-1] + "N"
