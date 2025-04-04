import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = ('NUMBER', 'VARIABLE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

# Token regex rules
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Number token (integer or float)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)  # Convert to float
    return t

# Variable token (letters only)
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignore whitespace
t_ignore = ' \t'

# Handle lexical errors
def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Parsing rules

def p_expression_binop(p):
    """E : E PLUS T
         | E MINUS T"""
    if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
        p[0] = p[1] + p[3] if p[2] == '+' else p[1] - p[3]  # Constant folding
    else:
        p[0] = f"({p[1]} {p[2]} {p[3]})" if isinstance(p[1], str) or isinstance(p[3], str) else p[1]

def p_expression_term(p):
    """E : T"""
    p[0] = p[1]

def p_term_binop(p):
    """T : T TIMES F
         | T DIVIDE F"""
    if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
        p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]  # Constant folding
    else:
        p[0] = f"({p[1]} {p[2]} {p[3]})" if isinstance(p[1], str) or isinstance(p[3], str) else p[1]

def p_term_factor(p):
    """T : F"""
    p[0] = p[1]

def p_factor_group(p):
    """F : LPAREN E RPAREN"""
    p[0] = p[2]

def p_factor_number(p):
    """F : NUMBER"""
    p[0] = p[1]

def p_factor_variable(p):
    """F : VARIABLE"""
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")
    exit(0)

# Build parser
parser = yacc.yacc()

# Function to optimize expression using constant folding
def optimize_expression(expression):
    result = parser.parse(expression)
    print(f"Optimized Expression: {result}")

# Test cases
expressions = [
    "5 + x - 3 * 2",
    "2 + 3 * 4 - 1",
    "x + (3 * 5) - 2",
    "(22 / 7) * r * r"
]

for expr in expressions:
    print(f"\nOriginal Expression: {expr}")
    optimize_expression(expr)
