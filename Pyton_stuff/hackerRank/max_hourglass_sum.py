import math
import os
import random
import re
import sys

# Print the largest (maximum) hourglass sum found in arr
'''
a b c
  d
e f g
'''
# Complete the hourglassSum function below.
def get_list_sum(arr, pos):
    return arr[0+pos] + arr[1+pos] + arr[2+pos] + arr[7+pos] + arr[12+pos] + arr[13+pos] + arr[14+pos]
def hourglassSum(arr):
    new_list_from_arr = [j for i in arr for j in i]
    base_sum = get_list_sum(new_list_from_arr,0)
    #print("Base sum: ", base_sum)
    for elem in [1,2,3,6,7,8,9,12,13,14,15,18,19,20,21]:
        new_sum = get_list_sum(new_list_from_arr,elem)
        #print("new_sum: ", new_sum)
        if new_sum > base_sum:
            #print("base_sum, new_sum",base_sum,new_sum)
            base_sum = new_sum
    return base_sum

print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]))
print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]))
print(hourglassSum([[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]))

