def distance(x1,y1,x2,y2):
    return "%.2f" % (((x1-x2)**2)+((y1-y2)**2))**(1/2)
def sqrt(nmbr):
    return nmbr**(1/2)
print(sqrt(4))
print(sqrt(5))
print(distance(9,7,3,2))
print(distance(-3,5,7,-1))
print(distance(1,0,4,4))
print(distance(0,0,16000,9000))