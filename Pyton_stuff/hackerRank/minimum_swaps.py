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

def minimumSwapsOv(arr):
    swp = 0
    n = len(arr)
    for i,j in enumerate(arr):
        if(j != i+1):
          source_idx = arr.index(i+1)
          destination_idx = arr.index(j)
          swp += 1
          arr[destination_idx], arr[source_idx] = arr[source_idx], arr[destination_idx]

    return swp

def minimumSwapsOv2(arr):
   i = 0
   swp = 0
   d = dict((val, idx) for val,idx in enumerate(arr))
   last = len(arr)-1
   while (True):
      value_idx = d[i]-1
      key = i
      if (d[i] != i+1):
         if value_idx == i+1:
            i+=1
         else:
            d[key],d[value_idx] = d[value_idx],d[key]
            swp +=1
      elif(d[i] == i+1):
         if(d[i] != last):
            i+=1
         else:
            break

   return swp

# Complete the minimumSwaps function below.
def minimumSwapsDbg(arr):
    nl = []
    for elem in arr:
        nl.append(elem)
    t1 = time.perf_counter_ns()
    min_swp = extendedSwap(arr)
    t2 = time.perf_counter_ns()
    min_swp2 = minimumSwapsOv2(nl)
    t3 = time.perf_counter_ns()
    print("List size: %s; Min inversions: %s; Duration in ms V: %s; Duration in ms O: %s; res V: %s; res O: %s" %(len(arr), min_swp, (t2 - t1) / 10 ** 6, (t3 - t2) / 10 ** 6, min_swp, min_swp2))
    return min_swp

def minimumSwaps(arr):
    min_swp = minimumSwapsDbg(arr)
    return min_swp


arr1 = [7, 1, 3, 2, 4, 5, 6]
arr1_num = 5
arr2 = [4, 3, 1, 2]
arr2_num = 3
arr3 = [2, 3, 4, 1, 5]
arr3_num = 3
arr4 = [1, 3, 5, 2, 4, 6, 7]
arr4_num = 3
arr5_num = 49990

print(arr1_num, " == ", minimumSwaps(arr1))
print(arr2_num, " == ", minimumSwaps(arr2))
print(arr3_num, " == ", minimumSwaps(arr3))
print(arr4_num, " == ", minimumSwaps(arr4))

f = open("input09_minimum_swaps.txt", "r")
lines = f.read().split("\n")
q = list(map(int, lines[1].rstrip().split()))
print(arr5_num, " == ", minimumSwaps(q))

f = open("input07_bribe_fail.txt", "r")
lines = f.read().split("\n")
q = list(map(int, lines[2].rstrip().split()))
#print(minimumSwaps(q))
