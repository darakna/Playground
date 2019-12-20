__author__ = 'darakna'
import os,subprocess
ips = ["k.kro", "google.ro"]#, "example.com","ele.ool"]
def pingping(host):
    response = os.system("ping -n 5 " + host)
    print(response)
    if response == 0:
        print (host, 'is up!')
    else:
        print (host, 'is down!')

for ip in ips:
    #pingping(ip)
    pass
#chost=subprocess.run("ping -n 5 " + "k.ro")
#print("Test")
#print(chost)

#with subprocess.run("ping -n 5 " + "k.ro"):
#    print("Test1")
#    print(proc.stdout.read())
#    Print("Test2")

