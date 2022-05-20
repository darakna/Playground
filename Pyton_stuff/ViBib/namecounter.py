import re

def get_filelines():
    filehandler = open("all_books.log", "r")
    linereader = filehandler.readlines()
    print("Read %s lines" % len(linereader))
    return linereader

def get_finameSize():
    linereader = get_filelines()
    charCounter = {}
    for elem in linereader:
        if str(len(elem)) not in charCounter:
            charCounter[str(len(elem))] = 1
        else:
            charCounter[str(len(elem))] = charCounter[str(len(elem))] + 1        
        indexpos = 0

    while(indexpos<len(charCounter)):
        if str(indexpos) in charCounter:
            print("%s : %s" % (indexpos, charCounter[str(indexpos)]))
        indexpos+=1

def get_allTags():
    linereader = get_filelines()
    indextag = []
    for elem in linereader:   
        curtag = elem.split()
        res = re.split('{|}', elem)
        if len(res) <= 2:
            print(res)
        elif res[1] not in indextag:
            indextag.append(res[1])    
    print("There are %s tags:\n%s" %(len(indextag), "\n".join(indextag)))

get_finameSize()
get_allTags()