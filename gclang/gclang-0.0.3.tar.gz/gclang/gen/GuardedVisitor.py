# Generated from Guarded.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GuardedParser import GuardedParser
else:
    from GuardedParser import GuardedParser

# This class defines a complete generic visitor for a parse tree produced by GuardedParser.

class GuardedVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GuardedParser#Impl.
    def visitImpl(self, ctx:GuardedParser.ImplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Or.
    def visitOr(self, ctx:GuardedParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#MulDiv.
    def visitMulDiv(self, ctx:GuardedParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#AddSub.
    def visitAddSub(self, ctx:GuardedParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#UnarySub.
    def visitUnarySub(self, ctx:GuardedParser.UnarySubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#True.
    def visitTrue(self, ctx:GuardedParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArrayLowerBound.
    def visitExprArrayLowerBound(self, ctx:GuardedParser.ExprArrayLowerBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#False.
    def visitFalse(self, ctx:GuardedParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ArrayLiteral.
    def visitArrayLiteral(self, ctx:GuardedParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArrayElement.
    def visitExprArrayElement(self, ctx:GuardedParser.ExprArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Identifier.
    def visitIdentifier(self, ctx:GuardedParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Brackets.
    def visitBrackets(self, ctx:GuardedParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Number.
    def visitNumber(self, ctx:GuardedParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArrayUpperElement.
    def visitExprArrayUpperElement(self, ctx:GuardedParser.ExprArrayUpperElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#And.
    def visitAnd(self, ctx:GuardedParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Equiv.
    def visitEquiv(self, ctx:GuardedParser.EquivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprMacroCall.
    def visitExprMacroCall(self, ctx:GuardedParser.ExprMacroCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArrayUpperBound.
    def visitExprArrayUpperBound(self, ctx:GuardedParser.ExprArrayUpperBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArrayLowerElement.
    def visitExprArrayLowerElement(self, ctx:GuardedParser.ExprArrayLowerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Negate.
    def visitNegate(self, ctx:GuardedParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#Logic.
    def visitLogic(self, ctx:GuardedParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ExprArraySize.
    def visitExprArraySize(self, ctx:GuardedParser.ExprArraySizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#start.
    def visitStart(self, ctx:GuardedParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#operatorList.
    def visitOperatorList(self, ctx:GuardedParser.OperatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#operator.
    def visitOperator(self, ctx:GuardedParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#skipOperator.
    def visitSkipOperator(self, ctx:GuardedParser.SkipOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#abortOperator.
    def visitAbortOperator(self, ctx:GuardedParser.AbortOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#printOperator.
    def visitPrintOperator(self, ctx:GuardedParser.PrintOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#assignOperator.
    def visitAssignOperator(self, ctx:GuardedParser.AssignOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#commandList.
    def visitCommandList(self, ctx:GuardedParser.CommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#command.
    def visitCommand(self, ctx:GuardedParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#ifOperator.
    def visitIfOperator(self, ctx:GuardedParser.IfOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#doOperator.
    def visitDoOperator(self, ctx:GuardedParser.DoOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#condition.
    def visitCondition(self, ctx:GuardedParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#macroCall.
    def visitMacroCall(self, ctx:GuardedParser.MacroCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#macroOperatorDefinition.
    def visitMacroOperatorDefinition(self, ctx:GuardedParser.MacroOperatorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#macroExpressionDefinition.
    def visitMacroExpressionDefinition(self, ctx:GuardedParser.MacroExpressionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#formalParameters.
    def visitFormalParameters(self, ctx:GuardedParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#actualParameters.
    def visitActualParameters(self, ctx:GuardedParser.ActualParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#initialAssignments.
    def visitInitialAssignments(self, ctx:GuardedParser.InitialAssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayLowerBound.
    def visitArrayLowerBound(self, ctx:GuardedParser.ArrayLowerBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayUpperBound.
    def visitArrayUpperBound(self, ctx:GuardedParser.ArrayUpperBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arraySize.
    def visitArraySize(self, ctx:GuardedParser.ArraySizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayElement.
    def visitArrayElement(self, ctx:GuardedParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayLowerElement.
    def visitArrayLowerElement(self, ctx:GuardedParser.ArrayLowerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayUpperElement.
    def visitArrayUpperElement(self, ctx:GuardedParser.ArrayUpperElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayShift.
    def visitArrayShift(self, ctx:GuardedParser.ArrayShiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayPushUp.
    def visitArrayPushUp(self, ctx:GuardedParser.ArrayPushUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayPushDown.
    def visitArrayPushDown(self, ctx:GuardedParser.ArrayPushDownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayDelUp.
    def visitArrayDelUp(self, ctx:GuardedParser.ArrayDelUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayDelDown.
    def visitArrayDelDown(self, ctx:GuardedParser.ArrayDelDownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayPopUp.
    def visitArrayPopUp(self, ctx:GuardedParser.ArrayPopUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arrayPopDown.
    def visitArrayPopDown(self, ctx:GuardedParser.ArrayPopDownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arraySwap.
    def visitArraySwap(self, ctx:GuardedParser.ArraySwapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuardedParser#arraySet.
    def visitArraySet(self, ctx:GuardedParser.ArraySetContext):
        return self.visitChildren(ctx)



del GuardedParser