__author__ = 'darakna'
from time import *
import threading
threadList = []
nameList = ["One", "Two", "Three", "Four", "Five"]
num_threads=10
def wait_and_print(worker):
    print(worker," starting work")
    print(threadList)
    sleep(3)
    print(worker, " finished")
for thread_ind in range(num_threads):
    worker=threading.Thread(target=wait_and_print,args=(thread_ind,))
    worker.start()
    threadList.append(worker)