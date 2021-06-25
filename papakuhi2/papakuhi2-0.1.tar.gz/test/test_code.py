import os
import sys
from papakuhi import main_class

def test():
    """
    unit test for our package
    """

    abspath = sys.path
    print(abspath)

    path=os.path.join(abspath,'data/test.dat')
    
    radius = 0.00005
    #papa_test = main_class.papa(radius,dir)
    print(papa_test.ra[0], papa_test.dec[0])
    #re = papa_test.combined_query()
    #print (re)



if __name__ == '__main__':
    test()