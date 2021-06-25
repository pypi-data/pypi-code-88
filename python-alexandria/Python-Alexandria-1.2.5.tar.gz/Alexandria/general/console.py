"""
Console
"""

from termcolor import colored


def print_color(text, color):
    print(colored(text, color))


def units(s, u, n):
    if not isinstance(s, type(str)):
        s = str(s)
    return s + ' '*(n-len(s.replace("\n", ""))) + '[{}]'.format(u.rstrip())


def result(var, val, u, r=5, n=10):
    print(units(f'{var} {val:.{r}f}', u, n))


def print_numbered_list(lst, sep=4):
    for i in range(len(lst)):
        n = f"{i+1}"+"."
        numeral = n + " "*(sep-len(n))
        print(numeral+'"'+lst[i]+'"')
