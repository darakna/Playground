__author__ = 'darakna'
def exact_change( target_amount, L ):
    if target_amount==0:
        return True
    if not L:
        return False
    if target_amount<L[0]:
        return exact_change(target_amount,L[1:])
    elif exact_change(target_amount,L[1:]):
        return exact_change(target_amount,L[1:])
    else:

        return exact_change(target_amount-L[0],L[1:])




print(exact_change( 42, [25, 16, 16,1,16, 25, 10, 5, 1] ))#True
print(exact_change( 42, [25, 1, 25, 10, 5] ))#False
print(exact_change( 42, [23, 1, 23, 100] ))#False
print(exact_change( 42, [23, 17, 2, 100] ))#True
print(exact_change( 42, [25, 16, 2, 15] ))#True # needs to be able to "skip" the 16
print(exact_change( 0, [4, 5, 6] ))#True
print(exact_change( -47, [4, 5, 6] ))#False
print(exact_change( 0, [] ))#True
print(exact_change( 42, [] ))#False
print(exact_change(22,[1, 5, 8, 4, 3, 6, 8, 9, 7, 10, 5]))