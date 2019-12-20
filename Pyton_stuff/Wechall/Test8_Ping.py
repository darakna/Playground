__author__ = 'darakna'
from threading import Thread
import subprocess
from queue import *

num_threads = 4
queue = Queue()
ips = ["k.ro", "8.8.8.8"]
#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
            shell=True,
            #tdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT)
        if ret == 0:
            print ("%s: is alive" % ip)
        else:
            print ("%s: did not respond" % ip)
        q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit
queue.join()