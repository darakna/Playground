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
def mutate4(oldL, gen=0):
    if gen == 0:
        for i in range(0,len(oldL)):
            oldL[i]=choice([0,1])
    return oldL

def evolve(list_l, gen=0):
    print (list_l,"(g:",gen,")")
    if gen==0:
        list_l=mutate4(list_l,gen+1)
    if allOnes(list_l) is True:
        return gen
    else:
        user = int(input("Index? "))
        if user in range(0,len(list_l)):
            list_l[user]= 1 if list_l[user]==0 else 0
            if user>0:list_l[user-1]= 1 if list_l[user-1]==0 else 0
            if user<(len(list_l)-1):list_l[user+1]= 1 if list_l[user+1]==0 else 0
        return evolve(list_l,gen+1)

print(evolve( [0, 1, 2, 3, 4, 5, 6, 7]))
