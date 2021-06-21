class Token(object):
    def __init__(self, type_, lexeme, literal, line):
        self.type = type_
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return "Token(type_={}, lexeme={}, literal={}, line={})".format(
            self.type, self.lexeme, self.literal, self.line
        )

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.lexeme == other.lexeme
            and self.literal == other.literal
        )
