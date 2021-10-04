from sly import Lexer
import colorama
colorama.init()
class TitaniumLexer(Lexer):
    tokens = {ID,EQ, NUMBER, PLUS, MINUS, TIMES, DIVIDE, ASSIGN, FUNCTION, RETURN, VAR, STRING}

    ignore = ' \t'
    ignore_comment = r'\\\\\.*'
    ignore_newline = r'\n+'

    def error(self, token):
        print(f"""{colorama.Fore.RED}Error{colorama.Fore.WHITE}: Illegal character\nTriggered here: ({colorama.Fore.GREEN}{token.lineno},{token.index}{colorama.Fore.WHITE}): \"{colorama.Fore.GREEN}{token.value[0]}{colorama.Fore.WHITE}\" """)
        self.index += 1
        exit(1)

    @_('int')
    def INTEGER(self,token):
        token.type = "INT"
        return token

    @_('float')
    def FLOAT(self,token):
        token.type = 'FLOAT'
        return token

    @_(r'\d+')
    def NUMBER(self,token):
        token.value = int(token.value)
        return token
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    literals = { '{', '}','(',')',':',';', '"', '\'', '[', ']',  ',','.'}
    STRING = r'\".+\"'
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ = r'=='
    ASSIGN  = r'='
    
    ID["func"] = FUNCTION
    ID["return"] = RETURN
    ID["var"] = VAR
