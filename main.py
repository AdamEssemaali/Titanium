from Lexer.lexer import TitaniumLexer
from Parser.parser import TitaniumParser
from CodeBuilder.builder import TitaniumBuilder
import sys
from datetime import datetime
from Runner.runner import TitaniumRunner

data = open("Tests/syntax.ti", "r").read()

time0 = datetime.now()

lex = TitaniumLexer()
tokens = lex.tokenize(data)

print(tokens)

#parser = TitaniumParser(tokens)
#codebuilder = TitaniumBuilder(parser.parse())
#codebuilder.build()
end  = datetime.now()
print(end - time0)
