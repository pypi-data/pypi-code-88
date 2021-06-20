from ..gen.GuardedVisitor import GuardedVisitor
from ..gen.GuardedParser import GuardedParser


class PythonVisitor(GuardedVisitor):
    def __init__(self):
        self.python = ''  # lines of python code
        self.indent = 0
        self._stack = []

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        return ctx.getText()

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        return ctx.getText()

    def visitTrue(self, ctx: GuardedParser.TrueContext):
        return 'True'

    def visitFalse(self, ctx: GuardedParser.FalseContext):
        return 'False'

    def visitUnarySub(self, ctx: GuardedParser.UnarySubContext):
        return '-' + self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitNegate(self, ctx: GuardedParser.NegateContext):
        return 'not' + self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitAnd(self, ctx: GuardedParser.AndContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return f'{left} and {right}'

    def visitOr(self, ctx: GuardedParser.OrContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return f'{left} or {right}'

    def visitImpl(self, ctx: GuardedParser.ImplContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return f'not {left} or {right}'

    def visitEquiv(self, ctx: GuardedParser.EquivContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return f'{left} == {right}'

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

        return '\n'.join([f'{k} = {v}' for k, v in zip(var_names, var_values)])

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

    # def visitIfOperator(self, ctx: GuardedParser.IfOperatorContext):
    #     command_list_ctx = ctx.getChild(0, GuardedParser.CommandListContext)

    #     fuses = []
    #     bodies = []
    #     for command in command_list_ctx.getTypedRuleContexts(GuardedParser.CommandContext):
    #         fuses.append(self.visit(command.getChild(0, GuardedParser.ExpressionContext)))

    #         self.indent += 2
    #         bodies.append(self.visit(command.getChild(0, GuardedParser.OperatorListContext)))
    #         self.indent -= 2
        
    #     result = f'if {fuses[0]}:\n' + ' ' * (self.indent + 2) + bodies[0]

    #     for i, b in enumerate(bodies[1:-1]):
    #         summary += f'\n elif {fuses[i]}:' + ' ' * (self.indent + 2) + bodies[i]}'
    #     summary += f'\nfi'
    #     return summary

    def visitDoOperator(self, ctx: GuardedParser.DoOperatorContext):
        ...

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        self._stack.append(f'assert {self._stack.pop()}')

    def visitStart(self, ctx: GuardedParser.StartContext):
        self.visitChildren(ctx)
        print('\n'.join(self.lines))
