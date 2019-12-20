__author__ = 'darakna'
import os
import time
import codecs

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths("folder_with_logs")

domain_char_list=list(range(0,127))
def stripall(word):
    if word=="":
        return ""
    else:
        if ord(word[0]) in domain_char_list:
            return word[0]+stripall(word[1:])
        else:
             return stripall(word[1:])


h=open("Logfiles.txt","w")
no_of_lines=0
for i in range(len(full_file_paths)):
    print(full_file_paths[i])
    h.write(full_file_paths[i])
    h.write("\n")
    f=open(full_file_paths[i])
    myEncoding = "utf-8"
    try:
        print("Try decode utf-16")
        myEncoding = 'utf-16'
        f=codecs.open(full_file_paths[i], "r", "utf-16")
        text=f.read()
        
        print("Succses decode utf-16")
    except:
        print("Fail decode utf-16, decode ASCII")
        f=open(full_file_paths[i])
        text=f.read()
        print("Succses decode ASCII")
    #text=f.read()
    #time.sleep(0.3)
    #print(text)
    text=text.split("\n")
    #print(text)
    g=open("Errors.txt","a", encoding=myEncoding)
    g.write("\n\n\n")
    g.write(full_file_paths[i])
    g.write("\n")
    no_of_lines+=1
    for words in text:
        #print(words)
        if "WARNING" in words or "ERROR" in words:
            try:
                print(words)
                g.write(words)
                g.write("\n")
            except:
                print(stripall(words))
                g.write(stripall(words))
                g.write("\n")
    f.close()
g.close()
h.write("No of log files = "+str(no_of_lines))
h.close()
