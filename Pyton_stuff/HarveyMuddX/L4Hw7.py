__author__ = 'darakna'
#
#Not working
#
def score(l,S,T):
    print(l,S,T)
    if T=="":
        return 0
    else:
        if l in S and l not in T:
            return 0
        elif l in S and l in T[0]:
            print("AAA")
            return 1
        elif l in S and l in T[1:]:
            return 0
        elif l not in S and l in T[0]:
            print("BBB")
            return 1
        elif l not in S and l in T[1:]:
            return score(l,S,T[1:])
        else:
            return 0
def jscore(S,T):
    #print(S,T)
    if S=="":
        return 0
    elif S[0]in T:
        return score(S[0],S[1:],T) + jscore(S[1:],T)
    else:
        return jscore(S[1:],T)



print(jscore( 'gattaca', 'aggtccaggcgc' )) # 2 'a's, 1 't', 1 'c', 1 'g'
print(jscore( 'diner', 'syrup' )) # just the 'r'
print(jscore( 'geese', 'elate' ))