from dataclasses import dataclass

from libbiomedit import metadata as _metadata

from .error import UserError

# Reexports
alnum_str = _metadata.alnum_str
METADATA_FILE = _metadata.METADATA_FILE
Purpose = _metadata.Purpose
HexStr1024 = _metadata.HexStr1024
HexStr256 = _metadata.HexStr256


@dataclass(frozen=True)
class MetaData(_metadata.MetaData):
    """Wrapper around libbiomedit.metadata.MetaData throwing UserError"""

    @classmethod
    def from_dict(cls, d: dict):
        try:
            return super().from_dict(d)
        except ValueError as e:
            raise UserError(format(e)) from e


load_metadata = MetaData.from_dict
