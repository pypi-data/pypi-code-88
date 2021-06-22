"""
PortableQDA tests
"""
import sys,nose
sys.path.append("../tests")

if __name__ == '__main__':
    sys.argv+=["-s",] #lots of log lines to screen, comment out at wlll
    nose.run()

