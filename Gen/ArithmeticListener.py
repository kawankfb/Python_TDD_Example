# Generated from C:/PHD_Projects/TDD_Python_Example/Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#start.
    def enterStart(self, ctx:ArithmeticParser.StartContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#start.
    def exitStart(self, ctx:ArithmeticParser.StartContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#expr_add_term.
    def enterExpr_add_term(self, ctx:ArithmeticParser.Expr_add_termContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expr_add_term.
    def exitExpr_add_term(self, ctx:ArithmeticParser.Expr_add_termContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#negative_term.
    def enterNegative_term(self, ctx:ArithmeticParser.Negative_termContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#negative_term.
    def exitNegative_term(self, ctx:ArithmeticParser.Negative_termContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#expr_is_term.
    def enterExpr_is_term(self, ctx:ArithmeticParser.Expr_is_termContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expr_is_term.
    def exitExpr_is_term(self, ctx:ArithmeticParser.Expr_is_termContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#positive_term.
    def enterPositive_term(self, ctx:ArithmeticParser.Positive_termContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#positive_term.
    def exitPositive_term(self, ctx:ArithmeticParser.Positive_termContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#expr_sub_term.
    def enterExpr_sub_term(self, ctx:ArithmeticParser.Expr_sub_termContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expr_sub_term.
    def exitExpr_sub_term(self, ctx:ArithmeticParser.Expr_sub_termContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term_div_factor.
    def enterTerm_div_factor(self, ctx:ArithmeticParser.Term_div_factorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term_div_factor.
    def exitTerm_div_factor(self, ctx:ArithmeticParser.Term_div_factorContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term_is_factor.
    def enterTerm_is_factor(self, ctx:ArithmeticParser.Term_is_factorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term_is_factor.
    def exitTerm_is_factor(self, ctx:ArithmeticParser.Term_is_factorContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term_mul_factor.
    def enterTerm_mul_factor(self, ctx:ArithmeticParser.Term_mul_factorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term_mul_factor.
    def exitTerm_mul_factor(self, ctx:ArithmeticParser.Term_mul_factorContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor_is_numerical.
    def enterFactor_is_numerical(self, ctx:ArithmeticParser.Factor_is_numericalContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor_is_numerical.
    def exitFactor_is_numerical(self, ctx:ArithmeticParser.Factor_is_numericalContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor_is_expression.
    def enterFactor_is_expression(self, ctx:ArithmeticParser.Factor_is_expressionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx:ArithmeticParser.Factor_is_expressionContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor_is_string.
    def enterFactor_is_string(self, ctx:ArithmeticParser.Factor_is_stringContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor_is_string.
    def exitFactor_is_string(self, ctx:ArithmeticParser.Factor_is_stringContext):
        pass



del ArithmeticParser