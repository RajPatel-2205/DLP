import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

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

# Ignore whitespace
t_ignore = ' \t'

# Handle lexical errors
def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Quadruple storage
quadruples = []
temp_count = 1  # Temporary variable counter

def new_temp():
    global temp_count
    temp_var = f"t{temp_count}"
    temp_count += 1
    return temp_var

# Parsing rules

def p_expression_plus_minus(p):
    """E : E PLUS T
         | E MINUS T"""
    temp_var = new_temp()
    quadruples.append((p[2], p[1], p[3], temp_var))
    p[0] = temp_var

def p_expression_term(p):
    """E : T"""
    p[0] = p[1]

def p_term_times_div(p):
    """T : T TIMES F
         | T DIVIDE F"""
    temp_var = new_temp()
    quadruples.append((p[2], p[1], p[3], temp_var))
    p[0] = temp_var

def p_term_factor(p):
    """T : F"""
    p[0] = p[1]

def p_factor_group(p):
    """F : LPAREN E RPAREN"""
    p[0] = p[2]

def p_factor_number(p):
    """F : NUMBER"""
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")
    exit(0)

# Build parser
parser = yacc.yacc()

# Function to process expression and generate quadruples
def generate_quadruples(expression):
    global quadruples, temp_count
    quadruples = []  # Reset quadruples list
    temp_count = 1   # Reset temp variable counter

    result = parser.parse(expression)
    
    print("\nQuadruple Representation:")
    print("{:<8} {:<10} {:<10} {:<10}".format("Operator", "Operand 1", "Operand 2", "Result"))
    print("-" * 40)
    for quad in quadruples:
        print("{:<8} {:<10} {:<10} {:<10}".format(quad[0], str(quad[1]), str(quad[2]), quad[3]))

# Test cases
expressions = [
    "9 + 42 * 8",
    "5 + 6 - 3",
    "7 - (8 * 2)",
    "(9 - 3) + (5 * 4 / 2)",
    "(3 + 5 * 2 - 8) / 4 - 2 + 6",
    "86 / 2 / 3"
]

for expr in expressions:
    print(f"\nExpression: {expr}")
    generate_quadruples(expr)
