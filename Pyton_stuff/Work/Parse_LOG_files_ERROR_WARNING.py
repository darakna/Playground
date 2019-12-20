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
full_file_paths = get_filepaths("path_with_logs")
g=open("Errors.txt","w")
for i in range(len(full_file_paths)):
    print(full_file_paths[i])
    f=open(full_file_paths[i])
    try:
        print("Test1")
        f=codecs.open(full_file_paths[i], "r", "utf-16")
        text=f.read()
        print("Test2")
    except:
        print("Test3")
        f=open(full_file_paths[i])
        text=f.read()
        print("Test4")
    #text=f.read()
    time.sleep(0.3)
    #print(text)
    text=text.split("\n")
    #print(text)
    g.write("\n\n\n")
    g.write(full_file_paths[i])
    g.write("\n")
    for words in text:
        #print(words)
        if "WARNING" in words or "ERROR" in words:
            print(words)
            g.write(words)
            g.write("\n")
    f.close()
g.close()

