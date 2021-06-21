from wtoolzargs.common import token_
from wtoolzargs.common import exceptions
from wtoolzargs.common import expressions
from wtoolzargs.ordering import tokentype

# NOTE: Grammar
#
# expression           -> orderings ;
# orderings            -> order ("," order )* ;
# order                -> identifier ("asc" | "desc")? ;
# identifier           -> IDENTIFIER ;
#
# here are some productions
#
# a asc
# a desc
# a desc, b desc


TT = tokentype.TokenType
ParseError = exceptions.ParseError
Token = token_.Token


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        res = self.expression()
        # REVIEW: How to handle this case more idiomatic.
        if not self.is_at_end():
            raise self.error(self.peek(), "Expect expression.")
        return res

    def expression(self):
        return self.orderings()

    def orderings(self):
        res = self.order()
        while self.match(TT.SEPERATOR):
            operator = self.previous()
            right = self.order()
            res = expressions.Binary(res, operator, right)
        return res

    def order(self):
        res = self.identifier()
        if self.match(TT.ASC, TT.DESC):
            operator = self.previous()
            return expressions.Unary(operator, res)

        return expressions.Unary(
            Token(type_=TT.ASC, lexeme="asc", literal=None, line=1), res
        )

    def identifier(self):
        if self.match(TT.IDENTIFIER):
            return expressions.Identifier(self.previous().lexeme)

        raise self.error(self.peek(), "Expect expression.")

    def match(self, *types):
        for e in types:
            if self.check(e):
                self.advance()
                return True
        return False

    def check(self, type_):
        if self.is_at_end():
            return False
        return self.peek().type == type_

    def advance(self):
        if not self.is_at_end():
            self.current = self.current + 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == TT.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, token, message):
        return ParseError("Error at '{}': {}".format(token.lexeme, message))
