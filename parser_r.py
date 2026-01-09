import ply.yacc as yacc
from lexer_r import tokens

# ======================
# Grammar Rules
# ======================

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_print(p):
    '''statement : PRINT LPAREN STRING RPAREN'''
    p[0] = ('print', p[3])

def p_statement_cat(p):
    '''statement : CAT LPAREN STRING RPAREN'''
    p[0] = ('cat', p[3])

def p_error(p):
    raise Exception("Syntax Error")

parser = yacc.yacc()
