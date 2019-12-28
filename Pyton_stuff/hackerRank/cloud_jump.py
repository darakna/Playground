#!/bin/python3
#8/8 tests

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    min_jumps = 0
    all_clouds = len(c)
    current_pos = 0
    while(current_pos != all_clouds):
        print(all_clouds, current_pos)
        if current_pos + 2 == all_clouds-1:
            min_jumps += 1
            break
        elif current_pos + 1 == all_clouds - 1:
            min_jumps += 1
            break
        elif c[current_pos + 2] == 0:
            current_pos = current_pos + 2
            min_jumps += 1
        elif c[current_pos + 1] == 0:
            current_pos = current_pos + 1
            min_jumps += 1


    return min_jumps


print("4=",jumpingOnClouds(list(map(int, "0 0 1 0 0 1 0".rstrip().split()))))
print("3=",jumpingOnClouds(list(map(int, "0 0 0 1 0 0".rstrip().split()))))
