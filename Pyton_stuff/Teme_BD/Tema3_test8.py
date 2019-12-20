__author__ = 'darakna'
import subprocess
from subprocess import PIPE
import threading
threadList = []
num_threads=5
#proces_vanat="PyAppReadCons.exe"
mesaje_trimise=["test1", "test2", "test3", "exit"]
proc = subprocess.Popen("PyAppReadCons.exe",stdin=PIPE,stdout=PIPE)