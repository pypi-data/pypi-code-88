# Copyright 2021 Oskar Sharipov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

from pydantic import BaseModel


class AirplaneBase(BaseModel):
    session: str
    id: int
    name: str
    phone: str
    username: typing.Optional[str]


class AirplaneCreate(AirplaneBase):
    pass


class Airplane(AirplaneBase):
    class Config:
        orm_mode = True
