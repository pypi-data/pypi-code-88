from wtoolzargs.filtering import tokentype
from wtoolzargs.common import expressions
from wtoolzargs.common import exceptions

# NOTE: Grammar
#
# bool only taken from
# https://cs.stackexchange.com/questions/10558/grammar-for-describing-boolean-expressions-with-and-or-and-not # noqa
# expression -> conditional_or
# conditional_or -> conditional_and ("or" conditional_and)*
# conditional_and -> primary ("and" primary)*
# primary -> id | not primay | "(" exression ")"
#
#
# the actual grammar
# expression           -> conditional_not ;
# conditional_not      -> "not" conditional_or | conditional_or ;
# conditional_or       -> conditional_and ( "or" conditional_and )* ;
# conditional_and      -> comparison ( "and" comparison )* ;
# comparison           -> identifier ( "ne" | "eq" | "gt" | "ge" | "lt" | "le" | "like" ) unary | "(" expression ")" ; # noqa
# unary                -> "not" unary | primary ;
# primary              -> NUMBER | STRING | BOOL; # FIXME: only strings
# identifier           -> IDENTIFIER ;
#
# here are some productions
#
# a eq 10
# a eq 'a'
# a eq 'a' and b eq 'b'
# a eq not 'a'
#
# (a eq 'a' or b eq 'b') and c eq 'c'
# not a eq not 'b'
# not a eq 'b'
# not (a eq 'a' and b eq 'b')
# a eq 'a' and b eq 'b' and (c eq 'c')

TT = tokentype.TokenType
ParseError = exceptions.ParseError


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
        return self.conditional_not()

    def conditional_not(self):
        if self.match(TT.NOT):
            operator = self.previous()
            right = self.conditional_or()
            return expressions.Unary(operator, right)
        return self.conditional_or()

    def conditional_or(self):
        res = self.conditional_and()
        while self.match(TT.OR):
            operator = self.previous()
            right = self.conditional_and()
            res = expressions.Binary(res, operator, right)
        return res

    def conditional_and(self):
        res = self.comparison()
        while self.match(TT.AND):
            operator = self.previous()
            right = self.comparison()
            res = expressions.Binary(res, operator, right)
        return res

    def comparison(self):
        if self.match(TT.LEFT_PAREN):
            e = self.expression()
            self.consume(TT.RIGHT_PAREN, "Expect ')' after expression.")
            return expressions.Grouping(e)

        res = self.identifier()
        if self.match(
            TT.NOT_EQUAL,
            TT.EQUAL,
            TT.GREATER_THAN,
            TT.GREATER_THAN_OR_EQUAL,
            TT.LESS_THAN,
            TT.LESS_THAN_OR_EQUAL,
            TT.LIKE,
        ):
            operator = self.previous()
            right = self.unary()
            return expressions.Binary(res, operator, right)

        raise self.error(self.previous(), "Expect expression.")

    def unary(self):
        if self.match(TT.NOT):
            operator = self.previous()
            right = self.unary()
            return expressions.Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TT.NUMBER, TT.STRING, TT.BOOL):
            return expressions.Literal(self.previous().literal)

        raise self.error(self.peek(), "Expect expression.")

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

    def consume(self, type_, message):
        if self.check(type_):
            return self.advance()
        raise self.error("{} {}".format(self.peek(), message))

    def error(self, token, message):
        return ParseError("Error at '{}': {}".format(token.lexeme, message))
