#test write to file
def print_to_file(*args):
    filehandler = open("Print_file.txt","a")
    for arg in args:
        filehandler.write(str(arg))
        filehandler.write(" ")
    filehandler.write("\n")
    filehandler.close()
