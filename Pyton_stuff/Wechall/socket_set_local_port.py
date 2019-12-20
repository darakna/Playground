# Echo client program
import socket
import sys

HOST = 'www.wechall.net'    # The remote host
local = ''
cookie_vote = b"cookie_vote"
cookie_WeChall= b"cookie_WeChall"
req2 = b'GET https://www.wechall.net/challenge/training/net/ports/index.php HTTP/1.1\r\nHost: www.wechall.net\r\nCookie: VOTE=' + cookie_vote + b'; WC='+ cookie_WeChall + b'\r\n\r\n'
PORT = 80            # The same port as used by the server
local_port = 42
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.bind(('',local_port))
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
s.sendall(req2)
data = s.recv(10240)
data2 = s.recv(10240)
data3 = s.recv(10240)
data4 = s.recv(10240)
s.close()
print('Received', data.decode())
print('Received2', data2.decode())
print('Received3', data3.decode())
print('Received4', data4.decode())