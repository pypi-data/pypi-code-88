import os
import re


def fcomp(yourpath):

    """Docs:
     Function receives the path and analyzes the directory it represents
     in order to find the files/directories of maximum and minimum sizes that the initial folder contains.
     Then returns a dictionary with tuples containing path to those objects as values.
     Keys used are: 'maxs' for maximum sized objects, 'mins' for minimal sized ones and 'eq' if all have equal sizes.
     Usage of backslash in paths should be avoided due to it causing the function to fail (SyntaxError).
     Either double backslash or slash should be used instead. Alternatively, the path can be
     initially inputted as raw"""

    contents = os.listdir(yourpath)
    slashes = re.compile('\\\\\\\\')
    yourpath = slashes.sub('/', yourpath)
    quantity = len(contents)
    if quantity == 0:
        returned = None
    else:
        sizetup = ()                                  # Creating a tuple with sizes of path contents in bytes
        for k in range(quantity):
            sizesum = 0
            currentpath = os.path.join(yourpath, contents[k])
            if os.path.isfile(currentpath):
                sizetup += (os.path.getsize(currentpath),)
            else:
                for path, dirs, files in os.walk(currentpath):
                    for file in files:
                        filepath = os.path.join(path, file)
                        sizesum += os.path.getsize(filepath)
                sizesum = (sizesum,)
                sizetup += sizesum
        maxs = 0                        # Finding indexes(keys) of one maximum and one minimum size contents
        mins = 0
        for k in range(1, quantity):
            if sizetup[k] > sizetup[maxs]:
                maxs = k
            else:
                if sizetup[k] < sizetup[mins]:
                    mins = k
        maxtup = ()                    # Finding all indexes(keys) of minimal and maximal sized contents
        mintup = ()
        for i in range(quantity):
            if sizetup[i] == sizetup[maxs]:
                maxtup += (i,)
            if sizetup[i] == sizetup[mins]:
                mintup += (i,)
        largest = ()                                                     # Preparing the returned values
        slash = re.compile('\\\\')
        for i in maxtup:
            largest += (slash.sub('/', str(os.path.join(yourpath, contents[i]))),)
        if maxtup == mintup:
            returned = {'eq': largest}
        else:
            smallest = ()
            for i in mintup:
                smallest += (slash.sub('/', str(os.path.join(yourpath, contents[i]))),)
            returned = {'maxs': largest, 'mins': smallest}
    return returned
