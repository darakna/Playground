__author__ = 'darakna'
import subprocess
from subprocess import PIPE
proces_vanat="pyappreadcons.exe"
mesaje_trimise=["test1", "test2", "test3", "exit"]
print ("Test    1")
proc = subprocess.Popen(proces_vanat,stdin=PIPE,stdout=PIPE)
print ("Test    2")



proc.stdin.Pope(mesaje_trimise[0].encode('UTF-8'))
print ("Test    3")

a=proc.stdout.read()
print ("Test    4")
print (a)
proc.kill()