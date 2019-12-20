__author__ = 'vpaun'
import sys
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
def the_winner_is(stg):
    print("Problem:",stg)
    L=[decipher(stg,n) for n in range (26)]
    LoL = [rating(x) for x in L ]
    for i in range(len(L)):
        #print(L[i],LoL[i]) //for debug
        pass
    print("Solution:", L[LoL.index(max(LoL))])
    print ("\n")

def extended_caesar(list):
    fstream=open("out.txt","wb")
    for i in range(0,128):
        print (i+32,(chr(i+32)))
        cstring = u""
        for letter in list:
            if letter+i>160:
                cstring=cstring+chr(i+letter-128)
                #pass
            elif letter + i < 32:
                cstring = cstring + chr(160-letter - i)
            else:
                cstring=cstring+chr(letter+i)
                #pass
        print (cstring)
        fstream.write(("\n"+str(i)+"  "+str(rating(cstring))+"\n").encode('utf8'))
        fstream.write(cstring.encode('UTF-8'))
    fstream.close()

sta="Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc."
stb="Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk."
stc = "PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC KB YWAOWN WJZ UKQN QJEMQA OKHQPEKJ EO XJNLBYYBHJWA"
std = "60 08 08 7D 20 03 08 7B 45 20 12 08 0E 20 0C 08 05 0F 7E 7D 20 08 07 7E 20 06 08 0B 7E 20 7C 01 7A 05 05 7E 07 00 7E 20 02 07 20 12 08 0E 0B 20 03 08 0E 0B 07 7E 12 47 20 6D 01 02 0C 20 08 07 7E 20 10 7A 0C 20 7F 7A 02 0B 05 12 20 7E 7A 0C 12 20 0D 08 20 7C 0B 7A 7C 04 47 20 70 7A 0C 07 40 0D 20 02 0D 58 20 4A 4B 51 20 04 7E 12 0C 20 02 0C 20 7A 20 0A 0E 02 0D 7E 20 0C 06 7A 05 05 20 04 7E 12 0C 09 7A 7C 7E 45 20 0C 08 20 02 0D 20 0C 01 08 0E 05 7D 07 40 0D 20 01 7A 0F 7E 20 0D 7A 04 7E 07 20 12 08 0E 20 0D 08 08 20 05 08 07 00 20 0D 08 20 7D 7E 7C 0B 12 09 0D 20 0D 01 02 0C 20 06 7E 0C 0C 7A 00 7E 47 20 70 7E 05 05 20 7D 08 07 7E 45 20 12 08 0E 0B 20 0C 08 05 0E 0D 02 08 07 20 02 0C 20 7F 7C 01 7E 0B 7D 7F 7C 7F 7F 7D 08 47"
std_nospace = '6008087D2003087B452012080E200C08050F7E7D2008077E2006080B7E207C017A05057E07007E2002072012080E0B2003080E0B077E1247206D01020C2008077E20107A0C207F7A020B0512207E7A0C12200D08207C0B7A7C044720707A0C07400D20020D58204A4B5120047E120C20020C207A200A0E020D7E200C067A050520047E120C097A7C7E45200C0820020D200C01080E057D07400D20017A0F7E200D7A047E072012080E200D08082005080700200D08207D7E7C0B12090D200D01020C20067E0C0C7A007E4720707E0505207D08077E452012080E0B200C08050E0D02080720020C207F7C017E0B7D7F7C7F7F7D0847'

#std_str = map(ord, std_nospace.decode('hex'))
std_str=std.split(" ")
print(std_str)
std_int = []
for a in std_str:
    std_int.extend([int(a,16)])
print (std_int)
max = std_int[0]
for i in std_int:
    if max < i:
        max = i
print (max)
extended_caesar(std_int)

#the_winner_is(sta)
#the_winner_is(stb)
#the_winner_is(stc)



