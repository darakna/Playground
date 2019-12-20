__author__ = 'vpaun'
import os
pid_name="calc.exe"
tmp_location="D:\DllsList.txt"
os.system('listdlls '+pid_name + " >>"+tmp_location)
readFileTemp=open(tmp_location)
if "injct64.dll" in readFileTemp.read():
    print("Simulator injection found in ",pid_name)
else:
    print("Simulator injection not found in",pid_name)
readFileTemp.close()
os.remove(tmp_location)
print(ord("®"))