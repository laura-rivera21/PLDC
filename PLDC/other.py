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
          'EXPONENT',
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
t_EXPONENT = r'\^'
t_LAPLACE = r'(?i)laplace'
t_SHOW = r'(?i)show'
t_POLT = r'(?i)polt'
t_POLS = r'(?i)pols'
t_VART = r't'
t_VARS = r's'

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
data = '''laplace(-9s^2+3s-5)'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value)
