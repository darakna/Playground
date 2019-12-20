__author__ = 'darakna'
# python 2
#
# Homework 8, Problem 1
# Loops!
#
# Name:
#

def fac(n):
    """ loop-based factorial function
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests: run by pressing the Run button above
def power(b,p):
    bw=1
    for pw in range(0,p):
        bw=bw*b
    return bw


print("power(2,5): should be 32 == ", power(2,5))
print ("power(5,2): should be 25 == ", power(5,2))
print ("power(42,0): should be 1 == ", power(42,0))
print ("power(0,42): should be 0 == ", power(0,42))
print ("power(0,0): should be 1 == ", power(0,0))

print ("fac(0): should be 1 == ", fac(0))
print ("fac(5): should be 120 == ", fac(5))



def summed( L ):
    """ loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        result = result + e  # or result += e
    return result

# tests!
print("summed( [4,5,6] ): should be 15 == ", summed( [4,5,6] ))
print ("summed( range(3,10) ): should be 42 == ", summed( range(3,10) ))

import random

def countGuesses( hidden ):
    """ uses a while loop to guess hidden, from 0 to 99
        input: hidden, a "hidden" integer from 0 to 99
        output: the number of guesses needed to guess hidden
    """
    guess = random.choice( range(0,100000) ) # 0 to 99, inclusive
    numguesses = 1    # we just made one, above
    a=0
    while guess != hidden:
        guess = random.choice( range(0,100000) )  # guess again!
        a+=guess
        numguesses += 1  # add one to our number of guesses
    #print(a/numguesses)
    return numguesses

print("I took", countGuesses( 199 ), "guesses to guess 42!")