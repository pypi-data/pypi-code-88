import enum


class TokenType(enum.Enum):
    EOF = enum.auto()

    ALSO = enum.auto()
    ASC = enum.auto()
    DESC = enum.auto()

    IDENTIFIER = enum.auto()
    SEPERATOR = enum.auto()
