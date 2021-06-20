"""
portableQDA facilitates round-trip information exchange using the REFI-QDA standard: codebooks (QDC files) and QDPX projects. This portable information can be used by any Qualitative Data Analysis (CAQDAS) Software conforming to that XML-based standard, as per https://www.qdasoftware.org"


Import/Export formats [QDC and QDPX](https://www.qdasoftware.org/wp-content/uploads/2019/09/REFI-QDA-1-5.pdf) are:   

- suitable for structured archiving of any kind of files, including:
  + personal corpus of information analysis (text coding, cites, comments)
  + the source documents themselves (any arbitrary format, including office docs, PDF, html, audio, surverys)
- well-defined and maintained by the [REF-QDA working group](http://qdasoftware.org)
- supported and developed by a growing number of participants

QDA stands for Qualitative Data Analysis, as known in social sciences. Related Wikipedia article states: “Qualitative research relies on data obtained by the researcher by first-hand observation, interviews, recordings, […]. The data are generally non-numerical. Qualitative methods include ethnography, grounded theory, discourse analysis […]. These methods have been used in sociology, anthropology, and educational research.”


Copyright 2021 Leandro Batlle

portableQDA is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = '0.4.0'

from typing import NamedTuple, Any

class resultCls(NamedTuple):
    """
    named tuple including:
        - result.error: level of error (if no error 0/False, otherwise an integer grather than 0)
        - result.Desc: error description
        - result.result: a pointer to the new element
    """
    error: int
    errorDesc: str
    result: Any

from portableqda.refi_qda import *
