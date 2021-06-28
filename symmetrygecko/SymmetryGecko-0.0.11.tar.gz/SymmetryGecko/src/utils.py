from time import time

def get_unix(take_floor=True):
    """ if take_floor is True, 1624830286.9898442 becomes 1624830286 """
    return round( time() ) if take_floor else time()