#!/usr/bin/python

import ply.lex as lex

testline = """11 + 2 - ( 33 *4 ) / 55
    + 6 -77
"""

tokens = [
       'NUM',
       'PLUS',
       'MINUS',
       'MUL',
       'DIV',
       'LP',
       'RP'
        ]

t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_LP    = r'\('
t_RP    = r'\)'

def t_NUM(tok):
    r'\d+'
    tok.value = int (tok.value)
    return tok

def t_newline(tok):
    r'\n+'
    tok.lexer.lineno += len(tok.value)


def t_error(tok):
    print("Illegal char: '%s'" % tok.value[0])
    tok.lexer.skip(1)

t_ignore = ' \t'

callexer = lex.lex()
callexer.input(testline)

for tok in callexer:
    print tok

