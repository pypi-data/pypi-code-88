def select(Arr):
    a = []
    last_end = float("-inf")
    Arr.sort(key = lambda i : i[1])
    for i in Arr:
        start = i[0]
        if start > last_end:
            last_end = i[1]
            a.append(i)
    return a
if __name__ == '__main__':
    Arr = [[0,6],[4,7],[3,9],[8,11]]
    print(select(Arr))