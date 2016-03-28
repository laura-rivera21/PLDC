'''
Created on Mar 25, 2016
@author: Melvin
'''
import ply.lex as lex

tokens = ['PLUS','MINUS','DIVIDE','TIMES','EULER','EXPONENT','NATLOG','TDOMAIN','SDOMAIN','TPOLYNOMIAL','SPOLYNOMIAL','LAPLACE','SHOW']
t_PLUS = r'\+'
t_MINUS= r'\-'
t_DIVIDE= r'/'
t_TIMES= r'\*'
t_EULER= r'\e'
t_EXPONENT= r'\^'
t_NATLOG= r'\ln'
t_TDOMAIN= r'\t'
t_SDOMAIN= r'\s'
t_TPOLYNOMIAL= r'\[][]'
t_SPOLYNOMIAL= r'\[][]'
t_LAPLACE= r'\laplace'
t_SHOW= r'\show'



print "hello world"