__author__ = 'darakna'
import subprocess,datetime
ips = ["k.ro", "google.ro", "example.com","wiki.com"]
def perftest(hostname):
    start_time=datetime.datetime.now()
    subprocess.run("ping -n 1 " + hostname)
    stop_time=datetime.datetime.now()
    return stop_time-start_time

for ip in ips:
    print(perftest(ip))