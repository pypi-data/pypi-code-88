import logging
import subprocess
import os

logger = logging.getLogger(__name__)


class Person:
    age = 10
    sex = 'male'


if __name__ == '__main__':

    mylist = [1, 1]
    print(all(mylist))

    person = Person()
    print(getattr(person, 'age'))

    env = os.environ.copy()
    print(env)
    si = subprocess.STARTUPINFO
    print(si)
