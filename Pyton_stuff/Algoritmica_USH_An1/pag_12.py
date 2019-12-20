def read_a_number():
    nb = input('Choose a number: ')
    try:
        mode = int(nb)
    except ValueError:
        print("Not a number")
        mode = read_a_number()
    return mode
def pag12_prog():
    n = read_a_number()
    x = []
    for a in range(n):
        x.append(read_a_number())
    print(x)
    s=0
    i=0
    while(i<n):
        if x[i] > 0:
            s = s+x[i]

        else:
            s = s-x[i]
        i += 1
    s = s / n
    print(s)
#pag12_prog()