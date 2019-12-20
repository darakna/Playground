__author__ = 'darakna'
# python 2

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.

def mutate(i, oldL):
    new_ith_element = 1 + oldL[i]
    return new_ith_element


def evolve(oldL, curgen = 0):
    print (oldL,                    )# print the old list, L
    print ("  (gen: " + str(curgen) + ")"  )# and its gen.
    time.sleep(0.25)

    if curgen == 5:  # we're done!
        return       # no return value... yet
    else:
        newL = [ mutate(i, oldL) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)
def mutate_aux(oldL):
    if not oldL:
        return 0
    else:
        return [oldL[i]**2 for i in range(len(oldL)) ]
def mutate1(list_lst,gen=0):
    print (list_lst,"(g:",gen,")")
    if gen == 5:
        return
    else:
        list_new=mutate_aux(list_lst)
        return mutate1(list_new,gen+1)
#mutate1([1,2,3])
def mutate2(list_l,gen=0):
    print (list_l,"(g:",gen,")")
    if gen == 5:
        return
    else:
        return mutate2(list((list_l[-1:]+list_l[:-1])),gen+1)
#mutate2( [1,2,3,42] )
def mutate3(list_l, gen=0):
    print (list_l,"(g:",gen,")")
    if gen == 5:
        return
    else:
        i=choice(range(len(list_l)))
        list_l[i]=choice([0,1])
        return mutate3(list_l,gen+1)
mutate3([1,2,3,42])