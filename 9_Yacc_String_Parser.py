import ply.lex as lex
import ply.yacc as yacc

# Define tokens (remove 'E' from the list)
tokens = ('I', 'B', 'T', 'A')

literals = "ibtea"  # Define literals directly

# Token definitions
def t_I(t):
    r'i'
    return t

def t_B(t):
    r'b'
    return t

def t_T(t):
    r't'
    return t

def t_A(t):
    r'a'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules
def p_S_rule1(p):
    """S : I E T S S_prime
         | A"""
    pass

def p_S_prime_rule(p):
    """S_prime : E S
               | """  # epsilon
    pass

def p_E_rule(p):
    """E : B"""
    pass

def p_error(p):
    print("Invalid string")
    exit(0)

parser = yacc.yacc()

# Test cases
inputs = ["ibtai", "ibtaea", "a", "ibtibta", "ibtaeibta", "ibti", "ibtaa", "iea", "ibtb", "ibtibt"]

for test in inputs:
    try:
        parser.parse(test)
        print(f"{test}: Valid string")
    except SystemExit:
        print(f"{test}: Invalid string")
