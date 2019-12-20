__author__ = 'darakna'
# python 2
#
# Homework 3, Problem 2
#
# Name:
#

import random
import time
def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])
def posibil():
    neg=0
    pos=0
    for i in range(0,1000):
        if rs()==1:pos=pos+1
        else: neg=neg+1
    print(neg,pos)

def rwpos( start, nsteps ):
    if nsteps >=0:
        print("start is " , start)
        return rwpos(start+rs(),nsteps-1)
    else: return 0
#rwpos(40,8)

def rwsteps( start, low, hi ):
    time.sleep(0.02)   #sleep for 0.1 seconds
    if start <hi and start > low:
        a=rs()
        print(" "*(start-low),(" \\" if a==1 else "/")," "*(hi-start))
        return (rwsteps(start+a,low,hi))
    else:
        print("Bump!")
        return 0
rwsteps(25,5,50)