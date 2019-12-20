__author__ = 'darakna'
def process_exists(name):
    i = psutil.get_pid_list()
    for a in i:
        try:
            if str(psutil.Process(a).name) == name:
                return True
        except:
            pass
    return False
#print(process_exists("Chrome"))

import psutil

for proc in psutil.process_iter():
    try:
        if proc.name() == u"chrome.exe":
            print(proc)
            print(proc.cmdline())
    except psutil.AccessDenied:
        print ("Permission error or access denied on process")