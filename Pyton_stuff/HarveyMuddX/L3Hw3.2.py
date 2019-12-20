__author__ = 'darakna'
def mult( n, m ):
    #functia mult primeste doi parametri si returneaza produsul acestora
    #obtinut prin adunare recursive
    if m==0:
        return 0
    elif m>0:
        return  n + mult(n,m-1)
    else:
        return -n-mult(-n,m+1)


print ( mult(6,-3))
print ("mult(6,7)    42 ==", mult(6,7))
print ("mult(6,-7)  -42 ==", mult(6,-7))
print ("mult(-6,7)  -42 ==", mult(-6,7))
print ("mult(-6,-7)  42 ==", mult(-6,-7))
print ("mult(6,0)     0 ==", mult(6,0))
print ("mult(0,7)     0 ==", mult(0,7))
print ("mult(0,0)     0 ==", mult(0,0))