__author__ = 'darakna'
import subprocess

def var1(s_process):
    print ('\nread:')
    proc = subprocess.Popen([s_process, '"to stdout"'],
                        stdout=subprocess.PIPE,
                        )
    stdout_value = proc.communicate()[0]
#    print ('\tstdout:', repr(stdout_value))
    print(stdout_value)
def var2(s_process2):
    print ('\npopen2:')
    proc = subprocess.Popen([s_process2, '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,)
    stdout_value = proc.communicate('through stdin to stdout','-')[0] #'through stdin to stdout'
    print ('\tpass through:', repr(stdout_value))
var2('PyAppReadCons.exe')