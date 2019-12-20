from pag_12 import *
def pag17_prog():
    n = read_a_number()
    x = []
    for a in range(n):
        x.append(read_a_number())
    s1 = 0
    s2 = 0
    i = 0
    while(i<n):
        if x[i] != 0:
            s1 +=x[i]
        else:
            s2 -= x[i]
        if s1 != -s2:
            i += 1
        else:
            print(i)
            break
#pag17_prog()