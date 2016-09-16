#!/usr/bin/python

v = ["a", "b", "c"]
glbvar = 1

def modify(v):
    #global v

    # if we access it as a 'reference', we can access global v's memory
    del v[:]
    v.append("x")
    v.append("y")

    # if we re-assign v to another object, we cannot access global v's memory
    v = []
    v += ["xxx", "yyy"]

    print "func: " + str(v)

    #global glbvar
    #glbvar = 2
    #print "glbvar:", glbvar

print "main1:", str(v)
#print "glbvar:", glbvar
modify(v)
print "main2: " + str(v)
#print "glbvar:", glbvar

