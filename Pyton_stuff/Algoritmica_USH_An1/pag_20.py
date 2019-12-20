from pag_12 import read_a_number
def pag20_prog(x = None):
    n = len(x)
    if n == 0:
        n = read_a_number()
        for a in range(n):
            x.append(read_a_number())
    i=0
    print(x)
    while i < n:
        if x[i] != 0:
            pass
        else:
            print("Sirul contine zerouri")
            break
        i += 1
        if i == n:
            print("Sirul nu contine zerouri")
#pag20_prog([1,2,3])
#pag20_prog([0,2,3])
#pag20_prog([1,2,0])
#pag20_prog([0])
#pag20_prog([0,0])
