#!/usr/bin/python

dic = {}
dic["SB"] = "Fzy"
dic["NB"] = "Ng Andrew"

dic2 = {"name": "fzy", "msg":"hello world"}

#print dic['SB']
#print dic2.keys()
#print dic2.values()

print dic2


glb_a="I'm glb var a"

print glb_a

def func(n, dic):
    global glb_a
    glb_a += ", modified in func !"
    print "hello" + str(n)
    print dic.values()

#func(1, dic);
func(2, dic2);

print glb_a

#raw_input("\nPress any key...")
