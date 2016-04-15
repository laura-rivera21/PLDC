import ply.lex as lex

# PLDClex.py - tokenizer

# list of tokens names
tokens = ('POLT',
          'POLS',
          'LAPLACE',
          'SHOW',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'LPAREN',
          'RPAREN',
          'RAISED',
          'VART',
          'VARS',
          'EQUALS')

# reserved words
reserved = {
            'show':'SHOW',
            'laplace':'LAPLACE',
}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RAISED = r'\^'
t_LAPLACE = r'(?i)laplace'
t_SHOW = r'(?i)show'
t_POLT = r'([A-Za-z]+[0-9]*)+'
t_POLS = r'/([A-Za-z]+[0-9]*)+'
t_VART = r't'
t_VARS = r's'
t_EQUALS = r'='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

# Ignore strings starting with # (comments)
t_ignore_COMMENT = r'\#.*'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''polynom = 9s^3+3s+61'''

# Give the lexer some input
lexer.input(data)

# Tokenize
#while True:
tok = lexer.token()
   # if not tok:
   #     break      # No more input
    #print(tok.type, tok.value)

# Yacc test

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
#from PLDClex import tokens

############EXPRESSION###############
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = str(p[1]) + '+' + str(p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = str(p[1]) + '-' + str(p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = str(p[1])

##############TERM##################
def p_term_times(p):
    'term : factor variable'
    p[0] = str(p[1]) + str(p[2])

def p_term_times_2(p):
    'term : factor TIMES variable RAISED factor'
    p[0] = str(p[1]) + '*' + str(p[3]) + '^' + str(p[5])

def p_term_var_exp(p):
    'term : variable RAISED factor'
    p[0] = str(p[1]) + '^' + str(p[3])

def p_term_var(p):
    'term : variable'
    p[0] = str(p[1])

def p_term_fac(p):
    'term : factor'
    p[0] = str(p[1])

##############FACTOR################
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = str(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = '(' + str(p[2]) + ')'

#############VARIABLE###############
def p_variable_t(p):
    'variable : VART'
    p[0] = str(p[1])

def p_variable_s(p):
    'variable : VARS'
    p[0] = str(p[1])

#############EXPONENT###############
def p_exponent(p):
    'exponent : NUMBER'
    p[0] = str(p[1])

#############FUNCTION###############
def p_function(p):
    'function : LAPLACE expression'
    p[0] = str(p[1]) + str(p[2])
    
#############EQUALS###############
def p_equals(p):
    'equals: EQUALS'
    p[0] = str(p[1])
    
#############POLYNOMIAL VARIABLE###############
def p_pol_var_t(p):
    'pol_var_t: POLT'
    p[0] = str(p[1])
    
def p_pol_var_s(p):
    'pol_var_s: POLTS'
    p[0] = str(p[1])
    
#############POLYNOMIAL###############
def p_polynomial_t(p):
    'polynomial : pol_var_t equals expression'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])
    
def p_polynomial_s(p):
    'polynomial : pol_var_s equals expression'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

result = parser.parse(data)
print(result)
