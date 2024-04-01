# Generated from ./CQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CQLParser import CQLParser
else:
    from CQLParser import CQLParser

# This class defines a complete listener for a parse tree produced by CQLParser.
class CQLListener(ParseTreeListener):

    # Enter a parse tree produced by CQLParser#query.
    def enterQuery(self, ctx:CQLParser.QueryContext):
        pass

    # Exit a parse tree produced by CQLParser#query.
    def exitQuery(self, ctx:CQLParser.QueryContext):
        pass


    # Enter a parse tree produced by CQLParser#complexQuery.
    def enterComplexQuery(self, ctx:CQLParser.ComplexQueryContext):
        pass

    # Exit a parse tree produced by CQLParser#complexQuery.
    def exitComplexQuery(self, ctx:CQLParser.ComplexQueryContext):
        pass


    # Enter a parse tree produced by CQLParser#within.
    def enterWithin(self, ctx:CQLParser.WithinContext):
        pass

    # Exit a parse tree produced by CQLParser#within.
    def exitWithin(self, ctx:CQLParser.WithinContext):
        pass


    # Enter a parse tree produced by CQLParser#containing.
    def enterContaining(self, ctx:CQLParser.ContainingContext):
        pass

    # Exit a parse tree produced by CQLParser#containing.
    def exitContaining(self, ctx:CQLParser.ContainingContext):
        pass


    # Enter a parse tree produced by CQLParser#simpleQuery.
    def enterSimpleQuery(self, ctx:CQLParser.SimpleQueryContext):
        pass

    # Exit a parse tree produced by CQLParser#simpleQuery.
    def exitSimpleQuery(self, ctx:CQLParser.SimpleQueryContext):
        pass


    # Enter a parse tree produced by CQLParser#sequence.
    def enterSequence(self, ctx:CQLParser.SequenceContext):
        pass

    # Exit a parse tree produced by CQLParser#sequence.
    def exitSequence(self, ctx:CQLParser.SequenceContext):
        pass


    # Enter a parse tree produced by CQLParser#sequencePart.
    def enterSequencePart(self, ctx:CQLParser.SequencePartContext):
        pass

    # Exit a parse tree produced by CQLParser#sequencePart.
    def exitSequencePart(self, ctx:CQLParser.SequencePartContext):
        pass


    # Enter a parse tree produced by CQLParser#tag.
    def enterTag(self, ctx:CQLParser.TagContext):
        pass

    # Exit a parse tree produced by CQLParser#tag.
    def exitTag(self, ctx:CQLParser.TagContext):
        pass


    # Enter a parse tree produced by CQLParser#attribute.
    def enterAttribute(self, ctx:CQLParser.AttributeContext):
        pass

    # Exit a parse tree produced by CQLParser#attribute.
    def exitAttribute(self, ctx:CQLParser.AttributeContext):
        pass


    # Enter a parse tree produced by CQLParser#positionPositionWord.
    def enterPositionPositionWord(self, ctx:CQLParser.PositionPositionWordContext):
        pass

    # Exit a parse tree produced by CQLParser#positionPositionWord.
    def exitPositionPositionWord(self, ctx:CQLParser.PositionPositionWordContext):
        pass


    # Enter a parse tree produced by CQLParser#positionPositionLong.
    def enterPositionPositionLong(self, ctx:CQLParser.PositionPositionLongContext):
        pass

    # Exit a parse tree produced by CQLParser#positionPositionLong.
    def exitPositionPositionLong(self, ctx:CQLParser.PositionPositionLongContext):
        pass


    # Enter a parse tree produced by CQLParser#positionWord.
    def enterPositionWord(self, ctx:CQLParser.PositionWordContext):
        pass

    # Exit a parse tree produced by CQLParser#positionWord.
    def exitPositionWord(self, ctx:CQLParser.PositionWordContext):
        pass


    # Enter a parse tree produced by CQLParser#positionLong.
    def enterPositionLong(self, ctx:CQLParser.PositionLongContext):
        pass

    # Exit a parse tree produced by CQLParser#positionLong.
    def exitPositionLong(self, ctx:CQLParser.PositionLongContext):
        pass


    # Enter a parse tree produced by CQLParser#positionLongPart.
    def enterPositionLongPart(self, ctx:CQLParser.PositionLongPartContext):
        pass

    # Exit a parse tree produced by CQLParser#positionLongPart.
    def exitPositionLongPart(self, ctx:CQLParser.PositionLongPartContext):
        pass


    # Enter a parse tree produced by CQLParser#attValuePairEquals.
    def enterAttValuePairEquals(self, ctx:CQLParser.AttValuePairEqualsContext):
        pass

    # Exit a parse tree produced by CQLParser#attValuePairEquals.
    def exitAttValuePairEquals(self, ctx:CQLParser.AttValuePairEqualsContext):
        pass


    # Enter a parse tree produced by CQLParser#attValuePairNotEquals.
    def enterAttValuePairNotEquals(self, ctx:CQLParser.AttValuePairNotEqualsContext):
        pass

    # Exit a parse tree produced by CQLParser#attValuePairNotEquals.
    def exitAttValuePairNotEquals(self, ctx:CQLParser.AttValuePairNotEqualsContext):
        pass


    # Enter a parse tree produced by CQLParser#attValuePairDefaultEquals.
    def enterAttValuePairDefaultEquals(self, ctx:CQLParser.AttValuePairDefaultEqualsContext):
        pass

    # Exit a parse tree produced by CQLParser#attValuePairDefaultEquals.
    def exitAttValuePairDefaultEquals(self, ctx:CQLParser.AttValuePairDefaultEqualsContext):
        pass


    # Enter a parse tree produced by CQLParser#propName.
    def enterPropName(self, ctx:CQLParser.PropNameContext):
        pass

    # Exit a parse tree produced by CQLParser#propName.
    def exitPropName(self, ctx:CQLParser.PropNameContext):
        pass


    # Enter a parse tree produced by CQLParser#repetitionZeroOrMore.
    def enterRepetitionZeroOrMore(self, ctx:CQLParser.RepetitionZeroOrMoreContext):
        pass

    # Exit a parse tree produced by CQLParser#repetitionZeroOrMore.
    def exitRepetitionZeroOrMore(self, ctx:CQLParser.RepetitionZeroOrMoreContext):
        pass


    # Enter a parse tree produced by CQLParser#repetitionOneOrMore.
    def enterRepetitionOneOrMore(self, ctx:CQLParser.RepetitionOneOrMoreContext):
        pass

    # Exit a parse tree produced by CQLParser#repetitionOneOrMore.
    def exitRepetitionOneOrMore(self, ctx:CQLParser.RepetitionOneOrMoreContext):
        pass


    # Enter a parse tree produced by CQLParser#repetitionZeroOrOne.
    def enterRepetitionZeroOrOne(self, ctx:CQLParser.RepetitionZeroOrOneContext):
        pass

    # Exit a parse tree produced by CQLParser#repetitionZeroOrOne.
    def exitRepetitionZeroOrOne(self, ctx:CQLParser.RepetitionZeroOrOneContext):
        pass


    # Enter a parse tree produced by CQLParser#repetitionExactly.
    def enterRepetitionExactly(self, ctx:CQLParser.RepetitionExactlyContext):
        pass

    # Exit a parse tree produced by CQLParser#repetitionExactly.
    def exitRepetitionExactly(self, ctx:CQLParser.RepetitionExactlyContext):
        pass


    # Enter a parse tree produced by CQLParser#repetitionMinMax.
    def enterRepetitionMinMax(self, ctx:CQLParser.RepetitionMinMaxContext):
        pass

    # Exit a parse tree produced by CQLParser#repetitionMinMax.
    def exitRepetitionMinMax(self, ctx:CQLParser.RepetitionMinMaxContext):
        pass


    # Enter a parse tree produced by CQLParser#quotedString.
    def enterQuotedString(self, ctx:CQLParser.QuotedStringContext):
        pass

    # Exit a parse tree produced by CQLParser#quotedString.
    def exitQuotedString(self, ctx:CQLParser.QuotedStringContext):
        pass


    # Enter a parse tree produced by CQLParser#and.
    def enterAnd(self, ctx:CQLParser.AndContext):
        pass

    # Exit a parse tree produced by CQLParser#and.
    def exitAnd(self, ctx:CQLParser.AndContext):
        pass


    # Enter a parse tree produced by CQLParser#or.
    def enterOr(self, ctx:CQLParser.OrContext):
        pass

    # Exit a parse tree produced by CQLParser#or.
    def exitOr(self, ctx:CQLParser.OrContext):
        pass


    # Enter a parse tree produced by CQLParser#implication.
    def enterImplication(self, ctx:CQLParser.ImplicationContext):
        pass

    # Exit a parse tree produced by CQLParser#implication.
    def exitImplication(self, ctx:CQLParser.ImplicationContext):
        pass


    # Enter a parse tree produced by CQLParser#valuePartString.
    def enterValuePartString(self, ctx:CQLParser.ValuePartStringContext):
        pass

    # Exit a parse tree produced by CQLParser#valuePartString.
    def exitValuePartString(self, ctx:CQLParser.ValuePartStringContext):
        pass


    # Enter a parse tree produced by CQLParser#valuePartParenthesised.
    def enterValuePartParenthesised(self, ctx:CQLParser.ValuePartParenthesisedContext):
        pass

    # Exit a parse tree produced by CQLParser#valuePartParenthesised.
    def exitValuePartParenthesised(self, ctx:CQLParser.ValuePartParenthesisedContext):
        pass


    # Enter a parse tree produced by CQLParser#valueWith.
    def enterValueWith(self, ctx:CQLParser.ValueWithContext):
        pass

    # Exit a parse tree produced by CQLParser#valueWith.
    def exitValueWith(self, ctx:CQLParser.ValueWithContext):
        pass


    # Enter a parse tree produced by CQLParser#valueWithout.
    def enterValueWithout(self, ctx:CQLParser.ValueWithoutContext):
        pass

    # Exit a parse tree produced by CQLParser#valueWithout.
    def exitValueWithout(self, ctx:CQLParser.ValueWithoutContext):
        pass



del CQLParser