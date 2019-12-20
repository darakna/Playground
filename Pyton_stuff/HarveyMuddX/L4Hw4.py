__author__ = 'darakna'
def encipher(S,n):
    if len(S)==0:
        return ""
    else:
        if ord(S[0]) in range(ord('A'),ord('Z')+1):
            if ord(S[0])+n > ord('Z'):
                return chr(ord(S[0])-26+n) + encipher(S[1:],n)
            else:
                return chr(ord(S[0])+n)+ encipher(S[1:],n)
        elif ord(S[0]) in range(ord('a'),ord('z')+1):
            if ord(S[0])+n > ord('z'):
                return chr(ord(S[0])-26+n) + encipher(S[1:],n)
            else:
                return chr(ord(S[0])+n)+ encipher(S[1:],n)
        else:
            return S[0]+encipher(S[1:],n)

print(encipher("AaZz",5),"                                  =FfEe")

# print("Test")
print (encipher('xyza', 1),"                                  =yzab")
print (encipher('Z A', 1,), '                                 =A B')
print (encipher('*ab?', 1),'                                  =*bc?')
print (encipher('This is a string!', 1),'                     =Uijt jt b tusjoh!')
print (encipher('Caesar cipher? I prefer Caesar salad.', 25),'=Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.')