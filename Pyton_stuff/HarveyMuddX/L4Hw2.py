__author__ = 'darakna'
from random import *
def allOnes(L):
    if len(L)==0:
        return True
    else:
        if L[0]==1:
            return allOnes(L[1:])
        else:
            return False

def evolve(list_l, gen=0):
    print (list_l,"(g:",gen,")")
    if allOnes(list_l) is True:
        return gen
    else:
        for i in range(0,len(list_l)):
            list_l[i]=choice([0,1])
        return evolve(list_l,gen+1)

evolve( [0,0,0,0,1])

