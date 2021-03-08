from token import *

class ReversePolishCalculator:
    _OPERATORS = {
        TokenType.OP_PLUS:float.__add__,
        TokenType.OP_MINUS:float.__sub__,
        TokenType.OP_MULT:float.__mul__,
        TokenType.OP_DIV:float.__div__
        }
    # Calculates expression in Reverse Polish notation. 
    # Returns number
    def calculate(self, tokens):
        stack = []
        for token in tokens:
            if token.isnumber():
                stack.append(token.value)
            elif token.type == TokenType.OP_UNO_MINUS:
                arg0 = stack.pop()
                stack.append(-arg0)
            elif token.isoperator():
                arg0, arg1 = stack.pop(), stack.pop()
                stack.append(self._OPERATORS[token.type](arg0,arg1))
            # for token == 'u+'  do nothing
        return stack.pop()