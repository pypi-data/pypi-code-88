import time
from pathlib import Path

from . import byte_translate, icon_manager, url
from .icon import Icon


class File:
    def __init__(self, path: Path):
        if path.suffix == 'url':
            self.path = path.stem
            self.is_url = True
            self.url = url.get_url_from_path(path)
        else:
            self.path = path
            self.is_url = False

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
        if self.is_url:
            size = 0
        elif self.is_dir:
            size = sum(f.stat().st_size for f in self.path.rglob('*') if f.is_file())
        else:
            size = self.path.stat().st_size

        return byte_translate.translate(size)

    @property
    def modified(self):
        if self.is_url:
            return '-'

        return time.ctime(self.path.stat().st_mtime)

    def __replace_filename(self, template: str, key: str) -> str:
        if self.is_url:
            return template.replace(key, self.url)
        else:
            return template.replace(key, self.filename)

    def to_html(self, template: str) -> str:
        return self.__replace_filename(template, '#FILENAME') \
            .replace('#ICON', self.icon.relative_path.as_posix()) \
            .replace('#SIZE', self.size) \
            .replace('#MODIFIED', self.modified)
