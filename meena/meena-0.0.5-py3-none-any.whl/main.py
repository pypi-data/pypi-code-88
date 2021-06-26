# CHILD REPO OF tinda
# os.system('pip install tinda) or 'pip install tinda' in bash
import threading
import speech_recognition
from tinda import *


try:
    from nope import *
except:
    pass

# bot()
# try:
#     bol("Welcome back")
#     botTime()
#     botDate()
# except:
#     pass



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
            print(str(data))
            return data
    z = setUp().lower()
    while  z == 0:
        continue
    while True:
        if 'zoe' in z:
            bol("Waking up Zoe, please wait")
            Zoe()
        elif 'thread zoe' in z:
            bol("starting zoe in another thread")
            ZoeT()
        else:
            z = setUp().lower()




def Zoe():
    bol("Starting in 3, 2")
    pspacer(7)
    print("ZOE: On Stand-by")
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
        if "quit" in query:
            bol('Roger')
            bol("quitting in 3 2")
            quit()
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
        if "zoe you there" in query:
            bol("yes boss")
        if "default cam" in query:
            bol('try-ing to access camera')
            try:
                videoRead(nope['defaultcam'])
            except:
                bol('negative')
                pass
        if "detect hand" in query:
            bol('try-ing to access camera')
            try:
                detectHand(nope['defaultcam'])
            except:
                bol('negative')
                pass
        if "play music" in query:
            bol('tring to access music directory')
            try:
                playMusic(lMusic)
            except:
                bol('negative')
                pass
        if "open your code" in query:
            bol('try-ing to access the code file, please wait')
            try:
                os.startfile("meena\meena\main.py")
            except:
                pass
        if "start creeper" in query:
            bol('try-ing to inittate creeper protocol')
            try:
                creeper()
            except:
                bol('negative')
                pass
        if "tinda code" in query:
            bol('try-ing to access the code file, please wait')
            try:
                os.startfile("tinda\tinda\function.py")
            except:
                pass
        if "show desktop" in query:
            bol('Roger')
            try:
                showDesktop()
            except:
                pass





#ADD show desktop, quit tasks, list tasks, 
#ADD text copy to implement paste bottype paste
#ADD creeper for voice data collection
#ADD self code check runner and diagnose tool




def ZoeT():
    threading.Thread(target=Zoe).start()

def creeping_for_zoe_startup():
    threading.Thread(target=wakeUpZoe).start()


creeping_for_zoe_startup()
