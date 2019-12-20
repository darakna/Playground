__author__ = 'darakna'
def letterScore( let ):
    let=let.lower()
    if let < 'a' or let > 'z':
        return 0
    else:
        if let in 'aeilnorstu': #1 point
            return 1
        elif let in 'dg': # 2 points
            return 2
        elif let in 'bcmp': # 3 points
            return 3
        elif let in 'fhvwy': # 4 points
            return 4
        elif let in 'k': #5 points
            return 5
        elif let in 'jx': # 8 points
            return 8
        elif let in 'qz': # 10 points
            return 10
def scrabbleScore(strng):
    if strng=='':
        return 0
    else:
        return letterScore(strng[0])+scrabbleScore(strng[1:])

#
# Tests
#
print ("scrabbleScore('quetzal'):  25 ==", scrabbleScore('quetzal'))
print ("scrabbleScore('jonquil'):  23 ==", scrabbleScore('jonquil'))
print ("scrabbleScore('syzygy'):   25 ==", scrabbleScore('syzygy'))
print ("scrabbleScore('abcdefghijklmnopqrstuvwxyz'):  87 ==", scrabbleScore('abcdefghijklmnopqrstuvwxyz'))
print ("scrabbleScore('?!@#$%^&*()'):  0 ==", scrabbleScore('?!@#$%^&*()'))
print ("scrabbleScore(''):          0 ==", scrabbleScore(''))

