'''
Created on Mar 25, 2016
@author: Laura
'''
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
          'VARS')

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
t_POLT = r'(?i)polt'
t_POLS = r'(?i)pols'
t_VART = 't'
t_VARS = 's'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d'
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
data = '''9t^2+3t+5'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value)

# Yacc test

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
#from PLDClex import tokens

############EXPRESSION###############
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

##############TERM##################
def p_term_times(p):
    'term : factor TIMES variable'
    p[0] = p[1] * p[3]

def p_term_times_2(p):
    'term : factor TIMES variable RAISED exponent'
    p[0] = p[1] * p[3] ^ p[5]

def p_term_var_exp(p):
    'term : variable RAISED exponent'
    p[0] = p[1] ^ p[3]

def p_term_var(p):
    'term : variable'
    p[0] = p[1]

def p_term_fac(p):
    'term : factor'
    p[0] = p[1]

##############FACTOR################
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


#############VARIABLE###############
def p_variable_t(p):
    'variable : VART'
    p[0]=p[1]

def p_variable_s(p):
    'variable : VARS'
    p[0]=p[1]



#############EXPONENT###############
def p_exponent(p):
    'exponent : NUMBER'
    p[0]=p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = '9s^2+3s+5'
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)