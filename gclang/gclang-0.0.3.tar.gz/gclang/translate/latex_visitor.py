from functools import reduce
import sympy as sp
from ..gen.GuardedVisitor import GuardedVisitor
from ..gen.GuardedParser import GuardedParser


def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


class LatexVisitor(GuardedVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.latex = ""

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        pass

    def visitStart(self, ctx: GuardedParser.StartContext):
        self.latex += r'''
\begin{verbatim}
'''
        self.latex += self.visitOperatorList(
            ctx.getChild(0, GuardedParser.OperatorListContext))

        self.latex += r'''
\end{verbatim}
'''
        return self.latex

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        return ctx.getText()

    def visitTrue(self, ctx: GuardedParser.NumberContext):
        return "True"

    def visitFalse(self, ctx: GuardedParser.NumberContext):
        return "False"

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        return ctx.getText()

    def visitAddSub(self, ctx: GuardedParser.AddSubContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return {
            ctx.ADD(): lambda x, y: f'({left} + {right})',
            ctx.SUB(): lambda x, y: f'({left} - {right})',
        }[ctx.getChild(1)](left, right)

    def visitMulDiv(self, ctx: GuardedParser.MulDivContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return {
            ctx.MUL(): lambda x, y: f'({left} * {right})',
            ctx.DIV(): lambda x, y: f'({left} / {right})',
        }[ctx.getChild(1)](left, right)

    def visitAssignOperator(self, ctx: GuardedParser.AssignOperatorContext):
        var_names = map(str, ctx.getTokens(GuardedParser.ID))
        var_values = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return f"{', '.join(var_names)} := {', '.join(var_values)}"

    def visitOperatorList(self, ctx: GuardedParser.OperatorListContext):
        return ';\n'.join([self.visit(operator) for operator in ctx.getTypedRuleContexts(GuardedParser.OperatorContext)])

    def visitIfOperator(self, ctx: GuardedParser.IfOperatorContext):
        command_list_ctx = ctx.getChild(0, GuardedParser.CommandListContext)

        fuses = []
        bodies = []
        for command in command_list_ctx.getTypedRuleContexts(GuardedParser.CommandContext):
            fuses.append(self.visit(command.getChild(0, GuardedParser.ExpressionContext)))
            bodies.append(self.visit(command.getChild(0, GuardedParser.OperatorListContext)))

        summary = f'''
if {fuses[0]} -> {bodies[0]}'''
        for i, b in enumerate(bodies[1:]):
            summary += f'\n|  {fuses[i]} -> {bodies[i]}'
        summary += f'\nfi'
        return summary
    
    def visitLogic(self, ctx: GuardedParser.LogicContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.LT(): lambda x, y: f'{x} < {y}',
            ctx.LE(): lambda x, y: f'{x} <= {y}',
            ctx.GT(): lambda x, y: f'{x} > {y}',
            ctx.GE(): lambda x, y: f'{x} >= {y}',
            ctx.EQ(): lambda x, y: f'{x} = {y}',
            ctx.NEQ(): lambda x, y: f'{x} != {y}',
        }[ctx.getChild(1)](left, right)

    def visitDoOperator(self, ctx: GuardedParser.IfOperatorContext):
        command_list_ctx = ctx.getChild(0, GuardedParser.CommandListContext)

        fuses = []
        bodies = []
        for command in command_list_ctx.getTypedRuleContexts(GuardedParser.CommandContext):
            fuses.append(self.visit(command.getChild(0, GuardedParser.ExpressionContext)))
            bodies.append(self.visit(command.getChild(0, GuardedParser.OperatorListContext)))

        summary = f'\ndo {fuses[0]} -> {bodies[0]}'
        for i, b in enumerate(bodies[1:]):
            summary += f'\n|  {fuses[i]} -> {bodies[i]}'
        summary += f'\nod'
        return summary