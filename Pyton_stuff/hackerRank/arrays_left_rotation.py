#Print a single line of len(a) space-separated integers denoting the final state of the array after performing d left rotations.
# Complete the rotLeft function below.
def rotLeft(a, d):
    new_start_pos = d%len(a)
    return a[new_start_pos:] + a[:new_start_pos]

print(rotLeft([1, 2, 3, 4, 5], 4))
print(rotLeft([1, 2, 3, 4, 5], 5))
print(rotLeft([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10))
print(rotLeft([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97], 13))