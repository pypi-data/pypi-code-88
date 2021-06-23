###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
from execute import ExeLine

f_0 = lambda : "HelloTest"
f_1 = lambda x, y: x * y
f_2 = lambda x: [i for i in range(0, x)]

def f_3(n: str, i: int, f: float = 1.53):
    return f"{n}::{i * f}:{i ** f}"

class c_1:
    def __init__(self, i, f):
        self.i = i
        self.f = f
    
    def get(self):
        return (self.i, self.f)

def tester():
    ex = ExeLine(False)
    ex.append_pocket('f_0', f_0)                # HelloTest   str
    ex.append_pocket('f_1', f_1, (5, 2))        # 10          int
    ex.append_pocket('f_2', f_2, (10, ))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    list
    ex.append_pocket('f_3', f_3, ('Test',), {'i': 5, 'f': 0.9})     # Test::4.5:4.256699612603923   str
    ex.append_pocket('c_1', c_1, (100, "HI"))   # c_1   object
    
    itex = iter(ex)
    for i in itex:
        if i[1] == 'c_1':
            c_1_e = i[-1]
            ex.append_pocket('c_1_e', c_1_e.get)
        yield (i[1], i[-1])

def test():
    print(f'{"":>10}*** Test ExeLine is Start ***{"":<10}')
    print(f'{"-":>10}-----------------------------{"-":<10}\n')
   
    for t in tester():
        print(f'{"":>10}* Testing {t[0]} into ExeLine :{"":<10}')
   
        if t[0] == 'f_0':
            assert t[-1] == 'HelloTest'

        elif t[0] == 'f_1':
            assert t[-1] == 10

        elif t[0] == 'f_2':
            assert t[-1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        elif t[0] == 'f_3':
            assert t[-1] == "Test::4.5:4.256699612603923"

        elif t[0] == 'c_1':
            assert t[-1].get() == (100, 'HI')
        
        print(f"{'':>10}{t[0]} is passed.{'':<10}")
        print(f"{'':>10}--------<>---------{'':<10}\n")
    
    print(f'{"":>10}Test ExeLine is Done.{"":<10}')
    print(f'{"-":>10}-----------------------------{"-":<10}\n')



if __name__ == "__main__":
    exit(test())