__author__ = 'darakna'


import os
hostname = "www.k.ro" #example
response = os.system("ping -n 1 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')