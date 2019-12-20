import string
#import sys
#sys.setrecursionlimit(1000000) # 10000 is an example, try with different values

#filehandler = open('test_str.txt', 'r')
filehandler = open('input_str.txt', 'r')
text=filehandler.read()
text = text.split("\n")
#print(text)

#for e in text:
#    print (e, e.count(" "))

def isn(strg):
    try:
        a = int(strg)
        return True
    except:
        return False

def calc(text, value):
    print ("Jump in for", value)
    if isn(value) is True:
            return int(value)
    for e in text:
        f = e.split(" ")
        if e.endswith(" -> " + value):

            if e.count(" ") == 2:
                return calc(text,(f[0]))
            elif "AND" in e:
                return calc(text, f[0]) & calc(text, f[2])
            elif "NOT" in e:
                return 65536 + ~calc(text, f[1])
            elif "OR" in e:
                return calc(text, f[0]) | calc(text, f[2])
            elif "LSHIFT" in e:
                return calc(text, f[0]) << int(f[2])
            elif "RSHIFT" in e:
                return calc(text, f[0]) >> int(f[2])
            else:
                print("- = - = -")
                return 0
print(calc(text, "a"))
#print(calc(text, "d"),": 72")
#print(calc(text, "e"),": 507")
#print(calc(text, "f"),": 492")
#print(calc(text, "g"),": 114")
#print(calc(text, "h"),": 65412")
#print(calc(text, "i"),": 65079")
#print(calc(text, "x"),": 123")
#print(calc(text, "y"),": 456")
