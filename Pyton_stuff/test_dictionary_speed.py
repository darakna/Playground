d = dict((val, chr(ord("a") + idx)) for val,idx in enumerate(range(16)))
print({x,y} for x,y in enumerate(range(16)))
print(d)
print(d.keys())
for elem in d:
    print(elem)