import re

class Token:
    """Terminal nodes in the AST. These are returned by the lexer when parse_next_token is called."""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"'{self}'"


class RegularExpression:
    """When pattern matching, provide an instance of this to perform regular expression pattern matching."""
    def __init__(self, re):
        self.pattern = re


class Lexer:
    """Divide a string up into tokens based on a list of lexemes and whitespace."""
    def __init__(self, lexemes, string, whitespace=[" ", "\t", "\n", "\r"], ignore_whitespace=True):
        self.cursor = 0
        self.lexemes = []
        self.string_lexemes = []
        self.re_lexemes = []
        self.set_lexemes(lexemes)
        self.whitespace = whitespace
        self.ignore_whitespace = ignore_whitespace
        self.string = string

    def set_whitespace(self, whitespace, ignore_whitespace=True):
        self.whitespace = whitespace
        self.ignore_whitespace = ignore_whitespace

    def set_lexemes(self, lexemes):
        self.lexemes = lexemes
        self.string_lexemes = []
        self.re_lexemes = []
        for lexeme in lexemes:
            if isinstance(lexeme, str):
                self.string_lexemes.append(lexeme)
            elif isinstance(lexeme, RegularExpression):
                self.re_lexemes.append(lexeme)

    def lookahead(self, lookahead=1):
        cursor_buffer = self.cursor
        tokens = []
        for i in range(lookahead):
            t = self.parse_next_token()
            if t is not None:
                tokens.append(t)
        self.cursor = cursor_buffer
        return tokens

    def parse_next_token(self):
        while self.cursor < len(self.string):
            t = self.string[self.cursor]
            if t in self.string_lexemes:
                current = Token(t)
                #FIXME deal with tokens with length greater than 1 by using "startswith"
                self.cursor += 1
                return current
            elif self.matches_re_lexeme():
                t = self.matches_re_lexeme()
                self.cursor += len(t)
                return t
            elif t in self.whitespace: #ignore non-lexeme whitespace
                self.cursor += 1
                return t
            else:
                atom_str = self.atom(self.cursor)
                atom = Token(atom_str)
                self.cursor += len(atom_str)
                return atom

    def matches_re_lexeme(self):
        for re_lexeme in self.re_lexemes:
            match = re.match(re_lexeme.pattern, self.string[self.cursor:])
            if match:
                token_len = match.regs[0][1]
                return self.string[self.cursor:self.cursor+token_len]
        return False


    def atom(self, i):
        #XXX this can cause an infinite loop if it returns an empty string
        j = i
        while j < len(self.string):
            current = self.string[j]
            #if current.isalnum():
            if not current.isspace() and current not in self.lexemes:
                j += 1
            else:
                return self.string[i:j]
            if j == len(self.string):
                return self.string[i:j]