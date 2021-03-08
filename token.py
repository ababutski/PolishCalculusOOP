class TokenType:
    NONE = -1
    NUMBER = 0
    OP_PLUS = 1
    OP_UNO_PLUS = 2
    OP_MINUS = 3
    OP_UNO_MINUS = 4
    OP_MULT = 5
    OP_DIV = 6
    OP_PAREHTESES_OPEN = 7 #openening parentheses
    OP_PAREHTESES_CLOSE = 8 #closing parentheses

class Token:
    def __init__(self, tokenType, value = 0):
        self.type = tokenType
        self.value = value
    
    def isnumber(self):
        return self.type == TokenType.NUMBER
    def isoperator(self):
        return (
            self.type == TokenType.OP_PLUS 
            or self.type == TokenType.OP_UNO_PLUS 
            or self.type == TokenType.OP_MINUS 
            or self.type == TokenType.OP_UNO_MINUS 
            or self.type == TokenType.OP_MULT 
            or self.type == TokenType.OP_DIV)
