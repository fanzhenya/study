#!/usr/bin/python

s1 = """ \
{'score': '98', 'name': 'Ming', 'sub': 'Math'} \
{'score': '100', 'name': 'Fzy', 'sub': 'Sci'} \
{'score': '87', 'name': 'Zhang', 'sub': 'Art'} \
"""

#print s1

s2 = 'name:mickey,age:58|name:minnie,age:47,weight:60'
dicList2 = [ dict(y.split(':')
    for y in x.split(','))
    for x in 'name:mickey,age:58|name:minnie,age:47,weight:60'.split('|')]
print dicList2
