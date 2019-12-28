#21/21 test passed

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_num = 0
    level = 0
    print(n, s)
    for elem in range(n):
        if s[elem] == "D":
            level  -= 1
        elif s[elem] == "U":
            level += 1
        print(level)
        if level == 0 and s[elem] == "U":
            print(n,elem, s[elem])
            valley_num += 1
    return valley_num

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = os.getcwd() + "\\outfile.log"
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    n = 12
    #s = input()
    s = "DDUUDDUDUUUD"
    result = countingValleys(n, s)

    #fptr.write(str(result) + '\n')
    print(str(result))
    #fptr.close()
