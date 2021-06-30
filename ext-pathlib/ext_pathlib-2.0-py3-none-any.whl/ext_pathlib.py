import itertools
import os
import os.path
import pathlib
import re
import shutil
from fnmatch import fnmatch
from os import PathLike, makedirs
from pathlib import PurePath
from typing import Generator, Union


class Path(type(pathlib.Path())):
    """Added Functions:\ncopy, copy2, move, move2, mkdirs, b, kb, mb, iglob, riglob, scan, scanr, write, readlines, str_is_file, exists, splitext, getatime, getmctime, getctime"""

    _self_type = type(pathlib.Path())

    def copy(self, target: Union[str, PathLike, PurePath]) -> None:
        """Copy file whilst making any necessary directories in target destination."""
        assert self.is_file()
        target = Path(target)
        makedirs(target.parent, exist_ok=True)
        shutil.copy(str(self), str(target))

    def copy2(self, target: Union[str, PathLike, PurePath]) -> None:
        """Copy file whilst making any necessary directories in target destination, appending '_2' (or increasing integer) to end of file name to prevent colision."""
        assert self.is_file()
        target = Path(target)
        makedirs(target.parent, exist_ok=True)
        target = self.move_helper(dst=target)
        shutil.copy(str(self), str(target))

    def move(self, dst: Union[str, PathLike, PurePath]) -> None:
        """Move file whilst making any necessary directories in target destination."""
        target = Path(dst)
        makedirs(target.parent, exist_ok=True)
        shutil.move(str(self), str(target))

        shutil.move(str(self), str(target))
        
    def move2(self, dst: Union[str, PathLike, PurePath]) -> None:
        """Move file whilst making any necessary directories in target destination, appending '_2' (or increasing integer) to end of file name to prevent colision."""
        target = Path(dst)
        makedirs(target.parent, exist_ok=True)
        target = self.move_helper(dst=target)
        shutil.move(str(self), str(target))

    def move_helper(self, dst: Union[str, PathLike, PurePath]) -> _self_type:
        """Get target destination for file, appending '_2' (or increasing integer) to end of file name to prevent colision."""
        mv_count = 2
        target = Path(dst)
        makedirs(target.parent, exist_ok=True)
        while target.exists():
            target = Path(
                re.sub("(_\d+)?(\..*?)$", f"_{mv_count}\\2", str(target), re.I)
            )
            mv_count += 1
        return target

    def mkdirs(self) -> None:
        """Make directories, with no errors on a directory existing."""
        makedirs(self, exist_ok=True)

    def b(self) -> int:
        """Return size of file in bytes"""
        assert self.is_file()
        return self.stat().st_size

    def kb(self) -> int:
        """Return size of file in kilobytes, rounded down."""
        assert self.is_file()
        return self.stat().st_size // 1024

    def mb(self) -> int:
        """Return size of file in megabytes, rounded down."""
        assert self.is_file()
        return round(self.stat().st_size / 1024 / 1024, 2)

    def iglob(self, search: Union[str, tuple]) -> Generator[None, None, _self_type]:
        """
        Search through directory matching one or more designations.
        (See Python fnmatch doc for more info on how to format search terms).
        """
        assert self.is_dir()

        if isinstance(search, str):
            return self.glob(search)
        if isinstance(search, tuple):
            output = itertools.chain()
            for x in search:
                output = itertools.chain(output, self.glob(x))
            return (x for x in output)

    def rglob(self, search: Union[str, tuple]) -> Generator[None, None, _self_type]:
        """
        Recursive search through directory matching one or more designations.
        (See Python fnmatch doc for more info on how to format search terms).
        """
        assert self.is_dir()

        if isinstance(search, str):
            return self.rglob(search)
        if isinstance(search, tuple):
            output = itertools.chain()
            for x in search:
                output = itertools.chain(output, self.rglob(x))
            return (x for x in output)

    def scan(self, wildcards: Union[str, tuple] = "*") -> Generator[None, None, _self_type]:
        """
        Search through directory matching one or more designations. Uses os.scandir to search for a speed increase, whilst returning Pathlib objects.
        (See Python fnmatch doc for more info on how to format search terms).
        """
        path = self.resolve()
        if path == ".":
            path = os.getcwd()
        if isinstance(wildcards, str):
            return (
                Path(x.path) for x in os.scandir(path) if fnmatch(x.path, wildcards)
            )
        if isinstance(wildcards, tuple):
            output = itertools.chain()
            for w in wildcards:
                output = itertools.chain(
                    output, [x for x in os.scandir(path) if fnmatch(x.path, w)]
                )
            return (Path(x.path) for x in output)

    def scanr(self, wildcards: Union[str, tuple] = "*") -> Generator[None, None, _self_type]:
        """
        Recursive search through directory matching one or more designations. Uses os.scandir to search for a speed increase, whilst returning Pathlib objects.
        (See Python fnmatch doc for more info on how to format search terms).
        """
        path = self.resolve()
        if path == ".":
            path = os.getcwd()
        if isinstance(wildcards, str):
            lst_out = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    lst_out.append(Path(os.path.join(root, file)))
            return (x for x in lst_out if fnmatch(x, wildcards))
        if isinstance(wildcards, tuple):
            output = itertools.chain()
            for w in wildcards:
                lst_out = []
                for root, dirs, files in os.walk(path):
                    for file in files:
                        lst_out.append(Path(os.path.join(root, file)))
                lst_out = [x for x in lst_out if fnmatch(x, w)]
                output = itertools.chain(output, lst_out)
            return (x for x in output)

    def write(self, data, mode: str = "w", encoding: str = None) -> None:
        """Open file and write data to it."""
        with self.open(mode, encoding=encoding) as fwrite:
            fwrite.write(data)

    def readlines(self, encoding: str = None) -> list[str]:
        """Open file and return the readlines."""
        with self.open("r", encoding=encoding) as fread:
            return fread.readlines()

    def str_is_file(self) -> bool:
        """Attempt to tell if a string (to a file that does not exist) is a file or not. Not very reliable, but sometimes helpful."""
        ext = os.path.splitext(str(self))[1]
        if self.is_dir():
            return False
        elif ext:
            return True
        else:
            return False

    def exists(self) -> bool:
        """Return bool of whether or not the file exists."""
        return os.path.exists(self)

    def splitext(self) -> tuple[str]:
        """Split filename from extension, returns a tuple."""
        return os.path.splitext(self)

    def getatime(self) -> float:
        """Get accessed time for file in float."""
        return os.path.getatime(self)

    def getmtime(self) -> float:
        """Get modified time for file in float."""
        return os.path.getmtime(self)

    def getctime(self) -> float:
        """Get created time for file in float."""
        return os.path.getctime(self)

    def mkdir(
        self, mode: Union[int, str] = 0o777, parents: bool = True, exist_ok: bool = True
    ) -> None:
        """Make directory command, with helpful default options. See pathlib.mkdir for further info on options."""
        self.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
