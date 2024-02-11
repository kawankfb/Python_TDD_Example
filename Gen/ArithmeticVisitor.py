# Generated from C:/PHD_Projects/TDD_Python_Example/Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticParser.

class ArithmeticVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticParser#start.
    def visitStart(self, ctx:ArithmeticParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#expr_add_term.
    def visitExpr_add_term(self, ctx:ArithmeticParser.Expr_add_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#negative_term.
    def visitNegative_term(self, ctx:ArithmeticParser.Negative_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#expr_is_term.
    def visitExpr_is_term(self, ctx:ArithmeticParser.Expr_is_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#positive_term.
    def visitPositive_term(self, ctx:ArithmeticParser.Positive_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#expr_sub_term.
    def visitExpr_sub_term(self, ctx:ArithmeticParser.Expr_sub_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#term_div_factor.
    def visitTerm_div_factor(self, ctx:ArithmeticParser.Term_div_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#term_is_factor.
    def visitTerm_is_factor(self, ctx:ArithmeticParser.Term_is_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#term_mul_factor.
    def visitTerm_mul_factor(self, ctx:ArithmeticParser.Term_mul_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#factor_is_numerical.
    def visitFactor_is_numerical(self, ctx:ArithmeticParser.Factor_is_numericalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#factor_is_expression.
    def visitFactor_is_expression(self, ctx:ArithmeticParser.Factor_is_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#factor_is_string.
    def visitFactor_is_string(self, ctx:ArithmeticParser.Factor_is_stringContext):
        return self.visitChildren(ctx)



del ArithmeticParser