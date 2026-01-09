import ply.lex as lex

# ======================
# Token List
# ======================
tokens = (
    'PRINT',
    'CAT',
    'STRING',
    'LPAREN',
    'RPAREN'
)

# ======================
# Token Regex Rules
# ======================
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

# ======================
# Reserved Words
# ======================
reserved = {
    'print': 'PRINT',
    'cat': 'CAT'
}

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]   # remove quotes
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_error(t):
    raise Exception(f"Illegal character '{t.value[0]}'")

lexer = lex.lex()
