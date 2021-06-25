from re import compile


def findAllWithRe(data, pattern):
    return compile(pattern).findall(data)
