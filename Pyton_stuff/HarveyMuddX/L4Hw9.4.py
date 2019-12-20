__author__ = 'darakna'
###!!!WORKING!!!!
def ver(S,T,l=0):
    #print(S,T,l)
    if S=="" or T=="":
        return ""
    if S[0]== T[0]:
        #if len(ver(S[1:],T[1:],l+1))>len(ver(S,T[1:],l)):
        return S[0]+ver(S[1:],T[1:],l+1)
        #else:
        #    return ver(S,T[1:])
    elif S[0] in T:
        if len(ver(S[1:],T,l))>len(ver(S,T[1:],l)):
            return ver(S[1:],T)
        else:
            return ver(S,T[1:])
    else:
        return ver(S[1:],T)
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


print(LCS( 'human', 'chimp' ))#'hm'
print(LCS( 'gattaca', 'tacgaacta' ))#'gaaca'
print(LCS( 'wow', 'whew' ))#'ww'
print(LCS( '', 'whew' ) )  # first input is the empty string''
print(LCS( 'abcdefgh', 'efghabcd' ))#'abcd' 'efgh' would be an equally acceptable result.