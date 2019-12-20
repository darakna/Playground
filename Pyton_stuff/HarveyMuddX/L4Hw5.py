__author__ = 'darakna'
# table of probabilities for each letter
def letProb( c ):
  """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
  """
  if c == ' ': return 0.1904
  if c == 'e' or c == 'E': return 0.1017
  if c == 't' or c == 'T': return 0.0737
  if c == 'a' or c == 'A': return 0.0661
  if c == 'o' or c == 'O': return 0.0610
  if c == 'i' or c == 'I': return 0.0562
  if c == 'n' or c == 'N': return 0.0557
  if c == 'h' or c == 'H': return 0.0542
  if c == 's' or c == 'S': return 0.0508
  if c == 'r' or c == 'R': return 0.0458
  if c == 'd' or c == 'D': return 0.0369
  if c == 'l' or c == 'L': return 0.0325
  if c == 'u' or c == 'U': return 0.0228
  if c == 'm' or c == 'M': return 0.0205
  if c == 'c' or c == 'C': return 0.0192
  if c == 'w' or c == 'W': return 0.0190
  if c == 'f' or c == 'F': return 0.0175
  if c == 'y' or c == 'Y': return 0.0165
  if c == 'g' or c == 'G': return 0.0161
  if c == 'p' or c == 'P': return 0.0131
  if c == 'b' or c == 'B': return 0.0115
  if c == 'v' or c == 'V': return 0.0088
  if c == 'k' or c == 'K': return 0.0066
  if c == 'x' or c == 'X': return 0.0014
  if c == 'j' or c == 'J': return 0.0008
  if c == 'q' or c == 'Q': return 0.0008
  if c == 'z' or c == 'Z': return 0.0005
  return 1.0
def rating(L):
    if len(L) == 0:
        return 0
    else:
        return letProb(L[0])+rating(L[1:])
def decipher(S,n):
    if len(S)==0:
        return ""
    else:
        if ord(S[0]) in range(ord('A'),ord('Z')+1):
            if ord(S[0])+n > ord('Z'):
                return chr(ord(S[0])-26+n) + decipher(S[1:],n)
            else:
                return chr(ord(S[0])+n)+ decipher(S[1:],n)
        elif ord(S[0]) in range(ord('a'),ord('z')+1):
            if ord(S[0])+n > ord('z'):
                return chr(ord(S[0])-26+n) + decipher(S[1:],n)
            else:
                return chr(ord(S[0])+n)+ decipher(S[1:],n)
        else:
            return S[0]+decipher(S[1:],n)
#stg="Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc."
stg="Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk."
L=[decipher(stg,n) for n in range (26)]
LoL = [rating(x) for x in L ]
for i in range(len(L)):
    print(L[i],LoL[i])
print(L[LoL.index(max(LoL))])

