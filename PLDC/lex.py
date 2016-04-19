import ply.lex as lex

# PLDClex.py - tokenizer

# list of tokens names
from Poliynomial import Polynomial
from coef import coefi

tokens = ('LAPLACE',
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
          'EQUALS',
          'EXPRNAME',
          'SHOWTEXT',
          'COMMA')

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
t_VART = r't'
t_VARS = r's'
t_EQUALS = r'\='
t_SHOWTEXT = r'"(.*?)"'
t_COMMA = r'\,'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EXPRNAME(t):
    r'(([A-Za-z]+[0-9]+)|([A-Za-z][A-Za-z]+[0-9]*))+'
    if t.value in 'laplace':
        t.type = reserved.get(t.value,'ID')
    if t.value in 'show':
        t.type = reserved.get(t.value,'ID')
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
data = '''varnam = laplace 3t^2+5t+3'''

# Give the lexer some input
lexer.input(data)



def printtok():
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.type, tok.value)

# Tokenize
print data
#printtok()



# Yacc test

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

#############LangFunctions###############
def p_langfunctions(p):
    'langfunction : polynomial'
    p[0] = str(p[1])

def p_langfunctions1(p):
    'langfunction : function'
    p[0] = str(p[1])

def p_langfunctions2(p):
    'langfunction : exprname'
    p[0] = str(p[1])

#############POLYNOMIAL###############
def p_polynomial(p):
    'polynomial : exprname expression'
    p[0] = str(p[1]) + str(p[2])


#############EXPRESSION NAME###############
def p_exprname(p):
    'exprname : EXPRNAME '
    p[0] = str(p[1])


def p_exprname1(p):
    'exprname : EXPRNAME EQUALS'
    p[0] = str(p[1]) + str(p[2])

def p_exprname2(p):
    'exprname : EXPRNAME EQUALS function'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_exprname3(p):
    'exprname : EXPRNAME EQUALS expression'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

#############FUNCTION###############
def p_function(p):
    'function : LAPLACE expression'
    pol = Polynomial(coefi(p[2])).show()
    p[0] = str(pol)
           #str(p[2])


def p_function1(p):
    'function : LAPLACE LPAREN exprname RPAREN'
    p[0] = str(p[1]) + '(' + str(p[3]) + ')'

def p_function2(p):
    'function : SHOW expression'
    p[0] = str(p[1]) + str(p[2])

def p_function3(p):
    'function : SHOW exprname '
    p[0] = str(p[1]) + " " + str(p[2])

def p_function4(p):
    'function : SHOW SHOWTEXT '
    p[0] = str(p[1]) +  str(p[2])

def p_function5(p):
    'function : SHOW LPAREN SHOWTEXT COMMA exprname RPAREN'
    p[0] = str(p[1]) + '(' + str(p[3]) + ',' + str(p[5]) +')'

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
    'term : factor  variable RAISED factor'
    p[0] = str(p[1]) + str(p[2]) + '^' + str(p[4])

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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

#result = parser.parse(data,debug=1)
result = parser.parse(data)
print(result)