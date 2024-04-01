# Generated from ./CQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CQLParser import CQLParser
else:
    from CQLParser import CQLParser

# This class defines a complete generic visitor for a parse tree produced by CQLParser.

class CQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CQLParser#query.
    def visitQuery(self, ctx:CQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#complexQuery.
    def visitComplexQuery(self, ctx:CQLParser.ComplexQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#within.
    def visitWithin(self, ctx:CQLParser.WithinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#containing.
    def visitContaining(self, ctx:CQLParser.ContainingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#simpleQuery.
    def visitSimpleQuery(self, ctx:CQLParser.SimpleQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#sequence.
    def visitSequence(self, ctx:CQLParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#sequencePart.
    def visitSequencePart(self, ctx:CQLParser.SequencePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#tag.
    def visitTag(self, ctx:CQLParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#attribute.
    def visitAttribute(self, ctx:CQLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#positionPositionWord.
    def visitPositionPositionWord(self, ctx:CQLParser.PositionPositionWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#positionPositionLong.
    def visitPositionPositionLong(self, ctx:CQLParser.PositionPositionLongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#positionWord.
    def visitPositionWord(self, ctx:CQLParser.PositionWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#positionLong.
    def visitPositionLong(self, ctx:CQLParser.PositionLongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#positionLongPart.
    def visitPositionLongPart(self, ctx:CQLParser.PositionLongPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#attValuePairEquals.
    def visitAttValuePairEquals(self, ctx:CQLParser.AttValuePairEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#attValuePairNotEquals.
    def visitAttValuePairNotEquals(self, ctx:CQLParser.AttValuePairNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#attValuePairDefaultEquals.
    def visitAttValuePairDefaultEquals(self, ctx:CQLParser.AttValuePairDefaultEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#propName.
    def visitPropName(self, ctx:CQLParser.PropNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#repetitionZeroOrMore.
    def visitRepetitionZeroOrMore(self, ctx:CQLParser.RepetitionZeroOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#repetitionOneOrMore.
    def visitRepetitionOneOrMore(self, ctx:CQLParser.RepetitionOneOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#repetitionZeroOrOne.
    def visitRepetitionZeroOrOne(self, ctx:CQLParser.RepetitionZeroOrOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#repetitionExactly.
    def visitRepetitionExactly(self, ctx:CQLParser.RepetitionExactlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#repetitionMinMax.
    def visitRepetitionMinMax(self, ctx:CQLParser.RepetitionMinMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#quotedString.
    def visitQuotedString(self, ctx:CQLParser.QuotedStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#and.
    def visitAnd(self, ctx:CQLParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#or.
    def visitOr(self, ctx:CQLParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#implication.
    def visitImplication(self, ctx:CQLParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#valuePartString.
    def visitValuePartString(self, ctx:CQLParser.ValuePartStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#valuePartParenthesised.
    def visitValuePartParenthesised(self, ctx:CQLParser.ValuePartParenthesisedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#valueWith.
    def visitValueWith(self, ctx:CQLParser.ValueWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CQLParser#valueWithout.
    def visitValueWithout(self, ctx:CQLParser.ValueWithoutContext):
        return self.visitChildren(ctx)



del CQLParser