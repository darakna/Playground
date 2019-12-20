from pag_12 import read_a_number
def pag21_prog(m = None, n = None):
    if m == None and n == None:
        m = read_a_number()
        n = read_a_number()
    a,b = m, n
    if m < n: m,n = n,m
    r = 0
    if m == n:
        n = 0
        r = m
    while n:
        r = n
        n = m % n
        m = r
    if r == 0:
        print(a, b," Numere prime", r)
    else:
        print(a, b," Cmmdc este ", r)

pag21_prog(6, 3)
pag21_prog(4, 3)
pag21_prog(16, 240)
pag21_prog(0, 1)
pag21_prog(1, 0)
pag21_prog(0, 0)
pag21_prog(110, 110)