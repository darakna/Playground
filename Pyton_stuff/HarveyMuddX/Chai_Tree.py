__author__ = 'darakna'
from turtle import *
def chai(size):
    """ our chai function! """
    if (size<9):
        return 0
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai( size/2)
        right(90)
        forward(size)
        left(90)
        chai( size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return #chai(size+5)
chai(100)
left(90)
speed(0)
width(0)
def svtree( trunklength, levels ):
    if levels==1:
        return 0
    else:
        forward(trunklength)
        left(60)
        forward(trunklength*0.8)
        svtree(trunklength*0.8,levels-1)
        backward(trunklength*0.8)
        right(120)
        forward(trunklength*0.8)
        svtree(trunklength*0.8,levels-1)
        backward(trunklength*0.8)
        left(60)
        backward(trunklength)
        return
hideturtle()
svtree(77,2)
