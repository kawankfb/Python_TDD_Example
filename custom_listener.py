from Gen.ArithmeticListener import ArithmeticListener
from Gen.ArithmeticParser import ArithmeticParser
from calculator import Calculator


class CustomListener(ArithmeticListener):
    def __init__(self):
        self.result = 0
        self.calculator = Calculator()

    def exitStart(self, ctx: ArithmeticParser.StartContext):
        ctx.value = ctx.getChild(0).value
        self.result = ctx.value

    # Exit a parse tree produced by ArithmeticParser#expr_add_term.
    def exitExpr_add_term(self, ctx: ArithmeticParser.Expr_add_termContext):
        ctx.value = self.calculator.add(ctx.getChild(0).value, ctx.getChild(2).value)

    # Exit a parse tree produced by ArithmeticParser#negative_term.
    def exitNegative_term(self, ctx: ArithmeticParser.Negative_termContext):
        ctx.value = self.calculator.mul(-1, ctx.getChild(1).value)

    # Exit a parse tree produced by ArithmeticParser#expr_is_term.
    def exitExpr_is_term(self, ctx: ArithmeticParser.Expr_is_termContext):
        ctx.value = ctx.getChild(0).value

    # Exit a parse tree produced by ArithmeticParser#positive_term.
    def exitPositive_term(self, ctx: ArithmeticParser.Positive_termContext):
        ctx.value = ctx.getChild(1).value

    # Exit a parse tree produced by ArithmeticParser#expr_sub_term.
    def exitExpr_sub_term(self, ctx: ArithmeticParser.Expr_sub_termContext):
        ctx.value = self.calculator.sub(ctx.getChild(0).value, ctx.getChild(2).value)

    # Exit a parse tree produced by ArithmeticParser#term_div_factor.
    def exitTerm_div_factor(self, ctx: ArithmeticParser.Term_div_factorContext):
        ctx.value = self.calculator.div(ctx.getChild(0).value, ctx.getChild(2).value)

    # Exit a parse tree produced by ArithmeticParser#term_is_factor.
    def exitTerm_is_factor(self, ctx: ArithmeticParser.Term_is_factorContext):
        ctx.value = ctx.getChild(0).value

    # Exit a parse tree produced by ArithmeticParser#term_mul_factor.
    def exitTerm_mul_factor(self, ctx: ArithmeticParser.Term_mul_factorContext):
        ctx.value = self.calculator.mul(ctx.getChild(0).value, ctx.getChild(2).value)

    # Exit a parse tree produced by ArithmeticParser#factor_is_numerical.
    def exitFactor_is_numerical(self, ctx: ArithmeticParser.Factor_is_numericalContext):
        number = ctx.NUMERICALVALUE().getText()
        if number.count('.') == 1:
            ctx.value = float(number)
        elif number.isnumeric():
            ctx.value = int(number)

    # Exit a parse tree produced by ArithmeticParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx: ArithmeticParser.Factor_is_expressionContext):
        ctx.value = ctx.getChild(1).value

    # Exit a parse tree produced by ArithmeticParser#factor_is_string.
    def exitFactor_is_string(self, ctx: ArithmeticParser.Factor_is_stringContext):
        ctx.value = str(ctx.STRING().getText().replace('\"', ''))
