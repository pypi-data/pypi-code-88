def center(msg: str, decorator='#', width=80):
    n = 2
    x = ' ' * int(width / 2 - n - len(msg) / 2)
    s0 = x + msg
    s1 = s0 + ' ' * (width - len(s0) - 4)
    s = '\n' + decorator * width + '\n'
    s += decorator * n + s1 + decorator * n + '\n'
    s += decorator * width
    print(s)
    return s