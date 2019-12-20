__author__ = 'darakna'
from time import sleep
from turtle import *    # loads the turtle library...
width(0)        # make the turtle pen 5 pixels wide
#shape('turtle') # use a turtle shape!
#forward(100)    # turtle goes forward 100 steps
right(90)       # turtle turns right 90 degrees
up()            # turtle lifts its pen up off of the paper
#forward(100)    # turtle goes forward 100 steps
down()          # turtle puts its pen down on the paper
color("red")    # turtle uses red pen
#circle(100)     # turtle draws circle of radius 100
#color("blue")   # turtle changes to blue pen
#forward(50)     # turtle moves forward 50 steps
#sleep(2)

from turtle import *
import time

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )

#poly( 7, 7 )
print((pensize()))
pensize(1)
speed(2)

def spiral( initialLength, angle, multiplier ):
    if initialLength<=1 or initialLength>500:
        return 0
    else:
        forward(initialLength)
        left(angle)
        return spiral(initialLength*multiplier,angle,multiplier)
#spiral( 5, 15, 1.01 )
spiral(2, 135, 1.1)