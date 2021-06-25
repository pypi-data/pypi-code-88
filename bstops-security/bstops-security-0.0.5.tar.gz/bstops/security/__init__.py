import os
import string
import sys
import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


def generate_key(num):
    s = string.ascii_letters + string.digits
    r = random.SystemRandom()
    return ''.join([r.choice(s) for _ in range(num)])