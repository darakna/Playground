__author__ = 'darakna'
#Binary sort

def compare(L,pos=0):
    if pos<0:pos=pos+1
    if pos+1>=len(L):
        return L
    else:
        if L[pos]>L[pos+1]:
            a=L[pos]
            L[pos]=L[pos+1]
            L[pos+1]=a
            return compare(L,pos-1)
        else:
            return compare(L,pos+1)
#def blsort(L):
#    L=compare(L,0)
#    return L

print(compare([ 18, 9]))

