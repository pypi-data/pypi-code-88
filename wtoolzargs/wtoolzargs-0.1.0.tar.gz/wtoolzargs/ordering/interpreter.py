from wtoolzargs.common import exceptions
from wtoolzargs.common import expressions
from wtoolzargs.ordering import tokentype

TT = tokentype.TokenType
InterpretError = exceptions.InterpretError


class Interpreter(expressions.Visitor):
    def __init__(self, model, expression):
        self.model = model
        self.expression = expression

    def interpret(self):
        res = self.evaluate(self.expression)
        if not isinstance(res, list):
            return [res]
        return res

    def visit_binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        # HACK: Apply a better solution.
        if expr.operator.type == TT.SEPERATOR:
            if isinstance(left, list):
                left.append(right)
                return left
            if isinstance(right, list):
                right.append(left)
                return right
            return [left, right]

        return None

    def visit_grouping_expr(self, expr):
        pass

    def visit_literal_expr(self, expr):
        pass

    def visit_identifier_expr(self, expr):
        return expr.value

    def visit_unary_expr(self, expr):
        right = self.evaluate(expr.right)

        if expr.operator.type == TT.ASC:
            field = self.field(right)
            return getattr(field, "asc")()

        if expr.operator.type == TT.DESC:
            field = self.field(right)
            return getattr(field, "desc")()

        return None

    def evaluate(self, expr):
        return expr.accept(self)

    def field(self, a):
        model = self.model
        if not hasattr(model, a):
            raise InterpretError("No such field '{}' on model.".format(a))
        return getattr(model, a)
