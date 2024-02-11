# Generated from C:/PHD_Projects/TDD_Python_Example/Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,3,6,38,8,6,1,7,5,7,41,8,7,10,7,12,
        7,44,9,7,1,7,1,7,4,7,48,8,7,11,7,12,7,49,1,8,4,8,53,8,8,11,8,12,
        8,54,1,9,1,9,5,9,59,8,9,10,9,12,9,62,9,9,1,9,1,9,1,10,4,10,67,8,
        10,11,10,12,10,68,1,10,1,10,1,60,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,0,17,0,19,8,21,9,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,75,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,
        0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,37,
        1,0,0,0,15,42,1,0,0,0,17,52,1,0,0,0,19,56,1,0,0,0,21,66,1,0,0,0,
        23,24,5,43,0,0,24,2,1,0,0,0,25,26,5,45,0,0,26,4,1,0,0,0,27,28,5,
        42,0,0,28,6,1,0,0,0,29,30,5,47,0,0,30,8,1,0,0,0,31,32,5,40,0,0,32,
        10,1,0,0,0,33,34,5,41,0,0,34,12,1,0,0,0,35,38,3,15,7,0,36,38,3,17,
        8,0,37,35,1,0,0,0,37,36,1,0,0,0,38,14,1,0,0,0,39,41,7,0,0,0,40,39,
        1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,
        44,42,1,0,0,0,45,47,5,46,0,0,46,48,7,0,0,0,47,46,1,0,0,0,48,49,1,
        0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,16,1,0,0,0,51,53,7,0,0,0,52,
        51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,18,1,0,0,
        0,56,60,5,34,0,0,57,59,9,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,61,
        1,0,0,0,60,58,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,34,0,0,
        64,20,1,0,0,0,65,67,7,1,0,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,
        0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,6,10,0,0,71,22,1,0,0,0,7,
        0,37,42,49,54,60,68,1,6,0,0
    ]

class ArithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    LPAREN = 5
    RPAREN = 6
    NUMERICALVALUE = 7
    STRING = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "NUMERICALVALUE", 
            "STRING", "WS" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "NUMERICALVALUE", 
                  "FLOAT", "INTEGER", "STRING", "WS" ]

    grammarFileName = "Arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


