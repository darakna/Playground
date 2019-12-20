import os
import bisect

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

search_path = "e:\\"
full_file_paths = get_filepaths(search_path)
wordlist = []
short_wordlist = []
for elem in full_file_paths:
    if elem.endswith(".txt"):
        if os.path.isfile(elem):
            if os.path.getsize(elem) < 100000:
                print(elem)
                f = open(elem, errors='ignore')
                words_unclean = f.read()
                words = ""
                for w in words_unclean:
                    if w.isalpha() and w.isascii() or w in [" ", "\r", "\n"]:
                        words += w
                for w in words.split():
                    w = w[0].upper() + w[1:].lower()
                    if 2 < len(w) < 12:
                        if w in wordlist and w not in short_wordlist:
                            bisect.insort(short_wordlist, w)
                        if w not in wordlist:
                            bisect.insort(wordlist, w)
print(wordlist)

with open("e:\\wordlist.txt", 'w') as f:
    for item in wordlist:
        f.write("%s\n" % item)
with open("e:\\wordlist_short.txt", 'w') as f:
    for item in short_wordlist:
        f.write("%s\n" % item)



#print(len(full_file_paths))


