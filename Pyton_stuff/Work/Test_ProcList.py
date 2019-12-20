__author__ = 'darakna'
import subprocess
cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    #print(line)
    pass

import os
os.system('WMIC /OUTPUT:D:\ProcessList.txt PROCESS get Caption,Commandline,Processid')
f = open("D:\ProcessList.txt")
plist = f.readlines()
f.close()


pid_name="Calculator.exe"
import os
os.system('D:\Dropbox\@Munca\WORK\MagicWandTools\#1SysinternalsSuite\listdlls '+pid_name)