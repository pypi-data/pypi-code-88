import time


def say(number: int):
    print(number)
    time.sleep(0.5)


for i in range(5):
    say(i)
