__author__ = 'darakna'

def ind( e, L ):
    if not e in L:
        return len(L)
    else:
        for elements in L:
            if e==elements:
                return L.index(elements)

#
# Tests
#
print ("ind( 42, [ 55, 77, 42, 12, 42, 100 ])  2 ==", ind( 42, [ 55, 77, 42, 12, 42, 100 ]))
print ("ind(42, range(0,100))                  42 ==", ind(42, range(0,100)))
print ("ind('hi', [ 'hello', 42, True ])       3 ==", ind('hi', [ 'hello', 42, True ]))
print ("ind('hi', [ 'well', 'hi', 'there' ])   1 ==", ind('hi', [ 'well', 'hi', 'there' ]))
print ("ind('i', 'team')                       4 ==", ind('i', 'team'))
print ("ind(' ', 'outer exploration')          5 ==", ind(' ', 'outer exploration'))