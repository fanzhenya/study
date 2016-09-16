#!/usr/bin/python

import ply.lex as lex
import operator

f = open("./sample2.txt")

tokens=[
        'OTHER',
        'WORD'
        ]

def t_WORD(token):
    r'[a-zA-Z][a-zA-Z\-_]*'
    return token

def t_OTHER(token):
    r'[^a-zA-Z]+'
    return token


def t_error(token):
    print "invalid token:", token.value
    token.lexer.skip(1)

t_ignore = ' \t'

pagelexer = lex.lex()


word_list = {}
for line in f:
    pagelexer.input(line)
    for tok in pagelexer:
        if tok.type != "WORD":
        #if tok.type != "OTHER":
            continue
        if tok.value in word_list:
            word_list[tok.value] += 1
        else:
            word_list.update({tok.value:1})

word_list = sorted(word_list.items(), key=operator.itemgetter(1))

for item in word_list:
    print '{0:20} => {1:10}'.format(item[0], item[1])

