# CHILD REPO OF tinda
# os.system('pip install tinda) or 'pip install tinda' in bash
import threading
import speech_recognition
from tinda import *
import os

try:
    from nope import *
except:
    print("Failed to located keys")
    print("Caution: Some functions might not work")

def wakeUpZoe():
    def setUp():
        listener = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.2)
            listen = listener.listen(source)
            try:
                data = listener.recognize_google(listen)
            except  speech_recognition.UnknownValueError:
                listener = speech_recognition.Recognizer()
                return "None"
            return data
    z = setUp().lower()
    while  z == 0:
        continue
    while True:
        if 'zoe' in z:
            bol("Waking up 'Zoe', please wait")
            print("Waking up 'Zoe', please wait")
            Zoe()
        elif 'thread zoe' in z:
            bol("starting 'Zoe' in another thread")
            ZoeT()
        else:
            z = setUp().lower()


def Zoe():
    bol("Starting in 3, 2")
    pspacer(2)
    print("@Zoe: On Stand-by")
    print("@Zoe: Waiting for further instructions")
    bol("'Zoe' on 'standby', 'waiting' for further instructions")
    while True:
        debug = True
        query = audioToText().lower()
        print(f"@Zoe:{Time()}")
        if query == 0:
            continue
        if "black image" in query:
            bol('Roger')
            imageBlack()
        if "what time" in query:
            botTime()
        if "what date" in query:
            botDate()
        if "get mouse position" in query:
            bol('Roger')
            botGetMousePosition()
        if "close application" in query:
            bol('Roger')
            botCloseApp()
        if "left click" in query:
            bol('Roger')
            botLeftClick()
        if "show me the links" in query:
            bol('Roger')
            linksList()
        if "what can you do" in query:
            bot()
        if "open youtube" in query:
            bol('Roger')
            openLinkD('youtube')
        if "open google" in query:
            bol('Roger')
            openLinkD('google')
        if "open git hub" in query:
            bol('Roger')
            openLinkD('github')
        if "open python index" in query:
            bol('Roger')
            openLinkD('pypi')
        if "open netflix" in query:
            bol('Roger')
            openLinkD('netflix')
        if "open instagram" in query:
            bol('Roger')
            openLinkD('instagram')
        if "test internet speed" in query:
            bol('Roger')
            speedTest()
        if "Zoe copy paste" in query:
            bol('Roger')
            botType()
        if "greet" in query:
            botGreet()
        if "bot test" in query:
            bol("starting bot test in 3, 2")
            bot()
        if "minimize app" in query:
            bol('Roger')
            botMinimizeApp()
        if "upload to python index" in query:
            pyPI()
        if "zoe" in query:
            bol("I'm here")
        elif "zoe you there" in query:
            bol("yes boss")
        if "default cam" in query:
            bol('try-ing to access camera')
            try:
                videoRead(nope['defaultcam'])
            except:
                bol('negative')
                print("Couldn't connect to the camera.")
                pass
        if "detect hand" in query:
            bol('try-ing to access camera')
            try:
                detectHand(nope['defaultcam'])
            except:
                bol('negative')
                print("Couldn't connect to the camera.")
                pass
        if "play music" in query:
            bol('tring to access music directory')
            try:
                playMusic(lMusic)
                bol("music it is")
            except:
                bol('negative')
                pass
        if "zoe code" in query:
            bol('try-ing to access the code file, please wait')
            try:
                os.startfile(nope['meena'])
                bol("my code it is, of what i could find")
            except:
                print("Couldn't locate souce file")
                bol('negative')
        if "start creeper" in query:
            bol('try-ing to initiate creeper protocol')
            try:
                creeper()
                bol("creeper initiated boss")
            except:
                bol('negative')
                pass
        if "Master code" in query:
            bol('try-ing to access the code file, please wait')
            try:
                os.startfile(nope['tinda'])
                bol("here's the current tinda code i found")
            except:
                print("Couldn't locate souce file")
                bol('negative')
        if "show desktop" in query:
            bol('Roger')
            try:
                showDesktop()
                bol('pew pew')
            except:
                bol('negative')
        if "default directory" in query:
            bol("Roger")
            x = ""
            os.startfile(x)
            bol("pew pew")
        if "quit" in query:
            bol("quitting in 3, 2, 1")
            bol('Bye now')
            break
            quit()
        if "system shutdown" in query:
            bol("Initiating default system shutdown protocol")
            Shutdown()
            bol("pew pew")
        if "cancel shutdown" in query:
            bol("roger")
            aShutdown()
            bol("'aborted shutdown protocol', pew pew")
        if "abort shutdown" in query:
            aShutdown()
            bol("Shut-down aborted!")
        if "code red" in query:
            bol("bye now")
            KILLALL()
        if "breach detected" in query:
            bol("thodi payne di, saaleyo!")
            KILLALL()


def ZoeT():
    threading.Thread(target=Zoe).start()

def creepForZoe():
    threading.Thread(target=wakeUpZoe).start()


#ADD quit tasks, list tasks, 
#ADD text copy to implement paste bottype paste
#ADD self code check runner and diagnose tool

if __name__ == "__main__":
    Zoe()


