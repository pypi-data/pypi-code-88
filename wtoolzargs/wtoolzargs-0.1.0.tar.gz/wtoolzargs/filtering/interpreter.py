from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy import or_

from wtoolzargs.common import exceptions
from wtoolzargs.common import expressions
from wtoolzargs.filtering import tokentype

# FIXME: Review types casting?

TT = tokentype.TokenType
InterpretError = exceptions.InterpretError


class Interpreter(expressions.Visitor):
    def __init__(self, model, expression):
        self.model = model
        self.expression = expression

    def interpret(self):
        return self.evaluate(self.expression)

    def visit_binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.type == TT.EQUAL:
            field = self.field(left)
            return field == right
        elif expr.operator.type == TT.NOT_EQUAL:
            field = self.field(left)
            return field != right
        elif expr.operator.type == TT.GREATER_THAN:
            field = self.field(left)
            return field > right
        elif expr.operator.type == TT.GREATER_THAN_OR_EQUAL:
            field = self.field(left)
            return field >= right
        elif expr.operator.type == TT.LESS_THAN:
            field = self.field(left)
            return field < right
        elif expr.operator.type == TT.LESS_THAN_OR_EQUAL:
            field = self.field(left)
            return field <= right
        elif expr.operator.type == TT.LIKE:
            # NOTE: Can you find out what wrong here? :-)
            field = self.field(left)
            return field.like(str(right))

        elif expr.operator.type == TT.AND:
            return and_(left, right)
        elif expr.operator.type == TT.OR:
            return or_(left, right)
        return None

    def visit_grouping_expr(self, expr):
        return self.evaluate(expr.expression)

    def visit_literal_expr(self, expr):
        return expr.value

    def visit_identifier_expr(self, expr):
        return expr.value

    def visit_unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.type == TT.NOT:
            return not_(right)
        return None

    def evaluate(self, expr):
        return expr.accept(self)

    def field(self, a):
        model = self.model
        if not hasattr(model, a):
            raise InterpretError("No such field '{}' on model.".format(a))
        return getattr(model, a)
