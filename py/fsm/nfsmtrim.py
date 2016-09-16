#!/usr/bin/python

# Title: FSM Optimization
# 
# Challenge Problem: 2 Stars
#
# Lexical analyzers are implemented using finite state machines generated
# from the regular expressions of token definition rules. The performance
# of a lexical analyzer can depend on the size of the resulting finite
# state machine. If the finite state machine will be used over and over
# again (e.g., to analyze every token on every web page you visit!), we
# would like it to be as small as possible (e.g., so that your webpages
# load quickly). However, correctness is more important than speed: even
# an optimized FSM must always produce the right answer.  
#
# One way to improve the performance of a finite state machine is to make
# it smaller by removing unreachable states. If such states are removed,
# the resulting FSM takes up less memory, which may make it load faster or
# fit better in a storage-constrained mobile device.
#
# For this assignment, you will write a procedure nfsmtrim that removes
# "dead" states from a non-deterministic finite state machine. A state is
# (transitively) "dead" if it is non-accepting and only non-accepting
# states are reachable from it. Such states are also called "trap" states:
# once entered, there is no escape. In this example FSM for r"a*" ...
#
# edges = { (1,'a') : [1] ,
#           (1,'b') : [2] ,
#           (2,'b') : [3] ,
#           (3,'b') : [4] } 
# accepting = [ 1 ] 
# 
# ... states 2, 3 and 4 are "dead": although you can transition from 1->2,
# 2->3 and 3->4 on "b", you are doomed to rejection if you do so. 
#
# You may assume that the starting state is always state 1. Your procedure
# nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting)
# corresponding to a FSM that accepts exactly the same strings as the input
# FSM but that has all dead states removed. 
#
# Hint 1: This problem is tricky. Do not get discouraged. 
#
# Hint 2: Think back to the nfsmaccepts() procedure from the "Reading
# Machine Minds" homework problem in Unit 1. You are welcome to reuse your
# code (or the solution we went over) to that problem. 
#
# Hint 3: Gather up all of the states in the input machine. Filter down
# to just those states that are "live". new_edges will then be just like
# edges, but including only those transitions that involve live states.
# new_accepting will be just like accepting, but including only those live
# states. 

# A stack, containning the transition hitory
#  [ (0, 'a'): 1, 
#    (1, 'b'): 2,
#    (2, 'c'): 3,
#    (3, 'd'): 1,
#    (1, 'b'): 4,   --> non-determinstic
#    ....           --> another loop back to 1
#    (1, 'x'): 5,
#    ....
#   ]

def isTransitInFsm(fsm, transit):
    if transit[0] in fsm:
        if transit[1] in fsm[transit[0]]:
            return True
    return False

def addTransitsToFsm(fsm, transits, live_states):
    for transit in transits:
        msg = ''
        if isTransitInFsm(fsm, transit):
            msg = "Skipped"
        else:
            live_states.append(transit[0][0])
            if transit[0] in fsm:
                fsm[transit[0]] += [transit[1]]
            else:
                fsm.update( {transit[0]: [transit[1]]} )
        print "adding", transit, "to fsm:", fsm, msg

def nfsmExplore(fsm, cur, accepting, new_fsm, new_accepting, live_states, visited_path):
    print "=========="
    print "cur:", cur, "new_fsm:", new_fsm, "new_accepting:", new_accepting, "visited:", visited_path
    transits = []
    for key in fsm.keys():
        if key[0] == cur:
            for value in fsm[key]:
                transits.append((key, value))
    # if there's no available transits from current state, stop exploring
    print "transits:", transits
    if not transits:
        print "no transits from cur:", cur
        if cur in accepting:
            if cur not in new_accepting:
                new_accepting.append(cur)
            print "state", cur, "is in accepting, return True"
            return True
        else:
            print "return False"
            return False

    if cur in accepting:
        print "!!1 cur:", cur, "is in accepting states"
        if cur not in new_accepting:
            new_accepting.append(cur)
        addTransitsToFsm(new_fsm, visited_path, live_states)
    else:
        if cur in live_states:
            print "!!2 cur:", cur, "is in live_states"
            addTransitsToFsm(new_fsm, visited_path, live_states)

    has_live_transit = False
    for transit in transits:
        if isTransitInFsm(new_fsm, transit):
            print "transit", transit, "already in new_fsm, continue"
            has_live_transit = True
            continue

        if transit in visited_path:
            print "transit already visited:", transit, "return False"
            return False
        else:
            print "making transit: ", transit
            visited_path.append(transit)
            if nfsmExplore(fsm, transit[1], accepting, new_fsm, new_accepting, live_states, visited_path):
                has_live_transit = True
                addTransitsToFsm(new_fsm, {transit}, live_states)
            visited_path.pop()
    return has_live_transit



import copy
def nfsmtrim(edges, accepting): 
    # Write your code here.


    visited = []
    live_states = []
    new_edges = {}
    new_accepting = []

    #new_edges_last_time = None
    #new_accepting_last_time = None

    changed = True
    count = 0
    while True:
        count += 1
        print "**** Round", count, "****"
        new_edges_last_time = copy.deepcopy(new_edges)
        new_accepting_last_time = copy.deepcopy(new_accepting)
        nfsmExplore(edges, 1, accepting, new_edges, new_accepting, live_states, visited)
        if new_edges == new_edges_last_time and new_accepting == new_accepting_last_time:
            break

    print new_edges
    print new_accepting

    return (new_edges, new_accepting)
    

    

        


# We have included a few test cases, but you will definitely want to make
# your own. 

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , } 
accepting1 = [ 1 ] 
(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 
print new_edges1
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1] 

(new_edges2, new_accepting2) = nfsmtrim(edges1,[]) 
print new_edges2 == {}
print new_accepting2 == [] 

(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6]) 
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]

edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
accepting4 = [ 2 ] 
(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4) 
print new_edges4 == { 
  (1, 'a'): [1],
  (1, 'b'): [2], 
  (2, 'b'): [3], 
  (3, 'c'): [2, 1], 
}
print new_accepting4 == [2]

edges5 = { (1,'a') : [1] ,
        (1,'b') : [2] ,
        (2,'b') : [3] } 
accepting5 = [3]
(new_edges5, new_accepting5) = nfsmtrim(edges5, accepting5) 
print new_edges5 == {
        (1,'a') : [1] ,
        (1,'b') : [2] ,
        (2,'b') : [3] }
print new_accepting5 == [3]

