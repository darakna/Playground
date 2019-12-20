__author__ = 'darakna'
import random
def throw_dart():
    return random.uniform(-1.0,1.0)
def check():
    x=throw_dart()
    y=throw_dart()
    if (x**2+y**2)**0.5<=1:
        return True
    else:
        return False
def forpi(n):
    numthrows=0
    numhits=0
    for i in range(n):
        numthrows+=1
        if check():
            numhits+=1
    return numhits/numthrows*4
#print(forpi(10000))
def aprox():
    numthrows=1
    numhits=1
    while numhits/numthrows*4!=3.1415:
        numthrows+=1
        if check():
            numhits+=1
        if numhits%1000==0:
            print(numthrows,numhits,numhits/numthrows*4)
    print(numthrows,numhits,numhits/numthrows*4)
aprox()