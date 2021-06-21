'''The *dboard* package implements the software representation of a Dassym's electronic board.

:author: F. Voillat
:copyright: ® 2021  Dassym SA

This program is free software: you can redistribute it and/or modify
it under the terms of the **GNU General Public License** as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You can consult the GNU General Public License on http://www.gnu.org/licenses/gpl-3.0.html.
'''
from .common import DBoardPreferedDapiMode, DBoardException, BaseBoardItem, SystemModeConfig, LastReset
from .base import  BaseDBoard
from .factory import DBoardFactory