from Lexer.lexer import TitaniumLexer

data = """
func main(): int{
    return 0;
}
"""
lex = TitaniumLexer()
for tok in lex.tokenize(data):
    print(f"{tok.type}:{tok.value}")