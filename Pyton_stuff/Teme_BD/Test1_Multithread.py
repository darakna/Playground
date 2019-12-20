__author__ = 'darakna'
from threading import Thread
import subprocess,os
from queue import *

num_threads = 10
queue = Queue()
ips = ["k.ro", "google.ro", "example.com"]
def pinger(i, q):
    print(i," ??? ",q)
    response = os.system("ping -n 1 " + ip)
for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
for ip in ips:

    pinger(ip,queue)
    queue.put(ip)
   # Wait until worker threads are done to exit
    queue.join()