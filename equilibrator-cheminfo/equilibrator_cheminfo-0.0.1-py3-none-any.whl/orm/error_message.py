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


"""Provide a model to store error messages of different severity levels."""


import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from .base import Base
from .mixin import ModelMixin


@enum.unique
class SeverityLevel(enum.Enum):
    """Define the severity level of a message."""

    WARNING = enum.auto()
    ERROR = enum.auto()
    CRITICAL = enum.auto()


class ErrorMessage(ModelMixin, Base):
    """Define a model to store error messages of different severity levels."""

    __tablename__ = "error_messages"

    molecule_id: int = Column(Integer, ForeignKey("molecules.id"))
    message: str = Column(String, nullable=False)
    level: str = Column(
        Enum(SeverityLevel), default=SeverityLevel.ERROR, nullable=False
    )

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return (
            f"{type(self).__name__}(molecule_id={self.molecule_id}, "
            f"level={self.level}, "
            f"message={self.message[:20] + ('...' if len(self.message) > 20 else '')})"
        )
