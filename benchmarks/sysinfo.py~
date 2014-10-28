import platform
from tabulate import tabulate

def print_sysinfo():

    A = []
    print
    A.append(['Python version ', ':', platform.python_version()])
    A.append(['compiler', ':', platform.python_compiler()])
    A.append(['system ', ':', platform.system()])
    A.append(['release', ':', platform.release()])
    A.append(['machine', ':', platform.machine()])
    A.append(['processor',':', platform.processor()])
    #print('CPU count  :', mp.cpu_count())
    A.append(['interpreter ',':', platform.architecture()[0]])
    #print('\n\n')
    print tabulate(A, tablefmt='rst')
    print 
