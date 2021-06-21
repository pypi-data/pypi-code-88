from wtoolzargs.common import expressions
from wtoolzargs.common import utils


class AstPrinter(expressions.Visitor):
    def print(self, expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr):
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr):
        if isinstance(expr.value, str):
            return "'{}'".format(str(expr.value))
        return str(expr.value)

    def visit_identifier_expr(self, expr):
        return str(expr.value)

    def visit_unary_expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *args):
        builder = utils.StringBuilder()
        builder.append("(").append(name)

        for expr in args:
            builder.append(" ")
            builder.append(expr.accept(self))

        builder.append(")")

        return str(builder)
