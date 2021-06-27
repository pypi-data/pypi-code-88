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


"""Provide an atomic element ORM model."""


from __future__ import annotations

from typing import Dict

from sqlalchemy import Column, ForeignKey, Integer, String

from .base import Base, Session
from .mixin import ModelMixin


class Element(ModelMixin, Base):
    """Define an atomic element ORM model."""

    __tablename__ = "elements"

    symbol: str = Column(String(2), nullable=False, unique=True, index=True)
    atomic_number: int = Column(Integer, nullable=False)

    def __repr__(self):
        """Return a string representation of this object."""
        return f"{self.symbol}({self.atomic_number})"

    @classmethod
    def symbol2element(cls, session: Session) -> Dict[str, Element]:
        return {elem.symbol: elem for elem in session.query(cls)}

    @classmethod
    def atomic_number2element(cls, session: Session) -> Dict[int, Element]:
        return {elem.atomic_number: elem for elem in session.query(cls)}

    @classmethod
    def symbol2atomic_number(cls, session: Session) -> Dict[str, int]:
        return {elem.symbol: elem.atomic_number for elem in session.query(cls)}

    @classmethod
    def atomic_number2symbol(cls, session: Session) -> Dict[int, str]:
        return {elem.atomic_number: elem.symbol for elem in session.query(cls)}


class MoleculeElementAssociation(Base):
    """Define the many-to-many association between molecules and elements."""

    __tablename__ = "molecule_element_associations"

    molecule_id: int = Column(Integer, ForeignKey("molecules.id"), primary_key=True)
    element_id: int = Column(Integer, ForeignKey("elements.id"), primary_key=True)
    quantity: int = Column(Integer, nullable=False)
