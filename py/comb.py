
def comb(l):
    if len(l) ==1:
        return [[], l]
    else: 
        rest = comb(l[1:])
        this_comb = []
        for sub in rest:
            this_comb.append(sub + [l[0]])
        return this_comb + rest

# Test:
all_comb = comb(['a', 'b', 'c'])
print all_comb
#print len(all_comb) 



def print_comb(lst, combined):
    if len(lst)==0:
        print combined
    else:
        print_comb(lst[1:], combined + [lst[0]])
        print_comb(lst[1:], combined)


#print_comb(['a', 'b', 'c'], [])
    

#_
#c
#
#b
#bc
#
#a
#ac
#ab
#abc
#
