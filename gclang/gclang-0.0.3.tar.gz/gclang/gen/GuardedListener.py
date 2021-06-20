# Generated from Guarded.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GuardedParser import GuardedParser
else:
    from GuardedParser import GuardedParser

# This class defines a complete listener for a parse tree produced by GuardedParser.
class GuardedListener(ParseTreeListener):

    # Enter a parse tree produced by GuardedParser#Impl.
    def enterImpl(self, ctx:GuardedParser.ImplContext):
        pass

    # Exit a parse tree produced by GuardedParser#Impl.
    def exitImpl(self, ctx:GuardedParser.ImplContext):
        pass


    # Enter a parse tree produced by GuardedParser#Or.
    def enterOr(self, ctx:GuardedParser.OrContext):
        pass

    # Exit a parse tree produced by GuardedParser#Or.
    def exitOr(self, ctx:GuardedParser.OrContext):
        pass


    # Enter a parse tree produced by GuardedParser#MulDiv.
    def enterMulDiv(self, ctx:GuardedParser.MulDivContext):
        pass

    # Exit a parse tree produced by GuardedParser#MulDiv.
    def exitMulDiv(self, ctx:GuardedParser.MulDivContext):
        pass


    # Enter a parse tree produced by GuardedParser#AddSub.
    def enterAddSub(self, ctx:GuardedParser.AddSubContext):
        pass

    # Exit a parse tree produced by GuardedParser#AddSub.
    def exitAddSub(self, ctx:GuardedParser.AddSubContext):
        pass


    # Enter a parse tree produced by GuardedParser#UnarySub.
    def enterUnarySub(self, ctx:GuardedParser.UnarySubContext):
        pass

    # Exit a parse tree produced by GuardedParser#UnarySub.
    def exitUnarySub(self, ctx:GuardedParser.UnarySubContext):
        pass


    # Enter a parse tree produced by GuardedParser#True.
    def enterTrue(self, ctx:GuardedParser.TrueContext):
        pass

    # Exit a parse tree produced by GuardedParser#True.
    def exitTrue(self, ctx:GuardedParser.TrueContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArrayLowerBound.
    def enterExprArrayLowerBound(self, ctx:GuardedParser.ExprArrayLowerBoundContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArrayLowerBound.
    def exitExprArrayLowerBound(self, ctx:GuardedParser.ExprArrayLowerBoundContext):
        pass


    # Enter a parse tree produced by GuardedParser#False.
    def enterFalse(self, ctx:GuardedParser.FalseContext):
        pass

    # Exit a parse tree produced by GuardedParser#False.
    def exitFalse(self, ctx:GuardedParser.FalseContext):
        pass


    # Enter a parse tree produced by GuardedParser#ArrayLiteral.
    def enterArrayLiteral(self, ctx:GuardedParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by GuardedParser#ArrayLiteral.
    def exitArrayLiteral(self, ctx:GuardedParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArrayElement.
    def enterExprArrayElement(self, ctx:GuardedParser.ExprArrayElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArrayElement.
    def exitExprArrayElement(self, ctx:GuardedParser.ExprArrayElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#Identifier.
    def enterIdentifier(self, ctx:GuardedParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GuardedParser#Identifier.
    def exitIdentifier(self, ctx:GuardedParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GuardedParser#Brackets.
    def enterBrackets(self, ctx:GuardedParser.BracketsContext):
        pass

    # Exit a parse tree produced by GuardedParser#Brackets.
    def exitBrackets(self, ctx:GuardedParser.BracketsContext):
        pass


    # Enter a parse tree produced by GuardedParser#Number.
    def enterNumber(self, ctx:GuardedParser.NumberContext):
        pass

    # Exit a parse tree produced by GuardedParser#Number.
    def exitNumber(self, ctx:GuardedParser.NumberContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArrayUpperElement.
    def enterExprArrayUpperElement(self, ctx:GuardedParser.ExprArrayUpperElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArrayUpperElement.
    def exitExprArrayUpperElement(self, ctx:GuardedParser.ExprArrayUpperElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#And.
    def enterAnd(self, ctx:GuardedParser.AndContext):
        pass

    # Exit a parse tree produced by GuardedParser#And.
    def exitAnd(self, ctx:GuardedParser.AndContext):
        pass


    # Enter a parse tree produced by GuardedParser#Equiv.
    def enterEquiv(self, ctx:GuardedParser.EquivContext):
        pass

    # Exit a parse tree produced by GuardedParser#Equiv.
    def exitEquiv(self, ctx:GuardedParser.EquivContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprMacroCall.
    def enterExprMacroCall(self, ctx:GuardedParser.ExprMacroCallContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprMacroCall.
    def exitExprMacroCall(self, ctx:GuardedParser.ExprMacroCallContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArrayUpperBound.
    def enterExprArrayUpperBound(self, ctx:GuardedParser.ExprArrayUpperBoundContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArrayUpperBound.
    def exitExprArrayUpperBound(self, ctx:GuardedParser.ExprArrayUpperBoundContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArrayLowerElement.
    def enterExprArrayLowerElement(self, ctx:GuardedParser.ExprArrayLowerElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArrayLowerElement.
    def exitExprArrayLowerElement(self, ctx:GuardedParser.ExprArrayLowerElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#Negate.
    def enterNegate(self, ctx:GuardedParser.NegateContext):
        pass

    # Exit a parse tree produced by GuardedParser#Negate.
    def exitNegate(self, ctx:GuardedParser.NegateContext):
        pass


    # Enter a parse tree produced by GuardedParser#Logic.
    def enterLogic(self, ctx:GuardedParser.LogicContext):
        pass

    # Exit a parse tree produced by GuardedParser#Logic.
    def exitLogic(self, ctx:GuardedParser.LogicContext):
        pass


    # Enter a parse tree produced by GuardedParser#ExprArraySize.
    def enterExprArraySize(self, ctx:GuardedParser.ExprArraySizeContext):
        pass

    # Exit a parse tree produced by GuardedParser#ExprArraySize.
    def exitExprArraySize(self, ctx:GuardedParser.ExprArraySizeContext):
        pass


    # Enter a parse tree produced by GuardedParser#start.
    def enterStart(self, ctx:GuardedParser.StartContext):
        pass

    # Exit a parse tree produced by GuardedParser#start.
    def exitStart(self, ctx:GuardedParser.StartContext):
        pass


    # Enter a parse tree produced by GuardedParser#operatorList.
    def enterOperatorList(self, ctx:GuardedParser.OperatorListContext):
        pass

    # Exit a parse tree produced by GuardedParser#operatorList.
    def exitOperatorList(self, ctx:GuardedParser.OperatorListContext):
        pass


    # Enter a parse tree produced by GuardedParser#operator.
    def enterOperator(self, ctx:GuardedParser.OperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#operator.
    def exitOperator(self, ctx:GuardedParser.OperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#skipOperator.
    def enterSkipOperator(self, ctx:GuardedParser.SkipOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#skipOperator.
    def exitSkipOperator(self, ctx:GuardedParser.SkipOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#abortOperator.
    def enterAbortOperator(self, ctx:GuardedParser.AbortOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#abortOperator.
    def exitAbortOperator(self, ctx:GuardedParser.AbortOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#printOperator.
    def enterPrintOperator(self, ctx:GuardedParser.PrintOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#printOperator.
    def exitPrintOperator(self, ctx:GuardedParser.PrintOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#assignOperator.
    def enterAssignOperator(self, ctx:GuardedParser.AssignOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#assignOperator.
    def exitAssignOperator(self, ctx:GuardedParser.AssignOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#commandList.
    def enterCommandList(self, ctx:GuardedParser.CommandListContext):
        pass

    # Exit a parse tree produced by GuardedParser#commandList.
    def exitCommandList(self, ctx:GuardedParser.CommandListContext):
        pass


    # Enter a parse tree produced by GuardedParser#command.
    def enterCommand(self, ctx:GuardedParser.CommandContext):
        pass

    # Exit a parse tree produced by GuardedParser#command.
    def exitCommand(self, ctx:GuardedParser.CommandContext):
        pass


    # Enter a parse tree produced by GuardedParser#ifOperator.
    def enterIfOperator(self, ctx:GuardedParser.IfOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#ifOperator.
    def exitIfOperator(self, ctx:GuardedParser.IfOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#doOperator.
    def enterDoOperator(self, ctx:GuardedParser.DoOperatorContext):
        pass

    # Exit a parse tree produced by GuardedParser#doOperator.
    def exitDoOperator(self, ctx:GuardedParser.DoOperatorContext):
        pass


    # Enter a parse tree produced by GuardedParser#condition.
    def enterCondition(self, ctx:GuardedParser.ConditionContext):
        pass

    # Exit a parse tree produced by GuardedParser#condition.
    def exitCondition(self, ctx:GuardedParser.ConditionContext):
        pass


    # Enter a parse tree produced by GuardedParser#macroCall.
    def enterMacroCall(self, ctx:GuardedParser.MacroCallContext):
        pass

    # Exit a parse tree produced by GuardedParser#macroCall.
    def exitMacroCall(self, ctx:GuardedParser.MacroCallContext):
        pass


    # Enter a parse tree produced by GuardedParser#macroOperatorDefinition.
    def enterMacroOperatorDefinition(self, ctx:GuardedParser.MacroOperatorDefinitionContext):
        pass

    # Exit a parse tree produced by GuardedParser#macroOperatorDefinition.
    def exitMacroOperatorDefinition(self, ctx:GuardedParser.MacroOperatorDefinitionContext):
        pass


    # Enter a parse tree produced by GuardedParser#macroExpressionDefinition.
    def enterMacroExpressionDefinition(self, ctx:GuardedParser.MacroExpressionDefinitionContext):
        pass

    # Exit a parse tree produced by GuardedParser#macroExpressionDefinition.
    def exitMacroExpressionDefinition(self, ctx:GuardedParser.MacroExpressionDefinitionContext):
        pass


    # Enter a parse tree produced by GuardedParser#formalParameters.
    def enterFormalParameters(self, ctx:GuardedParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by GuardedParser#formalParameters.
    def exitFormalParameters(self, ctx:GuardedParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by GuardedParser#actualParameters.
    def enterActualParameters(self, ctx:GuardedParser.ActualParametersContext):
        pass

    # Exit a parse tree produced by GuardedParser#actualParameters.
    def exitActualParameters(self, ctx:GuardedParser.ActualParametersContext):
        pass


    # Enter a parse tree produced by GuardedParser#initialAssignments.
    def enterInitialAssignments(self, ctx:GuardedParser.InitialAssignmentsContext):
        pass

    # Exit a parse tree produced by GuardedParser#initialAssignments.
    def exitInitialAssignments(self, ctx:GuardedParser.InitialAssignmentsContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayLowerBound.
    def enterArrayLowerBound(self, ctx:GuardedParser.ArrayLowerBoundContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayLowerBound.
    def exitArrayLowerBound(self, ctx:GuardedParser.ArrayLowerBoundContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayUpperBound.
    def enterArrayUpperBound(self, ctx:GuardedParser.ArrayUpperBoundContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayUpperBound.
    def exitArrayUpperBound(self, ctx:GuardedParser.ArrayUpperBoundContext):
        pass


    # Enter a parse tree produced by GuardedParser#arraySize.
    def enterArraySize(self, ctx:GuardedParser.ArraySizeContext):
        pass

    # Exit a parse tree produced by GuardedParser#arraySize.
    def exitArraySize(self, ctx:GuardedParser.ArraySizeContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayElement.
    def enterArrayElement(self, ctx:GuardedParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayElement.
    def exitArrayElement(self, ctx:GuardedParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayLowerElement.
    def enterArrayLowerElement(self, ctx:GuardedParser.ArrayLowerElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayLowerElement.
    def exitArrayLowerElement(self, ctx:GuardedParser.ArrayLowerElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayUpperElement.
    def enterArrayUpperElement(self, ctx:GuardedParser.ArrayUpperElementContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayUpperElement.
    def exitArrayUpperElement(self, ctx:GuardedParser.ArrayUpperElementContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayShift.
    def enterArrayShift(self, ctx:GuardedParser.ArrayShiftContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayShift.
    def exitArrayShift(self, ctx:GuardedParser.ArrayShiftContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayPushUp.
    def enterArrayPushUp(self, ctx:GuardedParser.ArrayPushUpContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayPushUp.
    def exitArrayPushUp(self, ctx:GuardedParser.ArrayPushUpContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayPushDown.
    def enterArrayPushDown(self, ctx:GuardedParser.ArrayPushDownContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayPushDown.
    def exitArrayPushDown(self, ctx:GuardedParser.ArrayPushDownContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayDelUp.
    def enterArrayDelUp(self, ctx:GuardedParser.ArrayDelUpContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayDelUp.
    def exitArrayDelUp(self, ctx:GuardedParser.ArrayDelUpContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayDelDown.
    def enterArrayDelDown(self, ctx:GuardedParser.ArrayDelDownContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayDelDown.
    def exitArrayDelDown(self, ctx:GuardedParser.ArrayDelDownContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayPopUp.
    def enterArrayPopUp(self, ctx:GuardedParser.ArrayPopUpContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayPopUp.
    def exitArrayPopUp(self, ctx:GuardedParser.ArrayPopUpContext):
        pass


    # Enter a parse tree produced by GuardedParser#arrayPopDown.
    def enterArrayPopDown(self, ctx:GuardedParser.ArrayPopDownContext):
        pass

    # Exit a parse tree produced by GuardedParser#arrayPopDown.
    def exitArrayPopDown(self, ctx:GuardedParser.ArrayPopDownContext):
        pass


    # Enter a parse tree produced by GuardedParser#arraySwap.
    def enterArraySwap(self, ctx:GuardedParser.ArraySwapContext):
        pass

    # Exit a parse tree produced by GuardedParser#arraySwap.
    def exitArraySwap(self, ctx:GuardedParser.ArraySwapContext):
        pass


    # Enter a parse tree produced by GuardedParser#arraySet.
    def enterArraySet(self, ctx:GuardedParser.ArraySetContext):
        pass

    # Exit a parse tree produced by GuardedParser#arraySet.
    def exitArraySet(self, ctx:GuardedParser.ArraySetContext):
        pass


