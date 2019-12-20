__author__ = 'darakna'
def counter(l,T):
    if T == "":
        return 0
    else:
        if l == T[0]:
            return 1 + counter(l,T[1:])
        elif l != T[0]:
            return 0 + counter(l,T[1:])




def jscore (S,T):
    if S=="":
        return 0
    elif counter(S[0],S)>counter(S[0],T):
        return jscore(S[1:],T)
    elif counter(S[0],S)<=counter(S[0],T):
        return 1 + jscore(S[1:],T)



print (jscore("g", "gattaca"))

print(jscore( 'gattaca', 'aggtccaggcgc' )) # 2 'a's, 1 't', 1 'c', 1 'g'
print(jscore( 'diner', 'syrup' )) # just the 'r'
print(jscore( 'geese', 'elate' ))
print(jscore( 'gattaca', '' )) # if empty, return 0