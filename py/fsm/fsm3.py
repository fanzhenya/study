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

fsm = { (0, 'a'): 1,
        (1, 'a'): 1, (1, '1'): 2,
        (2, '1'): 2 }
print fsm 

accepting = [2]

def fsmAccept(fsm, s, cur, accepting):
    if s == "":
        return cur in accepting
    try:
        #print cur, s
        return fsmAccept(fsm, s[1:], fsm[(cur, s[0])], accepting )
    except:
        print "not find edge for", (cur, s[0])
        return False


for s in line:
    print "==="
    print "entering string:", s
    myResult = fsmAccept(fsm, s, 0, accepting)
    if myResult:  
        print "fsm accepted:", s
    else:
        print "!!! fsm Rejected:", s

    goldenResult = re.findall(r'a+1+', s) == [s]
    print "golden:",  goldenResult
    
    assert(myResult == goldenResult)


