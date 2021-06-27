import itertools
import os
from os import name
import threading
import time
import sys
from tqdm import trange
from time import sleep
import random


def cls():
    if name == 'nt': 
        os.system('cls')
    else:
        os.system("clear")


def loadingC(

LoadTimeInSec=5,
LoadingText="loading",
ClearScreenAfterLoading=False,
TextAfterLoading=False,
EndText=""
):
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                if ClearScreenAfterLoading == False:
                    if TextAfterLoading==True:
                        print(EndText)
                        break
                    elif TextAfterLoading==False:
                        break
                elif ClearScreenAfterLoading == True:
                    cls()
                    if TextAfterLoading==True:
                        print(EndText)
                        break
                    elif TextAfterLoading==False:
                        break
                    break
            sys.stdout.write(f'\r{LoadingText} ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(LoadTimeInSec)
    done = True
    return 0



max_and_min_time =[
        0.1,0.1,0.1,0.1,0.1,
        0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,
        0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
        0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
        0.1,0.1,0.1,0.1,0.1,0.01,0.01,0.01,0.01, 
        0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
        0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
        0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
        0.9,0.9,0.9,
        ]



def loading_bar(files=101, DescriptionWhileDownloading="downloading",Leave=True,unit="it",end_txt=""):
    t = trange(files,
        desc=DescriptionWhileDownloading,
        leave=Leave,
        unit = unit)
    for i in t:
        t.set_description(f"{DescriptionWhileDownloading} %i" % i)
        t.refresh() 
        sleep(random.choice(max_and_min_time))
    print(end_txt)
