from io import BytesIO
from typing import List
from zipfile import ZipFile

from ..cfdi import CFDI


class MissingData(ValueError):
    pass


class CFDIParser:
    @classmethod
    def _get_files(cls, zipfile: ZipFile) -> List[str]:
        files = [zipfile.read(name).decode() for name in zipfile.namelist()]
        return files

    @classmethod
    def from_binary(cls, binary: bytes) -> List[CFDI]:
        zipfile = ZipFile(BytesIO(binary))
        cfdis = cls.parse_zip(zipfile)
        return cfdis

    @classmethod
    def parse_zip(cls, zipfile: ZipFile) -> List[CFDI]:
        raise NotImplementedError
