__author__ = 'darakna'
import re
def readfile(filename):
    readfile = open(filename)
    return readfile.read()
def num_list(text):
    return re.findall("[0-9]+",text)
def list_sum(list):
    testsum = 0
    for num in list:
        testsum+=int(num)
    return testsum
sample="sample_text.txt"
testfile = "regex_sum_42.txt"
hwfile = "regex_sum_175685.txt"

print(list_sum(num_list(readfile(sample))))
print(list_sum(num_list(readfile(testfile))))
print(list_sum(num_list(readfile(hwfile))))
