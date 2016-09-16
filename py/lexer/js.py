# JavvaScript: Comments & Keywords
#
# In this exercise you will write token definition rules for all of the
# tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and
# STRING. In addition, you will handle // end of line comments
# as well as /* delimited comments */. 
#
# We will assume that JavaScript is case sensitive and that keywords like
# 'if' and 'true' must be written in lowercase. There are 26 possible
# tokens that you must handle. The 'tokens' variable below has been 
# initialized below, listing each token's formal name (i.e., the value of
# token.type). In addition, each token has its associated textual string
# listed in a comment. For example, your lexer must convert && to a token
# with token.type 'ANDAND' (unless the && is found inside a comment). 
#
# Hint 1: Use an exclusive state for /* comments */. You may want to define
# t_comment_ignore and t_comment_error as well. 

import ply.lex as lex

  
reserved = {
        'else'    : 'ELSE',
        'false'   : 'FALSE',
        'function': 'FUNCTION',
        'if'      : 'IF',
        'return'  : 'RETURN',
        'true'    : 'TRUE',
        'var'     : 'VAR'
        }

tokens = [
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
#        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
#        'FALSE',        # false
#        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### Not used in this problem.
#        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
#        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### Not used in this problem. 
        'TIMES',        # *
#        'TRUE',         # true
#        'VAR',          # var
] + reserved.values()

#
# Write your code here. 
#


states = (
        ('dcomments', 'exclusive'),
        )


def t_ecomments(token):
    r'//.*\n'
    token.lexer.lineno +=1
    pass

t_ANDAND=r'&&'       # &&
t_COMMA=r','        # ,
t_DIVIDE=r'/'       # /
#t_ELSE=r'else'         # else
t_EQUAL=r'='        # =
t_EQUALEQUAL=r'=='   # ==
#t_FALSE=r'false'        # false
#t_FUNCTION=r'function'     # function
t_GE=r'>='           # >=
t_GT=r'>'           # >
#t_IF=r'if'           # if
t_LBRACE=r'\{'       # {
t_LE=r'<='           # <=
t_LPAREN=r'\('       # (
t_LT=r'<'           # <
t_MINUS=r'-'        # -
t_NOT=r'!'          # !
t_OROR=r'\|\|'         # ||
t_PLUS=r'\+'         # +
t_RBRACE=r'\}'       # }
#t_RETURN=r'return'       # return
t_RPAREN=r'\)'       # )
t_SEMICOLON=r';'    # ;
t_TIMES=r'\*'        # *
#t_TRUE=r'true'         # true
#t_VAR=r'var'          # var



def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    token.type = reserved.get(token.value, 'IDENTIFIER')
    return token

def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]+)?'
    token.value = float(token.value)
    return token

def t_STRING(token):
    #r'"(?:[^"\\]|(?:\\.))*"'
    r'"(?:[^"\\]|\\.)*"'
    token.value = token.value[1:-1]
    return token



def t_dcomments(token):
    r'/\*'
    token.lexer.code_start = token.lexer.lexpos
    token.lexer.begin('dcomments')

def t_dcomments_exit(token):
    r'\*/'
    token.value = token.lexer.lexdata[token.lexer.code_start:token.lexer.lexpos+1]
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

t_dcomments_ignore = ' \t\v'

def t_dcomments_error(token):
    #print "commnent unmatched: " + token.value#[0]
    token.lexer.skip(1)


# end code

t_ignore = ' \t\v\r' # whitespace 

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character: " + t.value[0], "at pos: ", t.lexpos
    print "dump:", t.value 
    t.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own. 

lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
    #print "==>", [tok.type, tok.lineno, tok.value]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1)
print test_lexer(input1) == output1

lexer = lex.lex() 

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2)
print test_lexer(input2) == output2

lexer = lex.lex() 

#str = "I have a \"ideal\" dream, which is to Fuck you"
input3 = """
str = if "I have a \\"idealistic\\" dream, which is to !Sleep# /*Fuck*/ you~~"
return """
output3 = ['IDENTIFIER', 'EQUAL', 'IF', 'STRING', 'RETURN']
print test_lexer(input3) == output3
