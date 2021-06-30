from screeninfo import get_monitors
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Moodipy.moodAnalyzer import find_mood
from Moodipy.UserSummary import Person
from Moodipy.LoadPage import LoadPg

class MoodAnalyzerPg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mood Analyzer"
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
        self.setStyleSheet("background-color:#abbdff")
        self.mood_window()
        self.show()

    def mood_window(self):
        # Labels
        Person.setLabel(self,"How are you feeling?", False, self.sw*20, self.sh*10, self.sw*370, self.sh*39, self.sw*20, "#abbdff", True, 'Segoe UI')
        Person.setLabel(self,"Write about your day...", False, self.sw*120, self.sh*70, self.sw*300, self.sh*35, self.sw*15, "#abbdff", False, 'Segoe UI')
        Person.setLabel(self, "Find your mood", False, self.sw*670, self.sh*70, self.sw*300, self.sh*35, self.sw*15, "#abbdff", False, 'Segoe UI')
        Person.setLabel(self, "", False, self.sw*20, self.sh*58, self.sw*320, self.sh*3, 0, "black", False, 'Segoe UI')
        # Textbox
        self.text = QTextEdit(self)
        self.text.setGeometry(self.sw*60, self.sh*100, self.sw*350, self.sh*450)
        self.text.setStyleSheet("border: 30px solid; border-radius:60px; background-color: #99acff; border-color: #99acff")
        self.text.setFont(QFont('Segoe UI', self.sw*11))
        # Block design
        boxDesign = QLabel(self)
        boxDesign.setGeometry(self.sw*570, self.sh*100, self.sw*350, self.sh*450)
        boxDesign.setStyleSheet("border: 30px solid; border-radius:60px; background-color: #99acff; border-color: #99acff")
        # OR label

        orLabel = QLabel("OR", self)
        orLabel.setAlignment(Qt.AlignCenter)
        orLabel.setGeometry(self.sw*460, self.sh*300, self.sw*60, self.sh*60)
        orLabel.setStyleSheet("border-radius: 30px; background-color: #99acff; border-color: #99acff; font-weight: bold")
        orLabel.setFont(QFont('Segoe UI', self.sw*12))


        # Text submit button
        btn1 = QPushButton("submit", self)
        btn1.clicked.connect(self.on_click)
        btn1.setGeometry(self.sw*200, self.sh*500, self.sw*80, self.sh*20)
        btn1.setStyleSheet("background-color: #abbdff;border-radius:10px; ")
        # Mood slider
        mood_slider = QSlider(Qt.Horizontal, self)
        mood_slider.setRange(0, 5)
        mood_slider.setGeometry(self.sw*630, self.sh*400, self.sw*250, self.sh*30)
        mood_slider.setFocusPolicy(Qt.NoFocus)
        mood_slider.setPageStep(1)
        mood_slider.valueChanged.connect(self.updateMood)
        mood_slider.setStyleSheet("background-color: #99acff;")
        # Mood image
        self.mood_img = QLabel(self)
        self.mood_img.setGeometry(self.sw*690, self.sh*200, self.sw*130, self.sh*130)
        awful_imgs = path.join(path.join(path.dirname(__file__), "imgs"), "awful.jpeg")
        styleS = "border-image : url("+awful_imgs+");background-color: #99acff;"
        self.mood_img.setStyleSheet(styleS)
        # Mood label
        self.mood = QLabel('awful', self)
        self.mood.setGeometry(self.sw*740, self.sh*350, self.sw*50, self.sh*30)
        self.mood.setMinimumWidth(self.sw*80)
        self.mood.setStyleSheet("background-color: #99acff;")
        self.mood.setFont(QFont('Segoe UI', self.sw*11))
        # Mood submit button
        btn2 = QPushButton("submit", self)
        btn2.clicked.connect(self.on_click2)
        btn2.setGeometry(self.sw*720, self.sh*500, self.sw*80, self.sh*20)
        btn2.setStyleSheet("background-color: #abbdff;border-radius:10px; ")

    def updateMood(self, value):
        moods = ["awful", "bad", "okay", "happy", "excited", "love"]
        mood_img = moods[value]+".jpeg"
        currMood = path.join(path.join(path.dirname(__file__), "imgs"), mood_img)
        styleS = "border-image : url("+currMood+");"
        self.mood_img.setStyleSheet(styleS)
        self.mood.setText(moods[value])

    def on_click(self):
        Person.currentmood = find_mood(self.text.toPlainText())
        if Person.currentmood is None:
            print("Please be more descriptive")
            self.pop_up()
        else:
            self.nextPg = LoadPg()
            self.nextPg.show()
            self.hide()

    def pop_up(self):
        msg = QMessageBox.question(self, 'Error', 'Please be more descriptive', QMessageBox.Ok)

    def on_click2(self):
        print("your mood: %s" % self.mood.text())
        mood = []
        mood.append(self.mood.text())
        Person.currentmood = mood
        self.nextPg = LoadPg()
        self.nextPg.show()
        self.hide()
