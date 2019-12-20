import sys
path = r"D:\StarWarsProj\BD_chalange_04.2017\tst.jpg"
f = open(path, "rb")
chars = f.read()
total_chars = len(chars)
new_char = ""
print(total_chars)
print(chars[0])
#sys.exit()
last = ""
new_chr = ""
updated_chr = ""
for a in range(total_chars):
    if chars[a] in range(32,127):
        new_char += chr(chars[a])
        last = chr(chars[a])
        new_chr += last
    elif last != "\n":
        new_char += "\n"
        last = "\n"
    if len(new_chr) > 4 and last == "\n" and new_chr not in updated_chr:
        updated_chr += new_chr + last
        new_chr = ""
f.close()
g = open(r"D:\StarWarsProj\BD_chalange_04.2017\out.log", "w")
g.write(new_char)
g.close()
g = open(r"D:\StarWarsProj\BD_chalange_04.2017\new_out.log", "w")
g.write(updated_chr)
g.close()
print(new_char)
