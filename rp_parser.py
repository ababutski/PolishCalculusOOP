from token import *

class ReversePolishParser:
    # dictionary with operators(keys) and their priority (values)
    _OPERATORS = {
        TokenType.OP_PLUS:0,
        TokenType.OP_MINUS:0,
        TokenType.OP_MULT:1,
        TokenType.OP_DIV:1,
        TokenType.OP_UNO_MINUS: 2,
        TokenType.OP_UNO_PLUS: 2,
        TokenType.OP_PAREHTESES_OPEN: -1,
        TokenType.OP_PAREHTESES_CLOSE: -1
        }
    
    _OPERATOR_TYPES = {
        '+':TokenType.OP_PLUS,
        '-':TokenType.OP_MINUS,
        '*':TokenType.OP_MULT,
        '/':TokenType.OP_DIV, 
        '(':TokenType.OP_PAREHTESES_OPEN,
        ')':TokenType.OP_PAREHTESES_CLOSE}

    # creating Reverse Polish notation
    # returns list with tokens. Each token is a string with number or operator.
    def parse(self, str):
        tokens = self._parse_tokens(str)
        result = []
        stack = []
        # iterate over string characters
        for i,token in enumerate(tokens):
            # if it's number
            if token.isnumber():
                result.append(token)
            # if it's openening parentheses
            elif token.type == TokenType.OP_PAREHTESES_OPEN:
                stack.append(token)
            # if it's closing parentheses
            elif token.type == TokenType.OP_PAREHTESES_CLOSE:
                # then moving tokens from stack to result until we meet opening parentheses
                t = stack.pop()
                while t.type != TokenType.OP_PAREHTESES_OPEN:
                    result.append(t)
                    t = stack.pop()
            # if it's operator
            elif token.isoperator():
                # taking priority of current operator
                p0 = self._OPERATORS[token.type]
                # moving tokens from stack to result while operators in stack have same or higher priority
                while len(stack) > 0:
                    t1 = stack.pop()
                    p1 = self._OPERATORS[t1.type]
                    if p1 >= p0:
                        result.append(t1)
                    # returning token back to stack and exiting cycle
                    else:
                        stack.append(t1)
                        break
                # finaly adding current token to stack
                stack.append(token)
        # moving tokens left in stack to result
        stack.reverse()
        for token in stack:
            if (token.type == TokenType.OP_PAREHTESES_OPEN 
            or token.type == TokenType.OP_PAREHTESES_CLOSE):
                raise SyntaxError('not paired parentheses in expression!')
            result.append(token)
        return result
    
    def _parse_tokens(self,str):
        result = []
        stack = []
        # iterate over string characters
        for i,token in enumerate(str):
            # if it's digit
            if token.isdigit():
                # if previous token was a number adding this digit to it
                if i > 0 and result[-1].isnumber():
                    result[-1].value = result[-1].value*10 + float(token)
                # otherwise add as new
                else:
                    result.append(Token(TokenType.NUMBER,float(token)))
            # if it's operator
            elif token in self._OPERATOR_TYPES:
                t = Token(self._OPERATOR_TYPES[token])
                # if prevouse token in input was NOT a digit then current token is unary operator
                if i==0 or result[-1].isnumber() == False:
                    # mark as unary
                    if token == '-':
                        t.type = TokenType.OP_UNO_MINUS
                    elif token == '+':
                        t.type = TokenType.OP_UNO_PLUS
                # taking priority of current operator
                result.append(t)
        return result


    