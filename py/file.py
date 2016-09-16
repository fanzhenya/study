#!/usr/bin/python

import re

def dumpList(lst):
    print "=== dumping lst ==="
    for a in lst:
        if (type(a) == str) or (type(a)== dict):
            print '"' + str(a) + '"'
        elif type(a) == DbItem:
            print a.toString()
        else:
            print "Unknow list item type: " + str(type(a))

def dumpDict(dic):
    print "=== dumping dic ==="
    for a in dic:
        print '"' + a + '", ' + '"' + dic[a] + '"'

class DbItem(object):
    def __init__(self, name, sub, score):
        self.name = name
        self.sub = sub
        self.score = score
    def toString(self):
        return "{}: sub={}, score={}".format(self.name, self.sub, self.score)


fileName = "db.txt"
try:
    f = open(fileName)
except:
    print "cannot open file: " + fileName
    exit()

print "opened file: " + fileName
#print f.readline().replace('\n', '').upper()

lineList = []
dic = {}
db_dic = []
db = []
print f.readline().replace('\n', '')
n=1
for line in f:
    ln = line.replace('\n','')
    #print "line " + str(n) +": " + ln

    # list
    lineList.append(ln);
    parsedList=re.split("\s*", ln)

    #dic
    dic.update({parsedList[0]: parsedList[1]})

    #db_dic
    db_dic_item = {}
    db_dic_item.fromkeys(("name, sub, score"))
    db_dic_item["name"] = parsedList[0]
    db_dic_item["sub"] = parsedList[1]
    db_dic_item["score"] = parsedList[2]
    db_dic.append(db_dic_item);

    #dic
    dbItem = DbItem(parsedList[0], parsedList[1], parsedList[2])
    db.append(dbItem)

    n+=1


dumpList(lineList)
dumpDict(dic)
dumpList(db_dic)
dumpList(db)
f.close()
