import sys
from parser_r import parser
from interpreter_r import Interpreter

def main():
    with open(sys.argv[1]) as f:
        code = f.read()

    ast = parser.parse(code)
    interpreter = Interpreter()
    interpreter.run(ast)

if __name__ == "__main__":
    main()
