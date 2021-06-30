import sys
import os
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Moodipy.UserSummary import Person
from Moodipy.UserLogin import UserLoginPG
from screeninfo import get_monitors
from Moodipy.MoodAnalyzerGUI import MoodAnalyzerPg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Moodipy"
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
        self.setStyleSheet("background-color: #ffdb94")
        self.main_window()
        self.show()

    def main_window(self):
        print(self.width)
        print(self.height)
        button = QPushButton(self)
        button.setGeometry(self.sw*480, self.sh*450, self.sw*40, self.sh*20)
        arrow_img = path.join(path.join(path.dirname(__file__), "imgs"), "arrow.png")
        styleS = "border-image : url(" + arrow_img + ");"
        button.setStyleSheet(styleS)
        button.clicked.connect(self.nextPG)

        Person.setLabel(self, "Welcome to", True, self.sw*390, self.sh*200, self.sw*220, self.sh*35, self.sw*19, "white", False,'Consolas')
        Person.setLabel(self, "Moodipy", True, self.sw*380, self.sh*260, self.sw*230, self.sh*58, self.sw*35, "white", True, 'Segoe UI')
        Person.setLabel(self, "Generating playlists that express how you feel", True, self.sw*335, self.sh*375, self.sw*338, self.sh*20, self.sw*9, "white", False,'Consolas')

    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(self.sw*270, self.sh*70, self.sw*450, self.sh*450)

    def nextPG(self):
        userInfoPath = path.join(path.dirname(__file__), "UserInfo.txt")
        if os.path.isfile(userInfoPath):
            if os.stat(userInfoPath).st_size == 0:
                self.nextPG = UserLoginPG()
                self.nextPG.show()
                self.hide()
            f = open(userInfoPath, "r+")
            Person.userID = f.readline()
            f.close()
            self.nextPG = MoodAnalyzerPg()
            self.nextPG.show()
            self.hide()
        else:
            self.nextPG = UserLoginPG()
            self.nextPG.show()
            self.hide()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
