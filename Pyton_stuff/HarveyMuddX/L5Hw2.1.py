__author__ = 'darakna'
def isOdd(numb):
    if numb%2==0:
        return False
    else:
        return True

print(isOdd(42))
print(isOdd(43))

def numToBinary(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    elif isOdd(N):
        return 1+(numToBinary(int(N/2))*10)
    else:
        return numToBinary(int(N/2))*10
def binaryToNum(S):
    if S==0:
        return 0
    elif S%10==1:
        return 1+(binaryToNum(int(S/10)))*2
    else:
        return binaryToNum(int(S/10))*2

print(numToBinary(5))
print(numToBinary(12))
print(numToBinary(0),'')
print(numToBinary(1),'1')
print(numToBinary(4),'100')
print(numToBinary(10),'1010')
print(numToBinary(42),'101010')
print(numToBinary(100),'1100100')

print(binaryToNum(101),"5")
print(binaryToNum(101010),"42")
print(binaryToNum(100),"4")
print( binaryToNum(1011),"11")
print( binaryToNum(1011),"11")
print( binaryToNum(0),"0")
print( binaryToNum(0),"0")
print( binaryToNum(1100100),"100")
print( binaryToNum(101010),"42")