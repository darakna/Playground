__author__ = 'darakna'
import os
import re
from os import walk

extensions_list = [".mpeg", ".mpe",".mpg",".mpeg",".mpeg-1",".mpeg-2",".m1s",".mpa",".mp2"
                 ,".m2a",".mp2v",".m2v",".m2s",".avi",".mov",".qt",".asf",".asx",".wmv",".wma",\
                 ".wmx",".rm",".ra",".ram",".rmvb",".mp4",".3gp",".ogm",".mkv"]


listmov="Movie_list.txt"
outfile = open(listmov,"w")
search_path = "L:\\"
def list_files(outlist):           #returns a list of files (full path) of a given directory
    f = []
    for (dirpath, dirnames, filenames) in walk(outlist):
        for file in filenames:
            extension = re.findall("[.][0-9a-zA-Z-]*$",file)
            #print(extension)
            #print(re.findall("[.][0-9a-zA-Z-]*$",file)[0])
            #print(extensions_list)
            try:
                extension_0 = extension[0]
                if extension_0 in extensions_list:
                    print(file)
                    f.append(dirpath+"\\"+file)
            except:
                pass
    return f

def write_list(inlist,outfile):        #writes the list returned by list_files function in given parameter
    outfile = open(outfile,"w")
    for e in inlist:
        if re.findall("[.]([0-9a-zA-Z]*$)",e)[0] in extensions_list:
            outfile.write((e)+"\n")
    outfile.close()

#write_list(list_files(search_path),listmov)
for lines in list_files(search_path):
    outfile.write(lines)
    outfile.write("\n")