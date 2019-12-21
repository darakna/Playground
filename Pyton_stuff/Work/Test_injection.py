__author__ = 'darakna'
import os
import subprocess
import sys
import time
tested_proc=r"c:\windows\system32\calc.exe"
listdlls_location=r"D:\WORK\MagicWandTools\#1SysinternalsSuite\listdlls.exe"
injected_dll_name = "injct"
domain_char_list=list(range(1,127))
if os.path.isfile(tested_proc) is False:
    print(tested_proc, " not found, script will not work ")
else:
    print(tested_proc, " found")
if os.path.exists(listdlls_location) is False:
    print(listdlls_location, " not found, script will not work ")
else:
    print(listdlls_location, "found")

def stripall(word):
    if word=="":
        return ""
    else:
        if ord(word[0]) in domain_char_list:
            return word[0]+stripall(word[1:])
        else:
             return stripall(word[1:])
def verify_(nume):
    var1=os.popen(listdlls_location+' -v '+nume).read()
    var=""
    for chars in var1:
        var=var+stripall(chars)
    if "injct" in var:
        print(var[
          var[:var.index(injected_dll_name)].rindex("\n")
          :
          var[:var.index(injected_dll_name)+var[var.index(injected_dll_name)+12:].index("dll")].rindex("\n")
          ])
    else:
        print("Injection not found")
def pornire_proces(nume):
    return subprocess.Popen(nume)
proc=pornire_proces(tested_proc)
verify_(tested_proc[tested_proc.rindex("\\")+1:])
if proc.poll()!=0:
    proc.kill()
time.sleep(3)

