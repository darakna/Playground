__author__ = 'darakna'
def mylen( s ):
    if s == '':
        return 0
    else:
        return 1 + mylen( s[1:] )

test = mylen("test1234")
print ('test is', test)

def flipside(s):
   """ flipside swaps s's sides
       input s: a string
   """
   x = int(len(s)/2)
   return s[x:] + s[:x]

#
# Tests
#
print (r"flipside('carpets')    petscar ==", flipside('carpets'))
print ("flipside('homework')  workhome ==", flipside('homework'))
print ("flipside('flipside')  sideflip ==", flipside('flipside'))
print ("flipside('az')              za ==", flipside('az'))
print ("flipside('a')                a ==", flipside('a'))
print ("flipside('')                   ==", flipside(''))