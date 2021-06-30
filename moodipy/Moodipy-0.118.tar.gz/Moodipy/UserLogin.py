from PyQt5.QtWidgets import *
from Moodipy.UserSummary import Person
from Moodipy.MoodAnalyzerGUI import MoodAnalyzerPg
from Moodipy.SpotifyAuthorization import Authorization
from screeninfo import get_monitors
from os import path


class UserLoginPG(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Login"
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
        self.setStyleSheet("background-color: #ccccff")
        self.mood_window()
        self.show()

    def mood_window(self):
        Person.setLabel(self, "", True, self.sw*290, self.sh*100, self.sw*460, self.sh*400, 0, "#f2ccff", False, 'Consolas')
        Person.setLabel(self, "Log In", False, self.sw*470, self.sh*130, self.sw*100, self.sh*39, self.sw*20, "#f2ccff", True, 'Consolas')
        Person.setLabel(self, "Login here using your Spotify username", False, self.sw*400, self.sh*170, self.sw*300, self.sh*39, self.sw*8, "#f2ccff", False, 'Consolas')
        Person.setLabel(self, "Username", False, self.sw*380, self.sh*230, self.sw*100, self.sh*30, self.sw*13, "#f2ccff", False, 'Consolas')
        self.username = QLineEdit(self)
        self.username.setGeometry(self.sw*380, self.sh*260, self.sw*270, self.sh*29)
        self.username.setStyleSheet("background-color: white")

        loginbtn = QPushButton("LOGIN", self)
        loginbtn.setGeometry(self.sw*450, self.sh*380, self.sw*150, self.sh*40)
        loginbtn.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ccccff, stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:20px;")
        loginbtn.clicked.connect(self.on_click)

    def on_click(self):
        Person.userID = (self.username.text())
        if Authorization() == None:
            self.pop_up()
        else:
            userInfoPath = path.join(path.dirname(__file__), "UserInfo.txt")
            f = open(userInfoPath, "w+")
            f.write(self.username.text())
            f.close()
            self.nextPg = MoodAnalyzerPg()
            self.nextPg.show()
            self.hide()

    def pop_up(self):
        msg = QMessageBox.question(self, 'Invalid Username', 'Please enter a valid username', QMessageBox.Ok)


