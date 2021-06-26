import foolscript as main

def run(fn, text):
    # Generate tokens
    lexer = main.Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = main.Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = main.Interpreter()
    context = main.Context('<program>')
    context.symbol_table = main.global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error


