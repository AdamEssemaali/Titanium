from Lexer.lexer import TitaniumLexer
from Parser.parser import TitaniumParser
from CodeBuilder.builder import TitaniumBuilder
import sys
from datetime import datetime
from Runner.runner import TitaniumRunner


if sys.argv[1] == "-b":
    data = open(sys.argv[2], "r").read()

    time0 = datetime.now()

    lex = TitaniumLexer()
    tokens = lex.tokenize(data)
    parser = TitaniumParser(tokens)
    codebuilder = TitaniumBuilder(parser.parse())
    codebuilder.build()
    TitaniumRunner(cfile="CACHE/output.cpp", output=sys.argv[3]).compile()
    end  = datetime.now()
    print(end - time0)
