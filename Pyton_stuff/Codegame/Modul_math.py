def modul (nbr):
    if nbr >= 0:
        return nbr
    else:
        return -1*nbr
listnum = []
listnum.append([1,modul(1)])
listnum.append([-5,modul(-5)])
listnum.append([0,modul(0)])
listnum.append([-0,modul(-0)])
print(listnum)
#print (modul(1))
#print (modul(-5))
#print(modul(0))
#print (modul(-0))