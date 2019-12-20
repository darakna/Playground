import os
import string

def get_valid_drives():
    print("Getting valid drives...")
    valid_drives = []
    for elem in string.ascii_lowercase:
        path = elem + ":\\"
        #if os.path.isdir(path):
        #    print(path)
        if os.path.exists(path):
            valid_drives.append(path)
            #print(path)
    print("Got %s..." % (valid_drives))
    return valid_drives

import os

def get_filepaths(directory, extension=""):
    print("Getting files with extension: [%s] for path %s..." % (extension, directory))
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            if filepath.lower().endswith(extension):
                file_paths.append(filepath)  # Add it to the list.
    print("Got %s files for path %s..." % (len(file_paths), directory))
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
valid_drives = get_valid_drives()
extensions_list2 = ".mp3"
valid_mp3s = []
#valid_drives = ["d:\\games\\Counter-Strike1.6 v.42"]
for drive in valid_drives:
    valid_mp3s.extend(get_filepaths(drive, extensions_list2))
f = open("all_mp3s.txt","wb")
for file in valid_mp3s:
    f.write(file.encode())
    f.write("\n".encode())
f.close()
