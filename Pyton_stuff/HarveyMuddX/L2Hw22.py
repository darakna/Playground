__author__ = 'darakna'
# python 2
#
# Homework 2, Problem 2
#
# Name:
# Date:
#

def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x
print(dbl("spam"))

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

def sq(x):
    return x*x
print(sq(5))

def interp(low,hi,fraction):#floating point
    return ((hi-low)*fraction)+low
print(interp(102,117,-4))

def checkends(strh):
    if strh[0]==strh[-1]:
        return True
    else:
        return False
def flipside(s):
    return s[int(len(s)/2):]+s[:int(len(s)/2)]

def convertFromSeconds(s):
    secs=s%60
    minu=int(s/60)%60
    hour=int(s/60/60)%24
    days=int(s/60/60/24)
    return [days,hour,minu,secs]
def front3(str):

  return str[:3]*3

def pigletLatin(tringsay):
    if tringsay=="": return ""
    elif tringsay[0] in "aeiouy":
            return tringsay+"way"
    else: return tringsay[1:]+tringsay[0]+"ay"





def cons_check(stringg):
    print("string:",stringg)
    if stringg[1] in "aeiou":
        return stringg[1:]+stringg[0]
    else:
        return cons_check(stringg[1:]+stringg[0])





def TruepigletLatin(tringsay):
    if tringsay=="": return ""
    elif tringsay[0] in "aeiou":
            print("else1")
            return tringsay+"way"
    elif tringsay[0]=="y":
        print("else2")
        if tringsay[1] in "aeiou":return tringsay[1:]+tringsay[0]+"ay"
        else: return tringsay+"way"
    else:
        print("else3")
        return cons_check(tringsay)+"ay"

print(TruepigletLatin("string"))
print(convertFromSeconds(63113852*2))

