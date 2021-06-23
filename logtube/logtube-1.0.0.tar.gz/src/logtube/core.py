from typing import Optional

from .event import Event
from .event import NONAME
from .output import Output, ConsoleOutput, FileOutput


class Core(Output):
    project: str
    env: str
    console_output: Optional[ConsoleOutput]
    file_output: Optional[FileOutput]

    """
    Core 维护着日志系统的输出器（包括命令行输出器和文件输出器），保持全局配置
    """

    def __init__(self, opts: Optional[dict]):
        self.project = NONAME
        self.env = NONAME
        self.console_output = None
        self.file_output = None

        if opts is None:
            return

        if "project" in opts:
            self.project = str(opts["project"])
        if "env" in opts:
            self.env = str(opts["env"])
        if "console" in opts:
            self.console_output = ConsoleOutput(opts["console"])
        if "file" in opts:
            self.file_output = FileOutput(opts["file"])

    def append_event(self, event: Event) -> None:
        if self.console_output is not None:
            self.console_output.append_event(event)
        if self.file_output is not None:
            self.file_output.append_event(event)

    def create_event(self) -> Event:
        e = Event()
        e.project = self.project
        e.env = self.env
        e.output = self
        return e


class CoreProvider(object):
    """
    CoreProvider 封装一层 Core 为 Logger 切换 Core 成为可能
    """
    core: Core

    def get_core(self) -> Core:
        return self.core
