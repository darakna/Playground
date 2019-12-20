__author__ = 'darakna'
import datetime
from random import *
def mutate3(list_l, gen=0):
    #print (list_l,"(g:",gen,")")
    if gen == 900:
        return
    else:
        i=choice(range(len(list_l)))
        list_l[i]=choice([0,1])
        return mutate3(list_l,gen+1)

def perf_t():
    start_time=datetime.datetime.now()
    for i in range(0,1000):
        mutate3([1,2,3,42])
    stop_time=datetime.datetime.now()
    return (stop_time-start_time)
print(perf_t())