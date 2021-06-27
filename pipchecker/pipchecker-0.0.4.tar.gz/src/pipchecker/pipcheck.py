import importlib.util
import sys
import fire

class Pipchecker:
    def __init__(self,pname):
        self.pname = pname


    def pipchecker(self):
        try:
            if importlib.util.find_spec(self.pname):
                return f'{self.pname}' + ' is already installed in your system'
            else:
                return f'{self.pname}' + ' is currently not installed in your system'
        except Exception as e:
            print(e)


def main(name):
    package1 = Pipchecker(f'{name}')
    print(package1.pipchecker())



if __name__ == '__main__':
    fire.Fire(main)
