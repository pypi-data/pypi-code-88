from math import floor

ratio = 1.5


def scale(num):
    return floor(num * ratio)


def set_ratio(num):
    global ratio
    ratio = num


def round_ratio(num):
    print("Ratio:", num)
    print("Scaled tile Px:", num * 32)
    print("Excess to be truncated:", (num * 32) % 2)
    print("Reduced to excess from ratio:", (((num * 32) % 2) / 32))
    print("Final rounded ratio:", num - (((num * 32) % 2) / 32))
    return num - (((num * 32) % 2) / 32)
