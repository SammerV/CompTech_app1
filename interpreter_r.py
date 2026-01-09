class Interpreter:
    def run(self, ast):
        for stmt in ast:
            if stmt[0] == 'print':
                print(stmt[1])
            elif stmt[0] == 'cat':
                print(stmt[1])
