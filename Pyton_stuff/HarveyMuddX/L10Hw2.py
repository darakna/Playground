__author__ = 'darakna'
import socket

server1 = 'www.py4inf.com'
server2 = "www.k.ro"
server4 = "www.google.ro"
server3 = "www.pythonlearn.com"
server5 = "capitalplaza.ro"
server6 = "darakna.go.ro"


command1 = "GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n"
command2 = "GET http://www.k.ro HTTP/1.1\n host: www.k.ro \n User-Agent: Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.3.1)\n Connection: Keep-Alive\n"
command3 = "GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n"
command4 = "GET / HTTP/1.1\n\n"
command5 = "GET / HTTP/1.1\n" \
        "Host: capitalplaza.ro\n"  \
        "Connection: keep-alive\n" \
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\n"\
        "Upgrade-Insecure-Requests: 1\n"\
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7\n"\
        "Accept-Encoding: gzip, deflate, sdch\n"\
        "Accept-Language: en-US,en;q=0.8,ro;q=0.6,fr;q=0.4,de;q=0.2\n\n"\
        #"Cookie: trafic_h=a7b80b9al658558c1c0cd5e733899514*1442412248*k.ro*1446047192*1446216904*4\n"


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((server5, 80))
mysock.send(command5.encode('utf-16'))

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        #print (data.decode())
        break
    print (data.decode())
    #print(command5)
mysock.close()