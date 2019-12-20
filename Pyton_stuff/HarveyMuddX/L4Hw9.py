__author__ = 'darakna'
###FAIL###
def LCS(S,T):
    pass
def substrings(arr,n):
    #passw
    #j
    #start
    #end
    no_of_strings = n-1;

    for passw in range(n):
        start = 0
        end = start+passw;
        for j in range (no_of_strings,0,-1):
            print(arr[start: end])
            start=start+1
            end = start+passw
        no_of_strings=no_of_strings-1
print(substrings( 'human', len("human")))#'hm'
#print(substrings( 'human', 'chimp' ))#'hm'
#print(LCS( 'gattaca', 'tacgaacta' ))#'gaaca'
#print(LCS( 'wow', 'whew' ))#'ww'
#print(LCS( '', 'whew' ) )  # first input is the empty string''
#print(LCS( 'abcdefgh', 'efghabcd' ))#'abcd'