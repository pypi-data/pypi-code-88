from pathlib import Path
from typing import TYPE_CHECKING, Iterable

from docs_translate.exceptions import ObjectNotFoundException, DocsFileNotFoundError, FileCreateError

if TYPE_CHECKING:
    from docs_translate.settings import Settings


class FilesWorker:
    suffixes = ['.md', '.rst']

    def __init__(self, settings: 'Settings') -> None:
        self.settings = settings
        self.object_to_process: Path = self.settings.path
        self.__validate_folder()

    def __validate_folder(self) -> None:
        if not self.object_to_process.exists():
            raise ObjectNotFoundException(self.object_to_process)

    def get_files(self) -> Iterable[Path]:
        files_list: list = []
        for _suffix in self.suffixes:
            if self.object_to_process.is_dir():
                files_list.extend(self.object_to_process.glob('**/*'+_suffix))
            elif self.object_to_process.suffix == _suffix:
                files_list.append(self.object_to_process)
            else:
                pass
        if len(files_list) == 0:
            raise DocsFileNotFoundError(self.object_to_process)

        return files_list

    def create_file(self, src: Path) -> Path:
        sub_path = src.parts[len(self.object_to_process.parts):-1]
        target_dir = self.settings.target_dir / "\\".join(sub_path)

        try:
            if not target_dir.exists():
                target_dir.mkdir(exist_ok=True)
            target_file = target_dir / src.name
            if not target_file.exists():
                open(file=target_file, mode='x').close()
        except FileExistsError:
            pass
        except Exception:
            raise FileCreateError(target_dir)

        return target_file


