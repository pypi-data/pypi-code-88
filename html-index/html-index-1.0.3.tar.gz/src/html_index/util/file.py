import time
from pathlib import Path

from . import byte_translate, icon_manager
from .icon import Icon


class File:
    def __init__(self, path: Path):
        self.path = path

    def __str__(self):
        return self.path.__str__()

    @property
    def is_dir(self) -> bool:
        return self.path.is_dir()

    @property
    def extension(self) -> str:
        if self.is_dir:
            return '__folder'
        return self.path.suffix[1:]

    @property
    def filename(self) -> str:
        return self.path.name

    @property
    def icon(self) -> Icon:
        return icon_manager.lookup(self.extension)

    @property
    def size(self) -> str:
        if self.is_dir:
            size = sum(f.stat().st_size for f in self.path.rglob('*') if f.is_file())
        else:
            size = self.path.stat().st_size

        return byte_translate.translate(size)

    @property
    def modified(self):
        return time.ctime(self.path.stat().st_mtime)

    def to_html(self, template: str) -> str:
        return template.replace('#FILENAME', self.filename) \
            .replace('#ICON', self.icon.relative_path.as_posix()) \
            .replace('#SIZE', self.size) \
            .replace('#MODIFIED', self.modified)
