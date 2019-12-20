__author__ = 'darakna'
from socket import *
import socket
fname = ""# input("Enter file name: ")
ip_valid = open('ip_valid.txt','w')
hostname_valid=open('hostname_valid.txt','w')
if fname!="mbox-short.txt":
    fname="mbox-short.txt"
fh = open(fname)
TLD=open("TLD_suffix.txt")
TLD_words=TLD.read()
domain_char_list=list(range(45,47))+list(range(48,58))+list(range(65,91))+list(range(97,123))
lcounter=0
dcounter=0
wcounter=0
wdcounter=0
wdpcounter=0
wordlist={}
domain_dict={}
hostnames=[]
ips=[]
def discover_superdomains(words):
    while words.count(".")>=1:
        print(words,newword,is_valid_domain(words),is_valid_ip(words))
        if is_valid_domain_verify(words):
            wordlist[is_valid_domain_verify(words)]=words
            words=domain_short(words)

def define_domain_dict():
    res = {}
    ord=0
    with open("TLD_suffix.txt","r") as text:
        for line in text:
            value = line
            res[line[:-1]] = value[:-1]
            ord=ord+1
    return res
domain_dict=define_domain_dict()
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
def is_valid_ip(ip):
    """Validates IP addresses.
    """
    return is_valid_ipv4_address(ip) or is_valid_ipv6_address(ip)
def is_valid_domain(adress):
    dpos=adress.rfind(".")
    if adress[dpos+1:]=="":
        return False
    if adress[dpos+1:].upper() in domain_dict:
        return True
    else:
        return False
def ip_has_domain(ip):
    try:
        name, alias, addresslist = socket.gethostbyaddr(ip)
    except:
        name=False
    return name
def stripall(word):
    if word=="":
        return ""
    else:
        if ord(word[0]) in domain_char_list:
            return word[0]+stripall(word[1:])
        else:
            return stripall(word[1:])
def stripdomain(dword):
    tp=dword[dword.index("://")+3:]
    tp=tp[:tp.index("/")]
    return tp
#from socket import getaddrinfo
#import socket

def is_valid_domain_verify(name):
    try:
        result = getaddrinfo(name, None)
        result=result[0][4][0]
    except:
        result="Fail"
    return (result)
def domain_short(words):
    return words[words.index(".")+1:]
for line in fh:
    lcounter=lcounter+1
    if "." not in line:
        continue
    for words in line.split():
        wcounter=wcounter+1
        if "." not in words:
            continue
        wdcounter=wdcounter+1
        newword="???!!!???"
        if "@" in words:
            newword=words
            words=words[words.index("@")+1:]
            wdpcounter=wdpcounter+1
        if "://" in words:
            newword=words
            words=stripdomain(words)
        newword=words
        words=stripall(words)
        if  is_valid_ip(words):
            if words not in ips:
                ips.append(words)
                ip_valid.write(words+"\n")
        elif is_valid_domain(words):
            if words not in hostnames:
                hostnames.append(words)
                hostname_valid.write(words+"\n")
            #if words not in wordlist:
                #if is_valid_ip(words):
                #    print(words,newword,is_valid_domain(words),is_valid_ip(words))
                #    if ip_has_domain(words):
                #        discover_superdomains(ip_has_domain(words))
                    #wordlist[words]="No_Valid_Domain"
                #elif is_valid_domain(words):
                 #   discover_superdomains(words)
            print(words)

    pos=line.find(".")
    #print(line)
    dcounter=dcounter+1
for key in wordlist:
    print(wordlist[key]," "*(50-len(wordlist[key])),key)
print(lcounter,dcounter,wcounter,wdcounter,wdpcounter)
#print(TLD_words)