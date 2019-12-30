import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
#Print a single integer denoting the number of letter a's in the first "n" letters of the infinite string created by repeating "s" infinitely many times.
def repeatedString(s, n):
    subset_num = s.count("a")
    return n//len(s)*subset_num + s[0:n%len(s)].count("a")


print(repeatedString("abcac", 10))
print(repeatedString("aba", 10))
print(repeatedString("a", 1000000000000))