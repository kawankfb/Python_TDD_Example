# Generated from C:/PHD_Projects/TDD_Python_Example/Arithmetic.g4 by ANTLR 4.13.1
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
        4,1,9,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,18,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,10,1,12,
        1,29,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,2,12,
        2,43,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,3,0,2,2,4,4,0,2,4,
        6,0,0,56,0,8,1,0,0,0,2,17,1,0,0,0,4,30,1,0,0,0,6,50,1,0,0,0,8,9,
        3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,6,1,-1,0,12,18,3,4,2,0,13,
        14,5,2,0,0,14,18,3,4,2,0,15,16,5,1,0,0,16,18,3,4,2,0,17,11,1,0,0,
        0,17,13,1,0,0,0,17,15,1,0,0,0,18,27,1,0,0,0,19,20,10,2,0,0,20,21,
        5,1,0,0,21,26,3,4,2,0,22,23,10,1,0,0,23,24,5,2,0,0,24,26,3,4,2,0,
        25,19,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,3,1,0,0,0,29,27,1,0,0,0,30,31,6,2,-1,0,31,32,3,6,3,0,32,
        41,1,0,0,0,33,34,10,2,0,0,34,35,5,3,0,0,35,40,3,6,3,0,36,37,10,1,
        0,0,37,38,5,4,0,0,38,40,3,6,3,0,39,33,1,0,0,0,39,36,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,
        51,5,7,0,0,45,46,5,5,0,0,46,47,3,2,1,0,47,48,5,6,0,0,48,51,1,0,0,
        0,49,51,5,8,0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,49,1,0,0,0,51,7,1,
        0,0,0,6,17,25,27,39,41,50
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "LPAREN", 
                      "RPAREN", "NUMERICALVALUE", "STRING", "WS" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "start", "expr", "term", "factor" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    LPAREN=5
    RPAREN=6
    NUMERICALVALUE=7
    STRING=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ArithmeticParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ArithmeticParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(ArithmeticParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Expr_add_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)

        def ADD(self):
            return self.getToken(ArithmeticParser.ADD, 0)
        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_add_term" ):
                listener.enterExpr_add_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_add_term" ):
                listener.exitExpr_add_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_add_term" ):
                return visitor.visitExpr_add_term(self)
            else:
                return visitor.visitChildren(self)


    class Negative_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(ArithmeticParser.SUB, 0)
        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative_term" ):
                listener.enterNegative_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative_term" ):
                listener.exitNegative_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative_term" ):
                return visitor.visitNegative_term(self)
            else:
                return visitor.visitChildren(self)


    class Expr_is_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_is_term" ):
                listener.enterExpr_is_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_is_term" ):
                listener.exitExpr_is_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_is_term" ):
                return visitor.visitExpr_is_term(self)
            else:
                return visitor.visitChildren(self)


    class Positive_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(ArithmeticParser.ADD, 0)
        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositive_term" ):
                listener.enterPositive_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositive_term" ):
                listener.exitPositive_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositive_term" ):
                return visitor.visitPositive_term(self)
            else:
                return visitor.visitChildren(self)


    class Expr_sub_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)

        def SUB(self):
            return self.getToken(ArithmeticParser.SUB, 0)
        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_sub_term" ):
                listener.enterExpr_sub_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_sub_term" ):
                listener.exitExpr_sub_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_sub_term" ):
                return visitor.visitExpr_sub_term(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7, 8]:
                localctx = ArithmeticParser.Expr_is_termContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.term(0)
                pass
            elif token in [2]:
                localctx = ArithmeticParser.Negative_termContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(ArithmeticParser.SUB)
                self.state = 14
                self.term(0)
                pass
            elif token in [1]:
                localctx = ArithmeticParser.Positive_termContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(ArithmeticParser.ADD)
                self.state = 16
                self.term(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticParser.Expr_add_termContext(self, ArithmeticParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(ArithmeticParser.ADD)
                        self.state = 21
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticParser.Expr_sub_termContext(self, ArithmeticParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 23
                        self.match(ArithmeticParser.SUB)
                        self.state = 24
                        self.term(0)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Term_div_factorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)

        def DIV(self):
            return self.getToken(ArithmeticParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_div_factor" ):
                listener.enterTerm_div_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_div_factor" ):
                listener.exitTerm_div_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_div_factor" ):
                return visitor.visitTerm_div_factor(self)
            else:
                return visitor.visitChildren(self)


    class Term_is_factorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_is_factor" ):
                listener.enterTerm_is_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_is_factor" ):
                listener.exitTerm_is_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_is_factor" ):
                return visitor.visitTerm_is_factor(self)
            else:
                return visitor.visitChildren(self)


    class Term_mul_factorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)

        def MUL(self):
            return self.getToken(ArithmeticParser.MUL, 0)
        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_mul_factor" ):
                listener.enterTerm_mul_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_mul_factor" ):
                listener.exitTerm_mul_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_mul_factor" ):
                return visitor.visitTerm_mul_factor(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ArithmeticParser.Term_is_factorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 31
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticParser.Term_mul_factorContext(self, ArithmeticParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(ArithmeticParser.MUL)
                        self.state = 35
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticParser.Term_div_factorContext(self, ArithmeticParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 36
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 37
                        self.match(ArithmeticParser.DIV)
                        self.state = 38
                        self.factor()
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Factor_is_stringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ArithmeticParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_string" ):
                listener.enterFactor_is_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_string" ):
                listener.exitFactor_is_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_string" ):
                return visitor.visitFactor_is_string(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_expressionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_expression" ):
                listener.enterFactor_is_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_expression" ):
                listener.exitFactor_is_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_expression" ):
                return visitor.visitFactor_is_expression(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_numericalContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERICALVALUE(self):
            return self.getToken(ArithmeticParser.NUMERICALVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_numerical" ):
                listener.enterFactor_is_numerical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_numerical" ):
                listener.exitFactor_is_numerical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_numerical" ):
                return visitor.visitFactor_is_numerical(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ArithmeticParser.Factor_is_numericalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(ArithmeticParser.NUMERICALVALUE)
                pass
            elif token in [5]:
                localctx = ArithmeticParser.Factor_is_expressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(ArithmeticParser.LPAREN)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(ArithmeticParser.RPAREN)
                pass
            elif token in [8]:
                localctx = ArithmeticParser.Factor_is_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(ArithmeticParser.STRING)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




