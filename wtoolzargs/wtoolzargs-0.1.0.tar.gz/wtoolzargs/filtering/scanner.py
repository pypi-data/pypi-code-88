from wtoolzargs.common import exceptions
from wtoolzargs.common import token_
from wtoolzargs.filtering import tokentype

ScanError = exceptions.ScanError
TT = tokentype.TokenType
Token = token_.Token


class Scanner(object):
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

        self.keywords = {
            "eq": TT.EQUAL,
            "ne": TT.NOT_EQUAL,
            "gt": TT.GREATER_THAN,
            "ge": TT.GREATER_THAN_OR_EQUAL,
            "lt": TT.LESS_THAN,
            "le": TT.LESS_THAN_OR_EQUAL,
            "and": TT.AND,
            "or": TT.OR,
            "not": TT.NOT,
            "like": TT.LIKE,
        }

    def scan(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TT.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == "(":
            self.add_token(TT.LEFT_PAREN)
        elif c == ")":
            self.add_token(TT.RIGHT_PAREN)
        elif c == " ":
            pass
        elif c == "\r":
            pass
        elif c == "\t":
            pass
        elif c == "\n":
            self.line = self.line + 1
        elif c == "T":
            self.boolean_true()
        elif c == "F":
            self.boolean_false()
        elif c == "'":
            self.string()
        elif self.is_digit(c):
            self.number()
        elif self.is_alpha(c):
            self.identifier()
        else:
            raise ScanError("Unexpected character '{}'.".format(c))

    def boolean_true(self):
        if (
            self.peek_next_at(0) == "r"
            and self.peek_next_at(1) == "u"
            and self.peek_next_at(2) == "e"
        ):
            for e in range(3):
                self.advance()
            self.add_token(TT.BOOL, "1")

    def boolean_false(self):
        if (
            self.peek_next_at(0) == "a"
            and self.peek_next_at(1) == "l"
            and self.peek_next_at(2) == "s"
            and self.peek_next_at(3) == "e"
        ):
            for e in range(4):
                self.advance()
            self.add_token(TT.BOOL, "0")

    def string(self):
        while self.peek() != "'" and not self.is_at_end():
            if self.peek() == "\n":
                self.line = self.line + 1
            self.advance()

        if self.is_at_end():
            raise ScanError("Unterminated string.")

        self.advance()

        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TT.STRING, value)

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        value = self.source[self.start : self.current]

        self.add_token(TT.NUMBER, float(value))

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        value = self.source[self.start : self.current]
        type_ = self.keywords.get(value, TT.IDENTIFIER)
        self.add_token(type_)

    def is_alpha(self, c):
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == "_"

    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)

    def is_digit(self, c):
        return c >= "0" and c <= "9"

    def peek(self):
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def peek_next_at(self, at):
        if self.current + at >= len(self.source):
            return "\0"
        return self.source[self.current + at]

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current = self.current + 1
        return self.source[self.current - 1]

    def add_token(self, type_, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type_, text, literal, self.line))
