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


from line_bot_tool.core.generator.command_generator import CommandGenerator


class GeneratorUtil:
    __cmd: str
    __target: str

    def __init__(self, arg: str, target: str) -> None:
        if arg.count(":") != 1:
            self.invalid_argument_error(arg)

        _, self.__cmd = arg.split(":")
        self.__target = target

    def execute(self) -> None:
        if self.__cmd == "command":
            cmd_generator = CommandGenerator(self.__target)
            cmd_generator.generate()
        else:
            self.invalid_argument_error(self.__cmd)

    def invalid_argument_error(self, arg: str) -> None:
        raise Exception(
            f"[GeneratorUtil] invalid argument '{arg}'. Expect 'gen:command', 'gen:event'"
        )
