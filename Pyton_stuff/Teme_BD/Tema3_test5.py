__author__ = 'darakna'
import subprocess
from subprocess import PIPE
import threading
import time
threadList = []
num_threads=5
proces_vanat="PyAppReadCons.exe"
mesaje_trimise=["test1", "test2", "test3", "exit"]
print ("...alocare ok...")
def pornire_proces(nume):
    return subprocess.Popen(nume,stdin=PIPE,stdout=PIPE)
def trimite_mesaj(mesaj):
    proc.stdin.write((mesaj+"\n").encode('UTF-8'))
    proc.stdin.flush()
    print ("...trimitere mesaj proces:      ",mesaj)

def primeste_mesaj():
    print ("...initializare asteptare mesaj ")
    print("...Mesaj:                       ",proc.stdout.read().decode("ASCII")[:-1])
    print ("...mesaj proces primit cu succes \n")

print ("...initializare bucla...")
for thread_ind in mesaje_trimise:
    proc = pornire_proces(proces_vanat)
    print ("...start bucla cu parametru     ",mesaje_trimise.index(thread_ind))
    worker=threading.Thread(target=trimite_mesaj,args=(thread_ind,))
    worker.start()
    threadList.append(worker)
    worker2=threading.Thread(target=primeste_mesaj,args=())
    worker2.start()
    threadList.append(worker2)
    print ("...stop bucla cu parametru      ",mesaje_trimise.index(thread_ind))
    time.sleep(0.1)
    if proc.poll()!=0:
        proc.kill()
    time.sleep(0.5)

