import string

filehandler = open('input_str.txt', 'r')
text=filehandler.read()
new_text = []
for a in text:
    if a in "\n":
        new_text.append(a)
    elif a in string.ascii_uppercase:
        new_text.append(a)
new_text = "".join(new_text)

new_text = new_text.split("\n")

cmdlist = []
for command in new_text:
    if command not in cmdlist:
        cmdlist.append(command)

print(cmdlist)

take2 = text.split("\n")
for cmds in take2:
    if "LSHIFT" in cmds:
        print(cmds)


#print (string.ascii_uppercase)
#for i in range(ord('A'), ord('Z')+1):
#    print (chr(i))