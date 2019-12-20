__author__ = 'darakna'
def ver(S,T):
    print(S,T)
    if T==""or S=="":
        return ""
    elif S[0]==T[0]:
        print("Bing")
        if len(ver(S[1:],T[:1]))>len(ver(S,T[1:]))+1:
            return S[0]+ver(S[1:],T[1:])
        else:
            return ver(S[1:],T[1:])
    elif S[0] not in T:
        print("????")
        return ver(S[1:],T)
    elif S[0] in T[1:]:
        return ver(S,T[1:])
    else:
        return ""
def sep(S,T):
    if S=="":
        pass
    else:
        pass

def ver2(S,T):
    if S=="":
        return ""
    elif S[0] in T:
        return S[0]+ver2(S[1:],T)
    else:
        return ver2(S[1:],T)
def LCS(S,T):
    S=ver2(S,T)
    T=ver2(T,S)
    #print(S,T)
    if S==T=="":
        return "No common letters"
    elif S==T:
        return S
    else:
        return ver(S,T)


#print(LCS( 'human', 'chimp' ))#'hm'
print(LCS( 'gattaca', 'tacgaacta' ))#'gaaca'
#print(LCS( 'wow', 'whew' ))#'ww'
#print(LCS( '', 'whew' ) )  # first input is the empty string''
#print(LCS( 'abcdefgh', 'efghabcd' ))#'abcd' 'efgh' would be an equally acceptable result.