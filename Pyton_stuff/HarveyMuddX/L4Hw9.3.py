__author__ = 'darakna'
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
    if S==T=="":
        return "No common letters"
    elif S==T:
        return S
    if S[0] != T[0]:
        return LCS(S,T[1:])
    elif LCS(S,T[1:]):
        return LCS(S,T[1:])
    else:
        return S[0] + LCS(S[1:],T[1:])
print(LCS( 'human', 'chimp' ))#'hm'
print(LCS( 'gattaca', 'tacgaacta' ))#'gaaca'
print(LCS( 'wow', 'whew' ))#'ww'
print(LCS( '', 'whew' ) )  # first input is the empty string''
print(LCS( 'abcdefgh', 'efghabcd' ))#'abcd' 'efgh' would be an equally acceptable result.