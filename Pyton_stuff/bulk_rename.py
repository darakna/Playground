from os import walk
import os

path_file = "WordList Collection"
os.chdir(path_file)
f = []
for (dirpath, dirnames, filenames) in walk(path_file):
    f.extend(filenames)
    break
size = 0
g =[]
for a in f:
    size = os.path.getsize(a)
    g.extend([(a, size)])
g_ordonat = []
while (len(g) > 0):
    minsize = g[0][1]
    gasit = 0
    #print(minsize)
    for a in range(len(g)):
        if minsize > g[a][1]:
            minsize = g[a][1]
            gasit = a
    g_ordonat.extend([g[gasit]])
    g.pop(gasit)
for elem in range(len(g_ordonat)):
    if elem > 8:
        os.rename(g_ordonat[elem][0], "{0:03d}".format(elem) + "_" + g_ordonat[elem][0])
        #print(g_ordonat[elem][0], "{0:03d}".format(elem) + "_" + g_ordonat[elem][0])
        #print(g_ordonat[elem])
    #print(g_ordonat[elem])


