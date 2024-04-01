# Generated from ./CQL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,174,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,45,8,1,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,3,3,55,8,
        3,1,4,4,4,58,8,4,11,4,12,4,59,1,5,1,5,3,5,64,8,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,72,8,5,1,5,3,5,75,8,5,1,6,1,6,3,6,79,8,6,1,6,1,6,5,6,
        83,8,6,10,6,12,6,86,9,6,1,6,3,6,89,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,3,8,100,8,8,1,8,3,8,103,8,8,1,9,1,9,1,10,1,10,1,10,1,10,
        3,10,111,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,120,8,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,131,8,12,1,13,1,
        13,1,13,3,13,136,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,148,8,14,1,14,3,14,151,8,14,1,15,1,15,1,16,1,16,1,16,
        3,16,158,8,16,1,17,1,17,1,17,1,17,1,17,3,17,165,8,17,1,18,1,18,1,
        18,1,18,1,18,3,18,172,8,18,1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,0,2,1,0,7,8,1,0,9,10,182,0,38,1,0,0,0,
        2,40,1,0,0,0,4,48,1,0,0,0,6,50,1,0,0,0,8,57,1,0,0,0,10,63,1,0,0,
        0,12,76,1,0,0,0,14,92,1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,0,20,106,
        1,0,0,0,22,119,1,0,0,0,24,130,1,0,0,0,26,132,1,0,0,0,28,150,1,0,
        0,0,30,152,1,0,0,0,32,157,1,0,0,0,34,164,1,0,0,0,36,171,1,0,0,0,
        38,39,3,2,1,0,39,1,1,0,0,0,40,44,3,6,3,0,41,42,3,4,2,0,42,43,3,2,
        1,0,43,45,1,0,0,0,44,41,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,49,
        5,5,0,0,47,49,5,6,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,5,1,0,0,0,50,
        54,3,8,4,0,51,52,3,32,16,0,52,53,3,6,3,0,53,55,1,0,0,0,54,51,1,0,
        0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,58,3,10,5,0,57,56,1,0,0,0,58,59,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,9,1,0,0,0,61,62,7,0,0,0,62,
        64,5,1,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,71,1,0,0,0,65,72,3,12,
        6,0,66,72,3,16,8,0,67,68,5,18,0,0,68,69,3,2,1,0,69,70,5,19,0,0,70,
        72,1,0,0,0,71,65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,72,74,1,0,0,
        0,73,75,3,28,14,0,74,73,1,0,0,0,74,75,1,0,0,0,75,11,1,0,0,0,76,78,
        5,12,0,0,77,79,5,14,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,
        0,80,84,5,7,0,0,81,83,3,14,7,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,
        1,0,0,0,84,85,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,87,89,5,14,0,0,
        88,87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,5,13,0,0,91,13,1,
        0,0,0,92,93,5,7,0,0,93,94,5,15,0,0,94,95,3,30,15,0,95,15,1,0,0,0,
        96,103,3,18,9,0,97,99,5,16,0,0,98,100,3,20,10,0,99,98,1,0,0,0,99,
        100,1,0,0,0,100,101,1,0,0,0,101,103,5,17,0,0,102,96,1,0,0,0,102,
        97,1,0,0,0,103,17,1,0,0,0,104,105,3,30,15,0,105,19,1,0,0,0,106,110,
        3,22,11,0,107,108,3,32,16,0,108,109,3,20,10,0,109,111,1,0,0,0,110,
        107,1,0,0,0,110,111,1,0,0,0,111,21,1,0,0,0,112,120,3,24,12,0,113,
        114,5,18,0,0,114,115,3,20,10,0,115,116,5,19,0,0,116,120,1,0,0,0,
        117,118,5,20,0,0,118,120,3,22,11,0,119,112,1,0,0,0,119,113,1,0,0,
        0,119,117,1,0,0,0,120,23,1,0,0,0,121,122,3,26,13,0,122,123,5,15,
        0,0,123,124,3,34,17,0,124,131,1,0,0,0,125,126,3,26,13,0,126,127,
        5,2,0,0,127,128,3,34,17,0,128,131,1,0,0,0,129,131,3,34,17,0,130,
        121,1,0,0,0,130,125,1,0,0,0,130,129,1,0,0,0,131,25,1,0,0,0,132,135,
        5,7,0,0,133,134,5,14,0,0,134,136,5,7,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,27,1,0,0,0,137,151,5,21,0,0,138,151,5,22,0,0,139,151,
        5,23,0,0,140,141,5,24,0,0,141,142,5,8,0,0,142,151,5,25,0,0,143,144,
        5,24,0,0,144,145,5,8,0,0,145,147,5,3,0,0,146,148,5,8,0,0,147,146,
        1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,151,5,25,0,0,150,137,
        1,0,0,0,150,138,1,0,0,0,150,139,1,0,0,0,150,140,1,0,0,0,150,143,
        1,0,0,0,151,29,1,0,0,0,152,153,7,1,0,0,153,31,1,0,0,0,154,158,5,
        26,0,0,155,158,5,27,0,0,156,158,5,4,0,0,157,154,1,0,0,0,157,155,
        1,0,0,0,157,156,1,0,0,0,158,33,1,0,0,0,159,165,3,30,15,0,160,161,
        5,18,0,0,161,162,3,36,18,0,162,163,5,19,0,0,163,165,1,0,0,0,164,
        159,1,0,0,0,164,160,1,0,0,0,165,35,1,0,0,0,166,167,3,34,17,0,167,
        168,3,32,16,0,168,169,3,36,18,0,169,172,1,0,0,0,170,172,3,34,17,
        0,171,166,1,0,0,0,171,170,1,0,0,0,172,37,1,0,0,0,21,44,48,54,59,
        63,71,74,78,84,88,99,102,110,119,130,135,147,150,157,164,171
    ]

class CQLParser ( Parser ):

    grammarFileName = "CQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'!='", "','", "'->'", "'WITHIN'", 
                     "'CONTAINING'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "'>'", "'/'", "'='", 
                     "'['", "']'", "'('", "')'", "'!'", "'*'", "'+'", "'?'", 
                     "'{'", "'}'", "'&'", "'|'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WITHIN", "CONTAINING", "NAME", "NUMBER", 
                      "DOUBLE_QUOTED_STRING", "SINGLE_QUOTED_STRING", "WS", 
                      "LT", "GT", "SOLIDUS", "EQUALS", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                      "EXCLAMATION_MARK", "ASTERISK", "PLUS", "QUESTION_MARK", 
                      "LEFT_CURLY_BRACKET", "LEFT_RIGHT_BRACKET", "AMPERSAND", 
                      "VERTICAL_LINE", "HYPHEN_MINUS" ]

    RULE_query = 0
    RULE_complexQuery = 1
    RULE_queryOperator = 2
    RULE_simpleQuery = 3
    RULE_sequence = 4
    RULE_sequencePart = 5
    RULE_tag = 6
    RULE_attribute = 7
    RULE_position = 8
    RULE_positionWord = 9
    RULE_positionLong = 10
    RULE_positionLongPart = 11
    RULE_attValuePair = 12
    RULE_propName = 13
    RULE_repetitionAmount = 14
    RULE_quotedString = 15
    RULE_booleanOperator = 16
    RULE_valuePart = 17
    RULE_value = 18

    ruleNames =  [ "query", "complexQuery", "queryOperator", "simpleQuery", 
                   "sequence", "sequencePart", "tag", "attribute", "position", 
                   "positionWord", "positionLong", "positionLongPart", "attValuePair", 
                   "propName", "repetitionAmount", "quotedString", "booleanOperator", 
                   "valuePart", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WITHIN=5
    CONTAINING=6
    NAME=7
    NUMBER=8
    DOUBLE_QUOTED_STRING=9
    SINGLE_QUOTED_STRING=10
    WS=11
    LT=12
    GT=13
    SOLIDUS=14
    EQUALS=15
    LEFT_SQUARE_BRACKET=16
    RIGHT_SQUARE_BRACKET=17
    LEFT_PARENTHESIS=18
    RIGHT_PARENTHESIS=19
    EXCLAMATION_MARK=20
    ASTERISK=21
    PLUS=22
    QUESTION_MARK=23
    LEFT_CURLY_BRACKET=24
    LEFT_RIGHT_BRACKET=25
    AMPERSAND=26
    VERTICAL_LINE=27
    HYPHEN_MINUS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complexQuery(self):
            return self.getTypedRuleContext(CQLParser.ComplexQueryContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = CQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.complexQuery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleQuery(self):
            return self.getTypedRuleContext(CQLParser.SimpleQueryContext,0)


        def queryOperator(self):
            return self.getTypedRuleContext(CQLParser.QueryOperatorContext,0)


        def complexQuery(self):
            return self.getTypedRuleContext(CQLParser.ComplexQueryContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_complexQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexQuery" ):
                listener.enterComplexQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexQuery" ):
                listener.exitComplexQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexQuery" ):
                return visitor.visitComplexQuery(self)
            else:
                return visitor.visitChildren(self)




    def complexQuery(self):

        localctx = CQLParser.ComplexQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_complexQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.simpleQuery()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5 or _la==6:
                self.state = 41
                self.queryOperator()
                self.state = 42
                self.complexQuery()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_queryOperator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WithinContext(QueryOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.QueryOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WITHIN(self):
            return self.getToken(CQLParser.WITHIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithin" ):
                listener.enterWithin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithin" ):
                listener.exitWithin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithin" ):
                return visitor.visitWithin(self)
            else:
                return visitor.visitChildren(self)


    class ContainingContext(QueryOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.QueryOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTAINING(self):
            return self.getToken(CQLParser.CONTAINING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContaining" ):
                listener.enterContaining(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContaining" ):
                listener.exitContaining(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContaining" ):
                return visitor.visitContaining(self)
            else:
                return visitor.visitChildren(self)



    def queryOperator(self):

        localctx = CQLParser.QueryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_queryOperator)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = CQLParser.WithinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(CQLParser.WITHIN)
                pass
            elif token in [6]:
                localctx = CQLParser.ContainingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(CQLParser.CONTAINING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(CQLParser.SequenceContext,0)


        def booleanOperator(self):
            return self.getTypedRuleContext(CQLParser.BooleanOperatorContext,0)


        def simpleQuery(self):
            return self.getTypedRuleContext(CQLParser.SimpleQueryContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_simpleQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleQuery" ):
                listener.enterSimpleQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleQuery" ):
                listener.exitSimpleQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleQuery" ):
                return visitor.visitSimpleQuery(self)
            else:
                return visitor.visitChildren(self)




    def simpleQuery(self):

        localctx = CQLParser.SimpleQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.sequence()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 201326608) != 0):
                self.state = 51
                self.booleanOperator()
                self.state = 52
                self.simpleQuery()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequencePart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CQLParser.SequencePartContext)
            else:
                return self.getTypedRuleContext(CQLParser.SequencePartContext,i)


        def getRuleIndex(self):
            return CQLParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = CQLParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.sequencePart()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 333696) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequencePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag(self):
            return self.getTypedRuleContext(CQLParser.TagContext,0)


        def position(self):
            return self.getTypedRuleContext(CQLParser.PositionContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(CQLParser.LEFT_PARENTHESIS, 0)

        def complexQuery(self):
            return self.getTypedRuleContext(CQLParser.ComplexQueryContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(CQLParser.RIGHT_PARENTHESIS, 0)

        def repetitionAmount(self):
            return self.getTypedRuleContext(CQLParser.RepetitionAmountContext,0)


        def NAME(self):
            return self.getToken(CQLParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(CQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_sequencePart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequencePart" ):
                listener.enterSequencePart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequencePart" ):
                listener.exitSequencePart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequencePart" ):
                return visitor.visitSequencePart(self)
            else:
                return visitor.visitChildren(self)




    def sequencePart(self):

        localctx = CQLParser.SequencePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sequencePart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.match(CQLParser.T__0)


            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 65
                self.tag()
                pass
            elif token in [9, 10, 16]:
                self.state = 66
                self.position()
                pass
            elif token in [18]:
                self.state = 67
                self.match(CQLParser.LEFT_PARENTHESIS)
                self.state = 68
                self.complexQuery()
                self.state = 69
                self.match(CQLParser.RIGHT_PARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0):
                self.state = 73
                self.repetitionAmount()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CQLParser.LT, 0)

        def NAME(self):
            return self.getToken(CQLParser.NAME, 0)

        def GT(self):
            return self.getToken(CQLParser.GT, 0)

        def SOLIDUS(self, i:int=None):
            if i is None:
                return self.getTokens(CQLParser.SOLIDUS)
            else:
                return self.getToken(CQLParser.SOLIDUS, i)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CQLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(CQLParser.AttributeContext,i)


        def getRuleIndex(self):
            return CQLParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag" ):
                return visitor.visitTag(self)
            else:
                return visitor.visitChildren(self)




    def tag(self):

        localctx = CQLParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CQLParser.LT)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 77
                self.match(CQLParser.SOLIDUS)


            self.state = 80
            self.match(CQLParser.NAME)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 81
                self.attribute()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 87
                self.match(CQLParser.SOLIDUS)


            self.state = 90
            self.match(CQLParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CQLParser.NAME, 0)

        def EQUALS(self):
            return self.getToken(CQLParser.EQUALS, 0)

        def quotedString(self):
            return self.getTypedRuleContext(CQLParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CQLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CQLParser.NAME)
            self.state = 93
            self.match(CQLParser.EQUALS)
            self.state = 94
            self.quotedString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_position

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PositionPositionWordContext(PositionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.PositionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def positionWord(self):
            return self.getTypedRuleContext(CQLParser.PositionWordContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionPositionWord" ):
                listener.enterPositionPositionWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionPositionWord" ):
                listener.exitPositionPositionWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionPositionWord" ):
                return visitor.visitPositionPositionWord(self)
            else:
                return visitor.visitChildren(self)


    class PositionPositionLongContext(PositionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.PositionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(CQLParser.LEFT_SQUARE_BRACKET, 0)
        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(CQLParser.RIGHT_SQUARE_BRACKET, 0)
        def positionLong(self):
            return self.getTypedRuleContext(CQLParser.PositionLongContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionPositionLong" ):
                listener.enterPositionPositionLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionPositionLong" ):
                listener.exitPositionPositionLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionPositionLong" ):
                return visitor.visitPositionPositionLong(self)
            else:
                return visitor.visitChildren(self)



    def position(self):

        localctx = CQLParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                localctx = CQLParser.PositionPositionWordContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.positionWord()
                pass
            elif token in [16]:
                localctx = CQLParser.PositionPositionLongContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(CQLParser.LEFT_SQUARE_BRACKET)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1312384) != 0):
                    self.state = 98
                    self.positionLong()


                self.state = 101
                self.match(CQLParser.RIGHT_SQUARE_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quotedString(self):
            return self.getTypedRuleContext(CQLParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_positionWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionWord" ):
                listener.enterPositionWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionWord" ):
                listener.exitPositionWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionWord" ):
                return visitor.visitPositionWord(self)
            else:
                return visitor.visitChildren(self)




    def positionWord(self):

        localctx = CQLParser.PositionWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_positionWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.quotedString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionLongContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positionLongPart(self):
            return self.getTypedRuleContext(CQLParser.PositionLongPartContext,0)


        def booleanOperator(self):
            return self.getTypedRuleContext(CQLParser.BooleanOperatorContext,0)


        def positionLong(self):
            return self.getTypedRuleContext(CQLParser.PositionLongContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_positionLong

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionLong" ):
                listener.enterPositionLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionLong" ):
                listener.exitPositionLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionLong" ):
                return visitor.visitPositionLong(self)
            else:
                return visitor.visitChildren(self)




    def positionLong(self):

        localctx = CQLParser.PositionLongContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_positionLong)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.positionLongPart()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 201326608) != 0):
                self.state = 107
                self.booleanOperator()
                self.state = 108
                self.positionLong()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionLongPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attValuePair(self):
            return self.getTypedRuleContext(CQLParser.AttValuePairContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(CQLParser.LEFT_PARENTHESIS, 0)

        def positionLong(self):
            return self.getTypedRuleContext(CQLParser.PositionLongContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(CQLParser.RIGHT_PARENTHESIS, 0)

        def EXCLAMATION_MARK(self):
            return self.getToken(CQLParser.EXCLAMATION_MARK, 0)

        def positionLongPart(self):
            return self.getTypedRuleContext(CQLParser.PositionLongPartContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_positionLongPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionLongPart" ):
                listener.enterPositionLongPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionLongPart" ):
                listener.exitPositionLongPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionLongPart" ):
                return visitor.visitPositionLongPart(self)
            else:
                return visitor.visitChildren(self)




    def positionLongPart(self):

        localctx = CQLParser.PositionLongPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_positionLongPart)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.attValuePair()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(CQLParser.LEFT_PARENTHESIS)
                self.state = 114
                self.positionLong()
                self.state = 115
                self.match(CQLParser.RIGHT_PARENTHESIS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(CQLParser.EXCLAMATION_MARK)
                self.state = 118
                self.positionLongPart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_attValuePair

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttValuePairEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propName(self):
            return self.getTypedRuleContext(CQLParser.PropNameContext,0)

        def EQUALS(self):
            return self.getToken(CQLParser.EQUALS, 0)
        def valuePart(self):
            return self.getTypedRuleContext(CQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairEquals" ):
                listener.enterAttValuePairEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairEquals" ):
                listener.exitAttValuePairEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairEquals" ):
                return visitor.visitAttValuePairEquals(self)
            else:
                return visitor.visitChildren(self)


    class AttValuePairNotEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propName(self):
            return self.getTypedRuleContext(CQLParser.PropNameContext,0)

        def valuePart(self):
            return self.getTypedRuleContext(CQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairNotEquals" ):
                listener.enterAttValuePairNotEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairNotEquals" ):
                listener.exitAttValuePairNotEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairNotEquals" ):
                return visitor.visitAttValuePairNotEquals(self)
            else:
                return visitor.visitChildren(self)


    class AttValuePairDefaultEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairDefaultEquals" ):
                listener.enterAttValuePairDefaultEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairDefaultEquals" ):
                listener.exitAttValuePairDefaultEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairDefaultEquals" ):
                return visitor.visitAttValuePairDefaultEquals(self)
            else:
                return visitor.visitChildren(self)



    def attValuePair(self):

        localctx = CQLParser.AttValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attValuePair)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = CQLParser.AttValuePairEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.propName()
                self.state = 122
                self.match(CQLParser.EQUALS)
                self.state = 123
                self.valuePart()
                pass

            elif la_ == 2:
                localctx = CQLParser.AttValuePairNotEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.propName()
                self.state = 126
                self.match(CQLParser.T__1)
                self.state = 127
                self.valuePart()
                pass

            elif la_ == 3:
                localctx = CQLParser.AttValuePairDefaultEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.valuePart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CQLParser.NAME)
            else:
                return self.getToken(CQLParser.NAME, i)

        def SOLIDUS(self):
            return self.getToken(CQLParser.SOLIDUS, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_propName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropName" ):
                listener.enterPropName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropName" ):
                listener.exitPropName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropName" ):
                return visitor.visitPropName(self)
            else:
                return visitor.visitChildren(self)




    def propName(self):

        localctx = CQLParser.PropNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_propName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CQLParser.NAME)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 133
                self.match(CQLParser.SOLIDUS)
                self.state = 134
                self.match(CQLParser.NAME)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetitionAmountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_repetitionAmount

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepetitionZeroOrMoreContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASTERISK(self):
            return self.getToken(CQLParser.ASTERISK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionZeroOrMore" ):
                listener.enterRepetitionZeroOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionZeroOrMore" ):
                listener.exitRepetitionZeroOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionZeroOrMore" ):
                return visitor.visitRepetitionZeroOrMore(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionMinMaxContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(CQLParser.LEFT_CURLY_BRACKET, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CQLParser.NUMBER)
            else:
                return self.getToken(CQLParser.NUMBER, i)
        def LEFT_RIGHT_BRACKET(self):
            return self.getToken(CQLParser.LEFT_RIGHT_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionMinMax" ):
                listener.enterRepetitionMinMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionMinMax" ):
                listener.exitRepetitionMinMax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionMinMax" ):
                return visitor.visitRepetitionMinMax(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionExactlyContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(CQLParser.LEFT_CURLY_BRACKET, 0)
        def NUMBER(self):
            return self.getToken(CQLParser.NUMBER, 0)
        def LEFT_RIGHT_BRACKET(self):
            return self.getToken(CQLParser.LEFT_RIGHT_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionExactly" ):
                listener.enterRepetitionExactly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionExactly" ):
                listener.exitRepetitionExactly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionExactly" ):
                return visitor.visitRepetitionExactly(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionZeroOrOneContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUESTION_MARK(self):
            return self.getToken(CQLParser.QUESTION_MARK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionZeroOrOne" ):
                listener.enterRepetitionZeroOrOne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionZeroOrOne" ):
                listener.exitRepetitionZeroOrOne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionZeroOrOne" ):
                return visitor.visitRepetitionZeroOrOne(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionOneOrMoreContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(CQLParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionOneOrMore" ):
                listener.enterRepetitionOneOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionOneOrMore" ):
                listener.exitRepetitionOneOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionOneOrMore" ):
                return visitor.visitRepetitionOneOrMore(self)
            else:
                return visitor.visitChildren(self)



    def repetitionAmount(self):

        localctx = CQLParser.RepetitionAmountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repetitionAmount)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = CQLParser.RepetitionZeroOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(CQLParser.ASTERISK)
                pass

            elif la_ == 2:
                localctx = CQLParser.RepetitionOneOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(CQLParser.PLUS)
                pass

            elif la_ == 3:
                localctx = CQLParser.RepetitionZeroOrOneContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(CQLParser.QUESTION_MARK)
                pass

            elif la_ == 4:
                localctx = CQLParser.RepetitionExactlyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(CQLParser.LEFT_CURLY_BRACKET)
                self.state = 141
                self.match(CQLParser.NUMBER)
                self.state = 142
                self.match(CQLParser.LEFT_RIGHT_BRACKET)
                pass

            elif la_ == 5:
                localctx = CQLParser.RepetitionMinMaxContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(CQLParser.LEFT_CURLY_BRACKET)
                self.state = 144
                self.match(CQLParser.NUMBER)
                self.state = 145
                self.match(CQLParser.T__2)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 146
                    self.match(CQLParser.NUMBER)


                self.state = 149
                self.match(CQLParser.LEFT_RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTED_STRING(self):
            return self.getToken(CQLParser.DOUBLE_QUOTED_STRING, 0)

        def SINGLE_QUOTED_STRING(self):
            return self.getToken(CQLParser.SINGLE_QUOTED_STRING, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_quotedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedString" ):
                listener.enterQuotedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedString" ):
                listener.exitQuotedString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuotedString" ):
                return visitor.visitQuotedString(self)
            else:
                return visitor.visitChildren(self)




    def quotedString(self):

        localctx = CQLParser.QuotedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_quotedString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_booleanOperator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VERTICAL_LINE(self):
            return self.getToken(CQLParser.VERTICAL_LINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AMPERSAND(self):
            return self.getToken(CQLParser.AMPERSAND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication" ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication" ):
                listener.exitImplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication" ):
                return visitor.visitImplication(self)
            else:
                return visitor.visitChildren(self)



    def booleanOperator(self):

        localctx = CQLParser.BooleanOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_booleanOperator)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = CQLParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(CQLParser.AMPERSAND)
                pass
            elif token in [27]:
                localctx = CQLParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(CQLParser.VERTICAL_LINE)
                pass
            elif token in [4]:
                localctx = CQLParser.ImplicationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(CQLParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_valuePart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValuePartStringContext(ValuePartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.ValuePartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quotedString(self):
            return self.getTypedRuleContext(CQLParser.QuotedStringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuePartString" ):
                listener.enterValuePartString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuePartString" ):
                listener.exitValuePartString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuePartString" ):
                return visitor.visitValuePartString(self)
            else:
                return visitor.visitChildren(self)


    class ValuePartParenthesisedContext(ValuePartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.ValuePartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_PARENTHESIS(self):
            return self.getToken(CQLParser.LEFT_PARENTHESIS, 0)
        def value(self):
            return self.getTypedRuleContext(CQLParser.ValueContext,0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(CQLParser.RIGHT_PARENTHESIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuePartParenthesised" ):
                listener.enterValuePartParenthesised(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuePartParenthesised" ):
                listener.exitValuePartParenthesised(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuePartParenthesised" ):
                return visitor.visitValuePartParenthesised(self)
            else:
                return visitor.visitChildren(self)



    def valuePart(self):

        localctx = CQLParser.ValuePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_valuePart)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                localctx = CQLParser.ValuePartStringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.quotedString()
                pass
            elif token in [18]:
                localctx = CQLParser.ValuePartParenthesisedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(CQLParser.LEFT_PARENTHESIS)
                self.state = 161
                self.value()
                self.state = 162
                self.match(CQLParser.RIGHT_PARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CQLParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValueWithoutContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueWithout" ):
                listener.enterValueWithout(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueWithout" ):
                listener.exitValueWithout(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueWithout" ):
                return visitor.visitValueWithout(self)
            else:
                return visitor.visitChildren(self)


    class ValueWithContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CQLParser.ValuePartContext,0)

        def booleanOperator(self):
            return self.getTypedRuleContext(CQLParser.BooleanOperatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CQLParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueWith" ):
                listener.enterValueWith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueWith" ):
                listener.exitValueWith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueWith" ):
                return visitor.visitValueWith(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = CQLParser.ValueWithContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.valuePart()
                self.state = 167
                self.booleanOperator()
                self.state = 168
                self.value()
                pass

            elif la_ == 2:
                localctx = CQLParser.ValueWithoutContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.valuePart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





