from AST.functionDeclaration import FunctionDeclaration
from AST.functioncallBlock import FunctionCallBlock
from AST.returnBlock import ReturnBlock
from AST.stringDeclaration import StringDeclaration
from AST.variableNode import VariabileNode
from Lexer.token import Token

# cogno è stato qui
class TitaniumParser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
    
    def is_open_bracket(self, tokens, i, nodes, node):
        args = {}
        i += 1

        while tokens[i].type != ')':
            temp = []
            if tokens[i].type == 'ID':
                temp.append(tokens[i].value)
            i+= 1
            if tokens[i].type == ":":
                i += 1
                args.__setitem__(temp[0], tokens[i].value)
            
        node.args = args

        i += 1
        if tokens[i].type == ":":
            i += 1
            node.type = tokens[i].value
            nodes.append(node)
    
    def step(self, tokens, i, nodes, node, type):
        i += 1
        
        if tokens[i].type == type:
            self.is_open_bracket(tokens, i, nodes, node)
    
    def is_id(self, tokens, i, nodes, node):
        node.name = tokens[i].value
        self.step(tokens, i, nodes, node, "(")
    
    def is_function(self, tokens, i, nodes):
        node = FunctionDeclaration("","","")
        self.step(tokens, i, nodes, node, "ID")
    
    def is_string(self, tokens, i, nodes):
        node = StringDeclaration(tokens[i].type)
        nodes.append(node)
    
    def is_return(self, tokens, i, nodes):
        node = ReturnBlock("")
        i += 1
        node.value = tokens[i].value
        nodes.append(node)
    
    def parse(self):
        i = 0
        tokens = []
        nodes = []

        for tok in self.tokens:
            tok = Token(index=tok.index, value=tok.value, ztype=tok.type, line=tok.lineno)
            if tok.value == "string":
                tok.value = "char*"
            tokens.append(tok)
        
        while i < len(tokens):
            if tokens[i].type == "FUNCTION":
                self.is_function(tokens, i, nodes)

            if tokens[i].type == "STRING":
                self.is_string(tokens, i, nodes)

            elif tokens[i].type == "{":
                nodes.append("NewScope")

            elif tokens[i].type == "}":
                nodes.append("EndScope")

            elif tokens[i].type == "(":
                nodes.append(tokens[i].type)

            elif tokens[i].type == ")":
                nodes.append(tokens[i].type)

            elif tokens[i].type == "RETURN":
                self.is_return(tokens, i, nodes)

            elif tokens[i].type == "VAR":
                i += 1
                node = VariabileNode("","","")
                if tokens[i].type == "ID":
                    node.name = tokens[i].value
                    i += 1
                    if tokens[i].type == ":":
                        i += 1
                        node.type = tokens[i].value
                        i += 1
                        if tokens[i].type == "ASSIGN":
                            i += 1
                            node.value = tokens[i].value
                nodes.append(node)

            elif tokens[i].type == "ID":
                node = FunctionCallBlock("",{})
                print(f"Trovato un ID : {tokens[i].value}")
                node.name = tokens[i].value
                i += 1
                if tokens[i].type == "(":
                    i += 1
                    while tokens[i].type != ')':
                        temp = []
                        print(tokens[i].type)
                        temp.append(tokens[i].value)
                        
                        node.args.__setitem__(temp[0], tokens[i].value)
                        i+= 1
                print(node.args)
                nodes.append(node)
                    
            i += 1

        return nodes