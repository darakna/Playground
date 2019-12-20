__author__ = 'darakna'
import os
os.system('WMIC /OUTPUT:D:\ProcessList.txt PROCESS get Caption,Commandline,Processid')
f = open("D:\ProcessList.txt")
plist = f.readlines()
f.close()