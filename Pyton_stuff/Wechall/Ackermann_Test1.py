__author__ = 'darakna'
def ack(m,n):
    print(m,n)
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    else:
        print("Exception throw")

print(ack(4,3))