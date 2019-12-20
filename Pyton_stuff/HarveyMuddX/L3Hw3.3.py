__author__ = 'darakna'
def dot( L, K ):
#    print (L[0],K[0])
    if len(L)!=len(K):
        return 0
    elif len(L)<1 or len(K)<1:
        #print("a")
        return 0
#    elif len(L)<1 and len(K)<1:
#        return 0
    else:
        #print("b")
        return  L[0]*K[0]+dot(L[1:],K[1:])

#
# Tests
#
print ("dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] ) )
print ("dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] ) )
print ("dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] ) )
print ("dot( [], [6] )           0.0 ==", dot( [], [6] ) )
print ("dot( [], [] )            0.0 ==", dot( [], [] )   )