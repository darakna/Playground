__author__= "darakna"
from sys import stdout
from time import sleep
import os
def cls():
    os.system('cls')
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
#print("\r%d" % a)
#stdout.flush()
#print("\r",a)
#sleep(1)
#print("\r",b)
#stdout.write("\r%o" % int("2"))

def printBoard(A):
    returned=""
    for row in A:
        line = ''
        for col in row:
            line += str(col)+" "
        returned+=("\r%s" %  str(line)+"\n")
    return returned[:-1]
c=printBoard(a)
d=printBoard(b)
cls()
print(c)
sleep(1)
cls()
print(d)
#stdout.write("\r%s" %  c)
#stdout.flush
#sleep(1)
#stdout.write("\r%s" %  d)
#stdout.flush()
#sleep(0.2)
#stdout.write("\r%s" %  str(line for line in a ))
#stdout.flush()
#
#stdout.write("\r%s" %  str(b) )