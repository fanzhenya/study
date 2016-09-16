#!/usr/bin/python

import re
import operator

word_list={}

#fname ='/var/log/apache2/access.log.1'
fname ='sample2.txt'

#exit(1)
f = open(fname)

for line in f:
    #print "===>" + line
    line = re.sub(r"[^a-zA-Z\-]", " ", line)
    parts = line.split(' ')
    
    for word in parts:
        if word == '':
            continue
        if word in word_list:
            word_list[word] += 1;
        else:
            word_list.update({word:1})



word_list = sorted(word_list.items(), key=operator.itemgetter(1))

for item in word_list:
    print '{0:20} => {1:10}'.format(item[0], item[1])
