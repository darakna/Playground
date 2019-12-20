__author__ = 'darakna'
# python 2
#
# Homework 3, Problem 3
# List comprehensions!
#
# Name:
#

# this gives us functions like sin and cos
from math import *

# two more functions (not in the math library above)
def dbl(x):
    """ doubler!  input: x, a number """
    return 2*x

def sq(x):
    """ squarer!  input: x, a number """
    return x**2

# examples for getting used to list comprehensions
def lc_mult( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each multiplied by 2**
    """
    return [ 2*x for x in range(N) ]

def lc_idiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        WARNING: this is INTEGER division...!
    """
    return [ x/2 for x in range(N) ]

def lc_fdiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        NOTE: this is floating-point division...!
    """
    return [ float(x)/2 for x in range(N) ]


# Here is where your functions start for the homework:

# Step 1, part 1
def unitfracs( N ):
    """ be sure to improve this docstring!
    """
    pass  # replace this line (pass is Python's empty statement)

print(lc_mult( 10 ),  # multiplication example
lc_mult( 5 ),  # a smaller example
lc_idiv( 10 ) , # integer division
lc_fdiv( 10 ) ) # floating-point division
def dbl(x):
  """ input: a number x (int or float)
    output: twice the input
  """
  return 2*x