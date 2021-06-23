"""
Copyright 2021 nanato12

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from abc import ABCMeta, abstractmethod
from ast import Constant, Expr


class BaseGenerator(metaclass=ABCMeta):
    ast_body: list

    def _ast_add_license(self) -> None:
        """append Expr to ast body"""

        with open("LICENSE") as license_file:
            self.ast_body.insert(
                0,
                Expr(value=Constant(value=f"\n{license_file.read()}")),
            )

    @abstractmethod
    def generate(self) -> None:
        """generate py file"""
