__author__ = 'darakna'
from socket import getaddrinfo
import socket

def is_valid_domain(name):
    try:
        result = getaddrinfo(name, None)
        result=result[0][4][0]
    except:
        result="Fail"
    return (result)
print(is_valid_domain("app1.prod.collab.uhi.ac.uk"))
print(is_valid_domain("prod.collab.uhi.ac.uk"))
print(is_valid_domain("collab.uhi.ac.uk"))
print(is_valid_domain("uhi.ac.uk"))
print(is_valid_domain("ac.uk"))
a=getaddrinfo("8.8.8.8",None)
print(a)

#import socket
name, alias, addresslist = socket.gethostbyaddr('8.8.8.8')
print(name)