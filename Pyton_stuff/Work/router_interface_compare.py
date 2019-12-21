__author__ = 'darakna'
import re
from os import walk
import codecs
listext=["txt","html","css","js"]
r1 = "files1.txt"
r2 = "files2.txt"
rap="raport.txt"
path1="Pass1"
path2="Pass2"
domain_char_list=list(range(1,127))

def same_files(s1,s2):
    rapo=open(rap,"w")
    for line1, line2 in zip(s1, s2):

        if line1[line1.index("\\")+1:] == line2[line2.index("\\")+1:]:
            print(line1[line1.index("\\")+1:])
            try:
                tmp1=open(line1)
                tmp2=open(line2)
                txt1=tmp1.read()
                txt2=tmp2.read()
            except:
                tmp1=codecs.open(line1, "r", "utf-16-le")
                tmp2=codecs.open(line2, "r", "utf-16-le")
                txt1=tmp1.read()
                txt2=tmp2.read()

            len1=len(txt1)
            len2=len(txt2)
            llen1=len(str(len1))
            llen2=len(str(len2))
            rapo.write("File"+" "*int((110-len(line1))/2)+line1+" "*int(100-len(line1))+line1+" "*int(100-len(line1))+"\n")
            rapo.write("Characters:"+ " "*40 + str(len1) + " "*100+ str(len2)+"\n")

            for index in range(len(txt1)):
                if txt1[index] != txt2[index]:
                    rapo.write("Differences:"+ " "*40 + txt1[index] + " "*100+ txt2[index]+"\n")
                try:
                    if ord(txt1[index]) not in domain_char_list:
                        rapo.write("Differences:"+ " "*40 + txt1[index] + " "*100+ txt2[index]+" "*15 + str(index) +"\n")
                except:
                    rapo.write("Differences:"+ " "*40 + txt1[index] + " "*100+ txt2[index]+" "*15 + str(index) +"\n")
            rapo.write("\n")



        else:
            print("Pass")


def list_files(outfile):           #returns a list of files (full path) of a given directory
    f = []
    for (dirpath, dirnames, filenames) in walk(outfile):
        for file in filenames:
            f.append(dirpath+"\\"+file)
    return f
def write_list(inlist,rout):        #writes the list returned by list_files function in given parameter
    outfile = open(rout,"w")
    for e in inlist:
        if re.findall("[.]([0-9a-zA-Z]*$)",e)[0] in listext:
            outfile.write((e)+"\n")
    outfile.close()
def compare_r(f1,f2):
    rout1 = open(f1)
    rout2 = open(f2)
    r1=rout1.read()
    r2=rout2.read()
    same_files(r1.split("\n")[:-1],r2.split("\n")[:-1])

write_list(list_files(path1),r1)
write_list(list_files(path2),r2)
compare_r(r1,r2)
