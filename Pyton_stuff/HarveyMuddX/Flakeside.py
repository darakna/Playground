__author__ = 'darakna'
from turtle import *
from time import *
def flakeside(sidelength, levels):
    if levels==0:
        forward (sidelength)
        return 0
    else:
        flakeside (sidelength/3,levels-1)
        right(60)
        flakeside(sidelength/3,levels-1)
        left(120)
        flakeside(sidelength/3,levels-1)
        right(60)
        flakeside (sidelength/3,levels-1)


def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
snowflake(100,3)

sleep(2)