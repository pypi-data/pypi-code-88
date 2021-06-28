import os
import sys

import getopt
from tpexe.action.delete import Delete
from tpexe.action.alloc import Alloc

CSV_PATH = './teleport.csv'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hda")
    except getopt.GetoptError:
        print('Usage: run.py -d [-a]')
        sys.exit(2)
 
    delete = Delete()
    alloc = Alloc(CSV_PATH)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: run.py -d [-a]')
            sys.exit()
        elif opt in "-a":
            alloc.alloc_run() 
        elif opt in "-d":
            delete.delete_host_run()

if __name__ == "__main__":
    main(sys.argv[1:])
