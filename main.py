import sys
from token import *
from rp_calc import *
from rp_parser import *

OPERATORS = {
        TokenType.OP_PLUS:'+',
        TokenType.OP_MINUS:'-',
        TokenType.OP_MULT:'*',
        TokenType.OP_DIV:'/',
        TokenType.OP_UNO_MINUS: '-u',
        TokenType.OP_UNO_PLUS: '+u'
        }

def tokenToString(token):
    if token.isnumber():
        return str(token.value)
    elif token.isoperator():
        return OPERATORS[token.type]
    return ""
# reading arguments as single string
line = ''.join(sys.argv[1:])
# removing whitespaces from string
#line = '1+2*3*(2+10)'

rpn = ReversePolishParser().parse(line)
print(' '.join(map(tokenToString,rpn)))

result = ReversePolishCalculator().calculate(rpn)
print(result)