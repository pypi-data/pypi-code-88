# CHILD REPO OF tinda
# os.system('pip install tinda) or 'pip install tinda' in bash

from tinda import *
try:
    from nope import *
except:
    pass


def Zoe():
    pspacer(7)
    print("ZOE: On Stand-by")
    bol("'Zoe' on standby, waiting for further instructions")
    while True:
        debug = True
        query = audioToText().lower()
        print(f"@Zoe:{Time()}")
        if query == 0:
            continue
        if "black image" in query:
            imageBlack()
        if "quit" in query:
            quit()
        if "what time" in query:
            botTime()
        if "what date" in query:
            botDate()
        if "get mouse position" in query:
            botGetMousePosition()
        if "close application" in query:
            botCloseApp()
        if "left click" in query:
            botLeftClick()
        if "show me the links" in query:
            linksList()
        if "what can you do" in query:
            botSkills()
        if "open youtube" in query:
            openLinkD('youtube')
        if "open google" in query:
            openLinkD('google')
        if "open git hub" in query:
            openLinkD('github')
        if "pie pee eye" in query:
            openLinkD('pypi')
        if "open netflix" in query:
            openLinkD('netflix')
        if "open instagram" in query:
            openLinkD('instagram')
        if "test internet speed" in query:
            speedTest()
        if "Zoe copy paste" in query:
            botType()
        if "greet" in query:
            botGreet()
        if "bot test" in query:
            bot()
        if "minimize app" in query:
            botMinimizeApp()
        if "upload to python index" in query:
                pyPI()
        if "zoe" in query:
            bol("I'm here")
        if "zoe there" in query:
            bol("yes boss")
        if "zoe you there" in query:
            bol("roger")
        if "default cam" in query:
            try:
                videoRead(nope['defaultcam'])
            except:
                pass
        if "detect hand" in query:
            try:
                detectHand(nope['defaultcam'])
            except: 
                pass
        if "play music" in query:
            try:
                playMusic(lMusic)
            except:
                pass



#ADD show desktop, quit tasks, list tasks, 
#ADD text copy to implement paste bottype paste
#ADD creeper for voice data collection
#ADD seld code check runner and diagnose tool




def ZoeT():
    threading.Thread(target=Zoe).start()

ZoeT()
