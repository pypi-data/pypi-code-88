from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Person:
    def __init__(self):
        self.__currentMood = []
        self.__userID = None
        self.__moodLabel = None
        self.__playlistName = None
        self.__tracks = {}

    @property
    def playlistName(self):
        return self.__playlistName

    @playlistName.setter
    def playlistName(self, title):
       self.__playlistName = title

    def setPlaylistName(self, label, currMood):
        playlistName = ''
        if label == "Happy" or currMood[0] == "joy":
            playlistName = "Happy Vibes"
        elif label == "Awful" or currMood[0] == "sadness":
            playlistName = "Downbeat and Angst"
        elif label == "Bad" or currMood[0] == "anger":
            playlistName = "Rage and Loathing"
        elif label == "Okay" or currMood[0] == "fear":
            playlistName = "It's Gonna be Okayyy"
        elif label == "Excited" or currMood[0] == "surprise":
            playlistName = "Hyped Up!"
        elif "Love" in label:
            playlistName = "In Love with Life"
        return playlistName

    @property
    def moodLabel(self):
        return self.__moodLabel

    @moodLabel.setter
    def moodLabel(self, label):
        self.__moodLabel = label

    def setMoodLabel(self, currMood):
        if len(currMood) == 1:
            moodLabel = currMood[0].capitalize()
        else:
            moodLabel = currMood[0].capitalize() + " and " + currMood[1].capitalize()
        return moodLabel

    @property
    def currentmood(self):
        return self.__currentMood

    @property
    def tracks(self):
        return self.__tracks

    @tracks.setter
    def tracks(self, tracks):
        self.__tracks = tracks

    @property
    def moods(self):
        return self.__moods

    @currentmood.setter
    def currentmood(self, currentMood):
        self.__currentMood = currentMood

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID):
        self.__userID = userID

    def setLabel(self, text, center, left, top, width, height, ftSize, bkColor, bold, font):
        label = QLabel(text, self)
        if center:
            label.setAlignment(Qt.AlignCenter)
        label.setGeometry(left, top, width, height)
        style = "background-color: "+bkColor+";"
        if bold:
            style = style+"font-weight: bold"
        label.setStyleSheet(style)
        label.setFont(QFont(font, ftSize))


