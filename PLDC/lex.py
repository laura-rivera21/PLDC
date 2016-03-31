'''
Created on Mar 25, 2016

@author: Laura
'''
import ply.lex as lex

# lex.py - tokenizer

# list of tokens names
tokens = (
          'POLT', 
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
          'EXPONENT')

# reserved words
reserved = {
            'show':'SHOW',
            'laplace':'LAPLACE',
}

# Regular expression rules for simple tokens
t_PLUS    = '\+'
t_MINUS   = '-'
t_TIMES   = '\*'
t_DIVIDE  = '/'
t_LPAREN  = '\('
t_RPAREN  = '\)'
t_EXPONENT = '\^'
t_LAPLACE = '(?i)laplace'
t_SHOW = '(?i)show'
t_POLT = '(?i)polt'
t_POLS = '(?i)pols'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
Laplace(3+4)*8^2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value)
