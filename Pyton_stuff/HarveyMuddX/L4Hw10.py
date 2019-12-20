__author__ = 'darakna'
###!!!!WORKING!!!!
def exact_change( target_amount, L):
    if target_amount==0:
        return True
    if not L:
        return False
    if target_amount<L[0]:
        return exact_change(target_amount,L[1:])
    elif exact_change(target_amount,L[1:]):
        return exact_change(target_amount,L[1:])
    else:
        #if TA==0: print("Test",L[0])
        #a=L[0]
        #tmp=L[0]
        #S.append(L[0])
        return exact_change(target_amount-L[0],L[1:])
def enum(targ,amount):
    if targ!=0 and amount==[]:
        return [False]
    if amount==[]:
        return [True]
    if exact_change(targ,amount)==False:
        return [False]
    elif exact_change(targ-amount[0],amount[1:])==True:
        return [amount[0]] + enum(targ-amount[0],amount[1:])
    else:
        return enum(targ,amount[1:])



print(enum( 42, [25, 16, 16,1,16, 25, 10, 5, 1]))#True
print(enum( 42, [25, 1, 25, 10, 5] ))#False
print(enum( 42, [23, 1, 23, 100] ))#False
print(enum( 42, [23, 17, 2, 100] ))#True
print(enum( 42, [25, 16, 2, 15] ))#True # needs to be able to "skip" the 16
print(enum( 0, [4, 5, 6] ))#True
print(enum( -47, [4, 5, 6] ))#False
print(enum( 0, [] ))#True
print(enum( 42, [] ))#False
print(enum(22,[1, 5, 8, 4, 3, 6, 8, 9, 7, 10, 5]))