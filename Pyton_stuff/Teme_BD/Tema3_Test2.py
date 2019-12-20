__author__ = 'darakna'
#import wmi
#c = wmi.WMI ()

#for process in c.Win32_Process ():
#  print (process.ProcessId, process.Name)
import subprocess
cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    print(line)