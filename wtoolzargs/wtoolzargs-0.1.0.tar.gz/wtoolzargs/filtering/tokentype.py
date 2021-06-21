import enum


class TokenType(enum.Enum):
    LEFT_PAREN = enum.auto()
    RIGHT_PAREN = enum.auto()
    EOF = enum.auto()

    EQUAL = enum.auto()
    NOT_EQUAL = enum.auto()
    GREATER_THAN = enum.auto()
    GREATER_THAN_OR_EQUAL = enum.auto()
    LESS_THAN = enum.auto()
    LESS_THAN_OR_EQUAL = enum.auto()

    AND = enum.auto()
    OR = enum.auto()
    NOT = enum.auto()

    LIKE = enum.auto()

    IDENTIFIER = enum.auto()
    STRING = enum.auto()
    NUMBER = enum.auto()
    BOOL = enum.auto()
