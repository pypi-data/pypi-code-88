from wtoolzargs.common import exceptions
from wtoolzargs.common import token_
from wtoolzargs.ordering import tokentype

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

        self.keywords = {"asc": TT.ASC, "desc": TT.DESC}

    def scan(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TT.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == ",":
            self.seperator()
        elif c == " ":
            pass
        elif c == "\r":
            pass
        elif c == "\t":
            pass
        elif c == "\n":
            self.line = self.line + 1
        elif self.is_alpha(c):
            self.identifier()
        else:
            raise ScanError("Unexpected character '{}'.".format(c))

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        value = self.source[self.start : self.current]
        type_ = self.keywords.get(value, TT.IDENTIFIER)
        self.add_token(type_)

    def seperator(self):
        self.add_token(TT.SEPERATOR)

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

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current = self.current + 1
        return self.source[self.current - 1]

    def add_token(self, type_, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type_, text, literal, self.line))
