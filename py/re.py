#!/usr/bin/python

import re

line = "Cats are smarter than Dogs and dogs"

matchObj = re.match(r'(.*) are .* than (.*)', line)

if matchObj:
    print matchObj.group()
    print matchObj.groups()
    print matchObj.group(1)
    print matchObj.group(2)
else:
    print "No match"


# match the 1st occurance
searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
    print "search --> searchObj.group() : ", searchObj.group()
else:
    print "Nothing found!!"

findlist = re.findall( r'dogs', line, re.M|re.I)
print findlist



line = """ str = "hello \"world\" I am fzy" """
#findlist = re.findall(r'"[(?:\\")]*?"', line)
findlist = re.findall(r'"[^\"]*"', line)
print findlist
