from xsdata.formats.dataclass.parsers import XmlParser
from faina_semenovna.blanks.smz_v0_28_schema import _smz_schema
from faina_semenovna.blanks import *
from io import StringIO


class FainaSemenovna:
    extract = XmlParser()
    __schema = _smz_schema

    @classmethod
    def schema(cls) -> str:
        return cls.__schema

    @classmethod
    def schema_file(cls):
        s = StringIO()
        s.write(cls.__schema)
        s.seek(0)
        return s
