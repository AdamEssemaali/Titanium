from sly import Lexer

class TitaniumLexer(Lexer):
    tokens = {ID, EQ, NUMBER, PLUS, MINUS, POW, DIVIDE, ASSIGN, FUNCTION, RETURN}

    ignore = ' \t'
    ignore_comment = r'\\\\\.*'
    ignore_newline = r'\n+'
    
    @_('int')
    def INTEGER(self,token):
        token.type = "INT"
        return token
    literals = { '{', '}','(',')',':',';', '"', '\'' }
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    POW   = r'\*'
    DIVIDE  = r'/'
    EQ = r'=='
    ASSIGN  = r'='
    ID["func"] = FUNCTION
    ID["return"] = RETURN

    @_(r'\d+')
    def NUMBER(self,token):
        token.value = int(token.value)
        return token
