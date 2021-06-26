from functools import reduce

def factorial(n):
    if n in (0,1):
        return 1
    if n<1:
        return None
    return reduce(lambda x,y:x*y, range(1,n+1))
