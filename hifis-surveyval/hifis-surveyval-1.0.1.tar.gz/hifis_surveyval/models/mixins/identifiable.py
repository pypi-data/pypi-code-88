# hifis-surveyval
# Framework to help developing analysis scripts for the HIFIS Software survey.
#
# SPDX-FileCopyrightText: 2021 HIFIS Software <support@hifis.net>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""
This module contains the base class for all objects that carry a unique ID.

IDs are composed of multiple parts interjected by a hierarchy separator.
"""

from typing import Optional, Set


class Identifiable(object):
    """
    This is the abstract superclass for all objects that carry an ID.

    The ID is expected to be a string (or be convertible into such and to be
    unique among all identifiable objects.

    IDs are separated by a HIERARCHY_SEPARATOR and the part after the last
    separator forms the so-called "short ID".
    If no hierarchical parent_id is given, the short ID and the full ID are the
    same.
    """

    HIERARCHY_SEPARATOR: str = "/"
    known_ids: Set[str] = set()

    def __init__(self, object_id: str, parent_id: Optional[str] = None):
        """
        Create a new identifiable object with a given ID.

        The class will track all known IDs to prevent duplicates.
        A full ID is formed by merging the parent's full ID (if it exists)
        and the object's ID.

        Args:
            object_id:
                A string serving as an ID to the object.
                It must be neither None nor empty.
            parent_id:
                (Optional, Default=None) The full ID of another identifiable
                object that forms the hierarchical parent of this one. Used
                to generate the full ID.
        Raises:
            ValueError:
                Signals either a duplicate or invalid object_id
        """
        if not object_id:
            raise ValueError(
                "ID of an identifiable object may neither be empty nor None"
            )

        if object_id in Identifiable.known_ids:
            raise ValueError(f"Attempted to assign duplicate ID {object_id}")

        self._full_id: str = (
            f"{parent_id}{Identifiable.HIERARCHY_SEPARATOR}{object_id}"
            if parent_id
            else object_id
        )
        Identifiable.known_ids.add(self._full_id)

    def __del__(self) -> None:
        """
        Deconstruct an identifiable object.

        The used ID will be removed from the known IDs and can be re-used.
        """
        assert self._full_id in Identifiable.known_ids

        Identifiable.known_ids.remove(self._full_id)

    @property
    def short_id(self) -> str:
        """
        Get the short ID of this object (without parent_id IDs).

        Returns:
            The string identifying this object with respect to its siblings
        """
        return self._full_id.split(Identifiable.HIERARCHY_SEPARATOR)[-1]

    # TODO: Decide whether to cache the short id

    @property
    def full_id(self) -> str:
        """
        Get the full ID of the object (includes parent_id IDs).

        Returns:
            The string identifying the object with respect to any other
            Identifiable
        """
        return self._full_id

    def __str__(self) -> str:
        """Return the full ID as representation of this identifiable object."""
        return self.full_id
