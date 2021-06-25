# The source code goes here
import os
from os import path
import platform

def getcwd():
    pwd = os.getcwd()
    print (pwd)

def mkdir(dirname):
    os.mkdir(dirname)

def chdir(dirpath):
    os.chdir(dirpath)

def rmdir(dirname):
    os.rmdir(dirname)

def rename(dirname, newdirname):
    os.rename(dirname, newdirname)

def touchfile(filename):
    os.mknod(filename)

def remove(filename):
    os.remove(filename)

def listdir(pwd=os.getcwd()):
    os.listdir(pwd)

def listall(pwd=os.getcwd()):
    for i in os.listdir(pwd):
        print (i)

def stat(filename):
    print (os.stat(filename))

def system(keyword):
    os.system(keyword)

def st_mode(filename):
    print (os.stat(filename).st_mode)

def st_ino(filename):
    print (os.stat(filename).st_ino)

def st_dev(filename):
    print (os.stat(filename).st_dev)

def st_nlink(filename):
    print (os.stat(filename).st_nlink)

def st_uid(filename):
    print (os.stat(filename).st_uid)

def st_gid(filename):
    print (os.stat(filename).st_gid)

def st_size(filename):
    print (os.stat(filename).st_size)

    
def isdir(pwd):
    os.path.isdir(pwd)

def filextentionsindir():
    files = os.listdir()

    for file in files:
        fullpath = path.join(os.getcwd(),file)
        print (path.splitext(fullpath)[1])

def system_configaration(): 
    system = platform.uname()
 
    print(f"System: {system.system}")
    print(f"Node Name: {system.node}")
    print(f"Release: {system.release}")
    print(f"Version: {system.version}")
    print(f"Machine: {system.machine}")
    print(f"Processor: {system.processor}")

if __name__ == '__main__':
    main()