from multiprocessing import Pool
import os
import sys

def processFile(x):
    os.system('python benchmarks/'+x)
    os.system('ls ')
    return

if __name__ == '__main__':
    pool = Pool(processes=int(sys.argv[1]))
    files=['client.py']
    pool.map(processFile, files)
