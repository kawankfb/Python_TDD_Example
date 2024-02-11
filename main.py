import argparse
from antlr4 import *

from custom_listener import CustomListener
from Gen.ArithmeticLexer import ArithmeticLexer
from Gen.ArithmeticParser import ArithmeticParser


def main(arguments):

    stream = FileStream(arguments.file, encoding='utf8')
    lexer = ArithmeticLexer(stream)

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = ArithmeticParser(token_stream)
    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.start()

    # Create a custom listener object
    listener = CustomListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # Get the result from the Listener
    result = listener.result
    print(result)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = arg_parser.parse_args()
    main(args)
