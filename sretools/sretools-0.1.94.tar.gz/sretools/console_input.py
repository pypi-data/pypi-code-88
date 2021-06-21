import sys
import tty
import termios
from collections import deque


debug=False

class Input :
    def __init__(self, ps1="[sretools]@ ") :
        self.__ps1 = ps1
        tty.setcbreak(sys.stdin.fileno())
        self.__history = deque(maxlen=500)
    def history(self) :
        return self.__history
    def getline(self) :
        cmd=""
        pcmd=len(self.__history)
        ptr=0
        print(self.__ps1+cmd,end="",flush=True)
        while True :
            c = sys.stdin.read(1)
            if debug :
                print(ord(c))
            # backspace 127 
            # arrow 27,91, up 65, down 66, right 67, left 68
            if ord(c) == 27 :
                c = sys.stdin.read(1)
                if debug :
                    print(ord(c))
                if ord(c) == 91  :
                    c = sys.stdin.read(1)
                    if debug :
                        print(ord(c))
                    # 65 up 66 down
                    if ord(c) in [65,66] : # 
                        if ord(c) == 65 :
                            pcmd -= 1
                        if ord(c) == 66 :
                            pcmd += 1
                        if pcmd < 0 :
                            pcmd = 0
                        if pcmd >= len(self.__history) :
                            pcmd = len(self.__history)-1
                        if 0 <= pcmd <= len(self.__history)-1 :
                            cmd = self.__history[pcmd]
                            print("\b"*200+" "*200+"\b"*300,end="",flush=True)
                            print(self.__ps1+cmd,end="",flush=True)
                    if ord(c) in [67,68] : # 
                        pass
                continue
            # darwin 127, linux 8
            if ord(c) == 127 or ord(c) == 8 :
                if cmd :
                    print("\b \b",end="",flush=True)
                if len(cmd) > 0 :
                    cmd = cmd[:-1]
                continue
            if ord(c) == 10 :
                print("")
                if cmd :
                    self.__history.append(cmd)
                    return cmd
                else :
                    print(self.__ps1+cmd,end="",flush=True)
                    continue
            cmd += c
            print(c,end="",flush=True)

def main() :
    xin = Input()
    while True :
        x = xin.getline()
        if x == "\\h" :
            for i,cmd in enumerate(xin.history()) :
                print("# {:3} : {}".format(i,cmd))
        if x == "\\q" :
            import os
            os.system("reset")
            os.system("clear")
            break
        print("# cmd = "+x)


if __name__ == "__main__" :
    main()
