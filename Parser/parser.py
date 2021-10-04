from AST.functionDeclaration import FunctionDeclaration
from AST.functioncallBlock import FunctionCallBlock
from AST.returnBlock import ReturnBlock
from AST.stringDeclaration import StringDeclaration
from AST.variableNode import VariabileNode
from Lexer.token import Token


class TitaniumParser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
    
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
                node = FunctionDeclaration("","","")
                args = {}
                i += 1

                if tokens[i].type == "ID":
                    node.name = tokens[i].value
                    i += 1
                    
                    if tokens[i].type == "(":
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

            if tokens[i].type == "STRING":
                node = StringDeclaration(tokens[i].type)
                nodes.append(node)

            elif tokens[i].type == "{":
                nodes.append("NewScope")


            elif tokens[i].type == "}":
                nodes.append("EndScope")

            elif tokens[i].type == "(":
                nodes.append(tokens[i].type)

            elif tokens[i].type == ")":
                nodes.append(tokens[i].type)

            elif tokens[i].type == "RETURN":
                node = ReturnBlock("")
                i += 1
                node.value = tokens[i].value
                nodes.append(node)

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