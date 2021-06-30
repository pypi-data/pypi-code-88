from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Moodipy.UserSummary import Person
from screeninfo import get_monitors


class MoodTrends(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mood Trends"
        self.desktop = QApplication.desktop()
        self.left = 0
        self.top = 0
        self.width = get_monitors()[0].width - 150
        self.height = get_monitors()[0].height - 80
        self.initUI()

    def initUI(self):
        self.sw = (self.width / 1000)
        self.sh = (self.height / 610)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #bdffcc")
        self.mood_window()
        self.show()

    def mood_window(self):

        Person.setLabel(self, "Mood Analysis", False, self.sw*20, self.sh*10, self.sw*370, self.sh*39, self.sw*20, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "Your Current Mood", False, self.sw*25, self.sh*100, self.sw*370, self.sh*39, self.sw*12, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "Your Mood Trends", False, self.sw*470, self.sh*330, self.sw*370, self.sh*39, self.sw*12, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "", False, self.sw*20, self.sh*58, self.sw*225, self.sh*3, 0, "black", False, 'Segoe UI')
        Person.setLabel(self, "", False, self.sw*25, self.sh*150, self.sw*480, self.sh*170, 0, "white", False, 'Segoe UI')
        Person.setLabel(self, "", False, self.sw*470, self.sh*370, self.sw*480, self.sh*170, 0, "white", False, 'Segoe UI')
        mood = ''
        if len(Person.currentmood) == 1:
            mood = Person.currentmood[0]
        else:
            mood = Person.currentmood[0] + " and " + Person.currentmood[1]

        Person.setLabel(self, mood, False, self.sw*90, self.sh*280, self.sw*150, self.sh*20, self.sw*11, "white", False, 'Consolas')




