__author__ = 'darakna'
#!/usr/bin/python

# Objective of the script:
# - Create a sorted view for psscan output
# - Identify the processes that are currently located in pslist
# - Number the processes in the order they appear in psscan
# - Sort by PIDs in the psscan output

# Modify the below files for the output that you receive from volatility
psscanFile='txt.psscan'  # Generated with the psscan volatility 2.4 plugin
pslistFile='txt.pslist-P' # Generated with the pslist -P volatility 2.4 plugin # -P gives you the physical offset instead of the virtual

# Offset(P) # Name  # PID  # PPID  #PDB  # Time   #Created  #Time Exited
# list[0] list[1]  list[2]  list[3]  list[4]  list[5]  list[6]   list[7]
# Function to find the name of the parent process
def findName(ppid, dictP):
    namePID = ''
    for i in range(0,len(dictP['name'])):
        if dictP['pid'][i] == ppid:
            namePID = dictP['name'][i]
    return namePID

# Function to find if the offset in the psscan output is found in the pslist output
def findPSList(oVal):
    exists = 'False'
    f = open(pslistFile, 'r')
    for line in f:
        if (('Offset' not in line) and ('-------' not in line)):
            list = line.split()
    psOffset = list[0]
    if (oVal[-8:] == psOffset[-8:]):
        exists='True'
    return exists

# The keys that make up the dictionary for the input of the psscan output
keys = ['offset', 'name', 'pid', 'ppid', 'pdb', 'createDate', 'createTime', 'createTimeZone', 'exitDate', 'exitTime', 'exitTimeZone']
dictPsscan = {}

# Open the File where the psscan output is located
file = open(psscanFile, 'r')
for line in file:
    # Ignore the header lines that are in the output
    if (('Offset' not in line) and ('-------' not in line)):
        list = line.split()
    # The line being read may not have all 12 values so append to the list until it does (Time Exited sometimes does not exist)
    while len(list) != 12:
        list.append('')
    # Add the values of the list into my dictionary
    for x in range(0,11):
        dictPsscan.setdefault(keys[x], []).append(list[x])

# Identify the length of the dictionary
dictLen = len(dictPsscan['offset'])
# Take from the dictionary dictPsscan and the values of the PID values. Create a list, sort and remove duplicates
listPID = []
for i in range(0, dictLen):
 listPID.append(dictPsscan['pid'][i])
 # Remove duplicate PID values and then sort them as an integer
 listPID = sorted(set(listPID), key=int)

titleTable = "Offset(P) pslist # name pid pName ppid pdb createdDate cTime cTZ exitDate eTime eTZ"
table = titleTable.split()
# Format the output to make it easier to read
print('{0:20s} {1:6s} {2:3s} {3:16s} {4:5} {5:16} {6:5} {7:12} {8:11} {9:9} {10:9} {11:11} {12:9} {13:9}'.format(table[0], table[1], table[2], table[3], table[4], table[5], table[6], table[7], table[8], table[9], table[10], table[11], table[12], table[13]))
print("-"*20 + " " + "-"*6 + " " + "-"*3 + " " + "-"*16 + " " + "-"*5 + " " + "-"*16 + " " + "-"*5 + " " + "-"*12 + " " + "-"*11 + " " + "-"*9 + " " + "-"*9 + " " + "-"*11 + " " + "-"*9 + " " + "-"*9)

# Loop through the PID values
for i in range(0, len(listPID)):
 # The counter is to count the number of instances of the PID coming out of psscan
 counter = 1
 for j in range(0, dictLen):
  if listPID[i] == dictPsscan['pid'][j]:
   outputInfo = dictPsscan['offset'][j] + " "
   outputInfo += findPSList(dictPsscan['offset'][j]) + " "
   outputInfo += str(counter) + " "
   outputInfo += dictPsscan['name'][j] + " "
   outputInfo += dictPsscan['pid'][j] + " "
   ppidName = findName(dictPsscan['ppid'][j], dictPsscan)
   if ppidName == '':
    ppidName = '(Unavailable)'
   outputInfo += ppidName + " "
   outputInfo += dictPsscan['ppid'][j] + " "
   outputInfo += dictPsscan['pdb'][j] + " "
   if (dictPsscan['createDate'][j]):
    outputInfo += dictPsscan['createDate'][j] + " "
   else:
    outputInfo += " * "
   if (dictPsscan['createTime'][j]):
    outputInfo += dictPsscan['createTime'][j] + " "
   else:
    outputInfo += " * "
   if (dictPsscan['createTimeZone'][j]):
    outputInfo += dictPsscan['createTimeZone'][j] + " "
   else:
    outputInfo += " * "
   if (dictPsscan['exitDate'][j]):
    outputInfo += dictPsscan['exitDate'][j] + " "
   else:
    outputInfo += " * "
   if (dictPsscan['exitTime'][j]):
    outputInfo += dictPsscan['exitTime'][j] + " "
   else:
    outputInfo += " * "
   if (dictPsscan['exitTimeZone'][j]):
    outputInfo += dictPsscan['exitTimeZone'][j]
   else:
    outputInfo += " * "
   table = outputInfo.split()
   # Format the output to make it easier to read
   print('{0:20s} {1:6s} {2:3s} {3:16s} {4:5} {5:16} {6:5} {7:12} {8:11} {9:9} {10:9} {11:11} {12:9} {13:9}'.format(table[0], table[1], table[2], table[3], table[4], table[5], table[6], table[7], table[8], table[9], table[10], table[11], table[12], table[13]))
   # Find the relevant PID files for that PPID
   counter += 1
