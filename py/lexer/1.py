#!/usr/bin/python

import ply.lex #as lex

webpage = "This is <b>my </b> web page"

tokens = (
        'RANGLE',
        'LANGLESLASH',
        'LANGLE',
        'WORD'
        )



def t_RANGLE(token):
    r'>'
    return token

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_WORD(token):
    r'\w+'
    return token

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    "ero str"
    t.lexer.skip(1)

htmllexer = ply.lex.lex()

htmllexer.input(webpage)

for tok in htmllexer:
    print tok

#while True:
#    tok = htmllexer.token()
#    if not tok:
#        break
#    print tok




print test_ANY("any")
