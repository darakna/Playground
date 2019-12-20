__author__ = 'darakna'
r_file=open("LICENSE.txt",'r')
w_file=open("out.txt",'w')
w_file2=open("out2.txt",'w')
w_file3=open("out3.txt",'w')
inp=r_file.read()
norm=""
wild=""
for litera in inp:
    if not (ord(litera) > 64 and ord(litera) < 91 or ord(litera)>96 and ord(litera) < 123 or ord(litera) == 32 or ord(litera) == 10):
        wild=wild+litera
    else:
        norm=norm+litera
norm_list = norm.split()
norm_char= norm.strip()
norm_char2= norm_char.strip(" ")
norm_char3= norm_char2.strip("\n")
norm_dictionar= dict()
norm_dictionar2= dict()
for element in norm_list:
    norm_dictionar[element] = norm_dictionar.get(element, 0)+1
for element in norm_char3:
    norm_dictionar2[element] = norm_dictionar2.get(element, 0)+1
table_hour = sorted(norm_dictionar.items())
table_hour2 = sorted(norm_dictionar2.items())
table_reversed=sorted([(h, a) for a,h in table_hour],reverse=True)
table_reversed2=sorted([(h, a) for a,h in table_hour2],reverse=True)
#print(sorted([(h, a) for a,h in table_hour],reverse=True), file=w_file)
for h, a in table_reversed:
    print(a, " "*(40-len(a)),h, file=w_file)
for h, a in table_reversed2:
    print(a, " "*(40-len(a)),h, file=w_file2)
for h, a in table_hour2:
    print(h, " "*(40-len(h)),a, file=w_file3)