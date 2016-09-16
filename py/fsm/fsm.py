#!/usr/bin/python

import re

# r'a+1+'


line = ["a1", "aa1", "aa11", "aa11a", "ab1", "1aa", "aa"]

print line


# states    TransCondi  Target
# 0         'a'         1
# 1         'a'         1
# 1         '1'         2 
# 2         '1'         2

fsm = [ \
        {'a': 1 }, \
        {'a': 1, '1':2 }, \
        {'1':2 } ]
print fsm 

def fsmAccept(fsm, s):
    cur=0
    nex=0
    for c in s[:]:
        print c
        edges = fsm[cur]
        if c in edges.keys():
            nex=edges[c]
            print "cur state", cur, "next state:", nex 
            cur=nex
        else:
            print "not find edge for", c, "from state", cur
            return False
    if cur == 2:
        return True
    else:
        return False

for s in line:
    print "==="
    print "entering:", s
    if fsmAccept(fsm, s):
        print "fsm accepted:", s
    else:
        print "!!! fsm Rejected:", s



