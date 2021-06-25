"""
Manipulation
"""


def chain_words(lst, sep=" "):
    t = ''
    for i in range(len(lst)):
        t = t + sep + lst[i]
    return t[1:]
