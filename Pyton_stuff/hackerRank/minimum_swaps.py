#!/bin/python3
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#passing 14/14

import math
import os
import random
import re
import sys
import time


def genuineSwap2(arr, elem):
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
    while True:
        elem = 0
        while elem < len(arr):
            if arr[elem] == elem + 1:
                elem += 1
                continue
            elif arr[arr[elem] - 1] == elem + 1:
                swap_check, arr = genuineSwap2(arr, elem)
                if swap_check:
                    swaps += 1
                    elem += 1
            else:
                a = arr[elem]
                index_a = elem
                b = arr[arr[elem] - 1]
                index_b = arr[elem] - 1
                arr[index_a] = b
                arr[index_b] = a
                swaps += 1
                break
        if elem == len(arr):
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
