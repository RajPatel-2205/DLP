import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'LPAREN', 'RPAREN')

# Token regex rules
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER   = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Number token (integer or float)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)  # Convert to float
    return t

# Ignore whitespace
t_ignore = ' \t'

# Handle lexical errors
def t_error(t):
    print("Invalid expression")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Parsing rules

def p_expression_add_sub(p):
    """E : E PLUS T
         | E MINUS T"""
    p[0] = p[1] + p[3] if p[2] == '+' else p[1] - p[3]

def p_expression_term(p):
    """E : T"""
    p[0] = p[1]

def p_term_mult_div(p):
    """T : T TIMES F
         | T DIVIDE F"""
    p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]

def p_term_factor(p):
    """T : F"""
    p[0] = p[1]

def p_factor_exponentiation(p):
    """F : G POWER F"""
    p[0] = p[1] ** p[3]

def p_factor_group(p):
    """F : G"""
    p[0] = p[1]

def p_group_parentheses(p):
    """G : LPAREN E RPAREN"""
    p[0] = p[2]

def p_group_number(p):
    """G : NUMBER"""
    p[0] = p[1]

def p_error(p):
    print("Invalid expression")
    exit(0)

# Build parser
parser = yacc.yacc()

# Test cases
expressions = [
    "(3 + 5) * 2 ^ 3",
    "3 + 5 * 2",
    "3 + 5 * 2 ^ 2",
    "3 + (5 * 2)",
    "3 + 5 ^ 2 * 2",
    "3 * (5 + 2)",
    "(3 + 5) ^ 2",
    "3 ^ 2 ^ 3",
    "3 ^ 2 + 5 * 2",
    "3 + ^ 5",  # Invalid
    "(3 + 5 * 2",
    "(3 + 5 * 2 ^ 2 - 8) / 4 ^ 2 + 6"
]

for expr in expressions:
    try:
        result = parser.parse(expr)
        print(f"{expr} = {result}")
    except SystemExit:
        print(f"{expr} = Invalid expression")
