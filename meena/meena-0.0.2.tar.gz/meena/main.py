# CHILD REPO OF tinda
# os.system('pip install tinda) or 'pip install tinda' in bash

from tinda import *
try:
    from nope import *
except:
    pass

# bot()
try:
    bol("Welcome back")
    botTime()
    botDate()
except:
    pass

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
            bol("quitting in 3,2")
            quit()
        if "what time" in query:
            botTime()
        if "what date" or "what day" in query:
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
            bol('trying to access camera')
            try:
                videoRead(nope['defaultcam'])
            except:
                bol('negative')
                pass
        if "detect hand" in query:
            bol('trying to access camera')
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



#ADD show desktop, quit tasks, list tasks, 
#ADD text copy to implement paste bottype paste
#ADD creeper for voice data collection
#ADD seld code check runner and diagnose tool




def ZoeT():
    threading.Thread(target=Zoe).start()


