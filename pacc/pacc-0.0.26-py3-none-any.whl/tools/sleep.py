import time


def sleep(seconds):
    s = seconds
    while seconds > 0:
        print('还剩%s秒' % seconds, end="")
        time.sleep(1)
        print("\r", end="", flush=True)
        seconds -= 1
    print('已完成%s秒的休息' % s)
