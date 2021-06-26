from time import sleep
from random import randint
slptime = 0.1
def retext(rane = (0,6),ifTOF = False):
    restring = randint(rane[0],rane[1])
    if ifTOF == True:
        restring = str(restring)
    return restring;
def setslp(time):
    global slptime
    slptime = time
    return slptime;
def clftext(*a):
    global time
    if type(a) == list:
        for i in a:
            b = str(i)
            for j in b:
                print("\033["+ str(retext((31,36))) + "m" + j,end = "")
                sleep(setslp(slptime))
    else:
        for f in a:
            c = str(f)
            for h in c:
                print("\033["+ str(retext((31,36))) + "m" + h,end = "")
                sleep(setslp(slptime))
    print()
    sleep(1)