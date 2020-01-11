#!/bin/python3
#passing 8/14

import math
import os
import random
import re
import sys
import time

def check_if_sorted(q):
    for elem in range(len(q[:-1])):
        if q[elem] > q[elem + 1]:
            return False
    return True


def genuineSwap(arr):
    for elem in range(len(arr)):
        if arr[elem] == elem + 1:
            continue
        if arr[arr[elem] - 1] == elem + 1:
            a = arr[elem]
            index_a = elem
            b = arr[arr[elem] - 1]
            index_b = arr[elem] - 1
            arr[index_a] = b
            arr[index_b] = a
            return True, arr
    return False, arr


def extendedSwap(arr):
    swaps = 0
    while not check_if_sorted(arr):
        swap_check, arr = genuineSwap(arr)
        if swap_check:
            swaps += 1
            continue
        for elem in range(len(arr)):
            if arr[elem] == elem + 1:
                continue
            else:
                a = arr[elem]
                index_a = elem
                b = arr[arr[elem] - 1]
                index_b = arr[elem] - 1
                arr[index_a] = b
                arr[index_b] = a
                swaps += 1
                break

    return swaps

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    min_swp = extendedSwap(arr)
    return min_swp

arr1 = [7, 1, 3, 2, 4, 5, 6]
arr1_num = 5
arr2 = [4, 3, 1, 2]
arr2_num = 3
arr3 = [2, 3, 4, 1, 5]
arr3_num = 3
arr4 = [1, 3, 5, 2, 4, 6, 7]
arr4_num = 3

print(arr1_num, " == ", minimumSwaps(arr1))
print(arr2_num, " == ", minimumSwaps(arr2))
print(arr3_num, " == ", minimumSwaps(arr3))
print(arr4_num, " == ", minimumSwaps(arr4))
