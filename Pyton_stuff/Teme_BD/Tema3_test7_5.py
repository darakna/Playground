__author__ = 'darakna'
__author__ = 'darakna'
import subprocess
from subprocess import PIPE
import threading
threadList = []
num_threads=5
proces_vanat="PyAppReadCons.exe"
mesaje_trimise=["test1", "test2", "test3", "exit"]
proc = subprocess.Popen(proces_vanat,stdin=PIPE,stdout=PIPE)
print ("...alocare ok...")
def trimite_mesaj(mesaj):
    proc.stdin.write((mesaj+"\n").encode('UTF-8'))
    proc.stdin.flush()
    print ("...trimitere mesaj proces:      ",mesaj)

def primeste_mesaj():
    print ("...initializare asteptare mesaj ")
    print(proc.stdout.read().decode("ASCII"))
    print ("... mesaj proces primit cu succes ")

    #proc.kill()
worker2=threading.Thread(target=primeste_mesaj,args=())
worker2.start()
threadList.append(worker2)
print ("...initializare bucla...")
for thread_ind in mesaje_trimise:
    print ("...start bucla cu parametru     ",mesaje_trimise.index(thread_ind))
    worker=threading.Thread(target=trimite_mesaj,args=(thread_ind,))
    worker.start()
    threadList.append(worker)
    print ("...stop bucla cu parametru      ",mesaje_trimise.index(thread_ind))

