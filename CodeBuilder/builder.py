from AST.functionDeclaration import FunctionDeclaration
from AST.functioncallBlock import FunctionCallBlock
from AST.returnBlock import ReturnBlock
from AST.stringDeclaration import StringDeclaration
from AST.variableNode import VariabileNode


class TitaniumBuilder:
    final_code = """#include \"stdlib\\io.hpp\" \n #include <stdbool.h>\n"""
    indent = 0

    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def new_line(self):
        self.final_code += "\n"
        for i in range(self.indent):
            self.final_code += "\t"

    def build(self):
        for node in self.nodes:
            if type(node) == FunctionDeclaration:
                self.final_code += f"{node.type} {node.name}("
                has_args = False

                for arg in node.args:
                    self.final_code += f"{node.args[arg]} {arg}, "
                    has_args = True
                
                if has_args:
                    _string = list(self.final_code)
                    _string.pop(len(_string) - 1)
                    _string.pop(len(_string) - 1)
                    self.final_code = "".join(_string)

                self.final_code += ")"

            if node == "NewScope":
                self.final_code += "{"
                self.indent += 1
                self.new_line()
            

            if node == "EndScope":
                self.indent -= 1
                self.new_line()
                self.final_code += "}"
                self.new_line()

            if type(node) == ReturnBlock:
                self.final_code += f"return {node.value};"
                self.new_line()
            
            if type(node) == VariabileNode:
                self.final_code += f"{node.type} {node.name} = {node.value};"
                self.new_line()
            
            if type(node) == FunctionCallBlock:
                self.final_code += f"{node.name}("
                for arg in node.args:
                    self.final_code += f"{node.args[arg]}"
                
                self.final_code += f");"
                self.new_line()

            if type(node) == StringDeclaration:
                self.final_code += f"\"{node}\""



        open("output.cpp", "w").write(self.final_code)
