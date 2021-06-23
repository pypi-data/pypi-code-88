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


from argparse import ArgumentParser, Namespace

from line_bot_tool.core.generator import GeneratorUtil

__description__ = "Useful tool for line bot"
__copyright__ = "Copyright 2021 nanato12"
__version__ = "1.0-b"
__license__ = "Apache License 2.0"
__author__ = "nanato12"
__author_email__ = "admin@nanato12.info"
__url__ = "https://github.com/nanato12/line-bot-tool"


class CommandLineUtil:
    """コマンドラインからの情報を管理するクラス"""

    args: Namespace

    def __init__(self) -> None:
        parser = ArgumentParser()
        parser.add_argument("gen", help="コマンドや関数を生成する時に使用する引数", nargs=2)
        self.args = parser.parse_args()

    def execute(self) -> None:
        if self.args.gen:
            gutil = GeneratorUtil(*self.args.gen)
            gutil.execute()


def exec_from_command_line() -> None:
    """コマンドラインから情報を受け取る関数"""
    util = CommandLineUtil()
    util.execute()
