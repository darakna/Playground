__author__ = 'darakna'
import os.path
import shutil
cale_fisier_citire="BDFLT_times.txt"
if os.path.exists(cale_fisier_citire) is True:
    filehandler = open(cale_fisier_citire)
else:
    cale_fisier_citire=input("Fisierul "+cale_fisier_citire+" nu a fost gasit. Introdu cale si nume fisier citire:")
    filehandler = open(cale_fisier_citire)
filehandler_w=open("Files_not_found.txt",'w')
stream_read=filehandler.readlines()
lines_number=0
index_f=0
index_v=0
for line in stream_read:
    lines_number=lines_number+1
    cale_inceput = 9
    cale_final = line.find("------")-1
    cale_origine=line[cale_inceput:cale_final]
    cale_destinatie="Dest_Folder"+line[cale_inceput+2:cale_final]
    #print (cale_origine,cale_destinatie)
    if os.path.exists(cale_origine) is True:
        if not os.path.exists(cale_destinatie[:cale_destinatie.rfind("\\")]):
            os.makedirs(cale_destinatie[:cale_destinatie.rfind("\\")])
        shutil.copyfile(cale_origine, cale_destinatie)
        index_v=index_v+1
    else:
        filehandler_w.write(str(index_f))
        index_f=index_f+1
        filehandler_w.write(" ")
        filehandler_w.write(cale_origine)
        #time_position=line.find("------ Time ")+12
        filehandler_w.write(line[cale_final+12:])
cale_script=os.path.abspath(__file__)
print("Directorul scriptului este:",cale_script,"Numarul de fisiere copiate este:",index_v)
#print(lines_number)
