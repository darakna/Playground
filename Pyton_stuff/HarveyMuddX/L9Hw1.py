__author__ = 'darakna'
# Homework 9, Problem 1
# Game of Life
import random
import os
def cls():
    os.system('cls')
def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A
def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)+" "
        print (line)
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
def randomCells(w, h):
    A = createBoard(w,h)
    for line in range(1,w-1):
        for col in range(1,h-1):
            A[line][col]=random.choice([0, 1])
    return A
def modif(a,A):
    pass
def isn(e):
    return True if e else False
def countN(l,c,a):
    return a[l-1][c-1]+a[l-1][c]+a[l-1][c+1]+a[l][c-1]+a[l][c+1]+a[l+1][c-1]+a[l+1]

def mutate(a):
    if len(a)<=2 or len(a[0])<=2:
        print("Area to small")
        return a
    else:
        line=random(1,len(a)-1)
        col=random(1,len(a)-1)
        countN(a,line,col)
        modif(a[line][col])

b=diagonalize(8,8)
c=randomCells(8,8)
printBoard(c)
#print(len(b),len(b[0]))