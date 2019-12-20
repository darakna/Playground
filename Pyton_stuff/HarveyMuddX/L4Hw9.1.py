__author__ = 'darakna'
def ver(S,T):
    if S=="" and T=="":
        return "Match"
    elif S=="" or T=="":
        return ""
    elif S[0] in T:
        return S[0]+ver(S[1:],T[T.find(S[0])+1:])
    else:
        return ""
def ver3(S,T):
    if S == "" or T=="":
        return ""
    elif S[0]==T[0]:
        return S[0]+ver3(S[1:],T[1:])
    else:
        return ver3(S,T[1:])
def ver2(S,T):
    if S=="":
        return ""
    elif S[0] in T:
        return S[0]+ver2(S[1:],T)
    else:
        return ver2(S[1:],T)

def LCS(S,T):
    s1=ver2(S,T)
    s2=ver2(T,S)
    if s1 == "" or s2 == "":
        return "No common letters"
    elif s1==s2:
        return s1
    else:
        longs=len(ver3(s1,s2))
        if longs>len(s1)-longs:
            return ver3(s1,s2)
        else:
            return s1[len(ver3(s1,s2)):]
        #return s1+"   "+s2


print(LCS( 'human', 'chimp' ))#'hm'
print(LCS( 'gattaca', 'tacgaacta' ))#'gaaca'
print(LCS( 'wow', 'whew' ))#'ww'
print(LCS( '', 'whew' ) )  # first input is the empty string''
print(LCS( 'abcdefgh', 'efghabcd' ))#'abcd' 'efgh' would be an equally acceptable result.