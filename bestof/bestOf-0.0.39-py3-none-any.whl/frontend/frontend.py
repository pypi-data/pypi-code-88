
import cv2 as cv
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
print("Starting...")

import bestOf.backend.similarity as similarity
from bestOf.backend.classDefinitions import BlinkAndCropNet, cropped_model
import bestOf.backend.blinkDetector as blinkDetector
import bestOf.backend.cropDetector as cropDetector
import bestOf.backend.identifyPeople as identifyPeople


def loadImages(filenames):
    for filename in filenames:
        yield identifyPeople.read_img(filename)


IMAGELIST = []
GROUPS = []

# Reference Source 1: https://learndataanalysis.org/how-to-pass-data-from-one-window-to-another-pyqt5-tutorial/


def main():
    class processingResults(QWidget):
        def __init__(self):
            super().__init__()
            self.options()
            self.setWindowTitle("Best Of")
            self.setGeometry(1550, 800, 500, 500)
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.des)
            self.setLayout(self.layout)

        def display(self):
            self.__init__()
            self.show()

        def options(self):
            self.des = QGroupBox("Images Selected.",
                                 alignment=QtCore.Qt.AlignCenter)
            vert = QVBoxLayout()
            layout = QHBoxLayout()
            self.redo = QPushButton('&Run Again')
            self.redo.clicked.connect(self.imageProcessing)
            layout.addWidget(self.redo)
            self.back = QPushButton('&Back to Main Menu')
            self.back.clicked.connect(self.close)
            layout.addWidget(self.back)
            info = IMAGELIST
            groups = GROUPS
            if len(info) == 0:
                return
            print(info)
            print(groups)
            for group in groups:
                h = QHBoxLayout()
                for index in group:
                    lab = QLabel()
                    for el in info:
                        if el[0] == index:
                            lab.setPixmap(QPixmap(el[1]))
                    h.addWidget(lab)
                vert.addLayout(h)
            vert.addLayout(layout)
            self.des.setLayout(vert)

        def imageProcessing(self):
            # Code from backend goes here...
            print("Redoing image selection.")

    class settingsMenu(QWidget):
        def __init__(self):
            super().__init__()
            self.options()
            self.setWindowTitle("Settings Menu")
            self.setGeometry(1550, 800, 500, 500)
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.des)
            self.setLayout(self.layout)

        def display(self):
            self.show()

        def options(self):
            self.des = QGroupBox("Apply the following criteria for image refinement.",
                                 alignment=QtCore.Qt.AlignCenter)
            layout = QHBoxLayout()

            self.closeButton = QPushButton('&Close Settings')
            self.closeButton.clicked.connect(self.close)
            layout.addWidget(self.closeButton)
            self.des.setLayout(layout)

    class mainWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Best Of: Main Menu")
            self.resize(800, 800)
            self.setGeometry(1550, 800, 500, 500)
            self.nextWindow = settingsMenu()
            self.process = processingResults()
            self.makeUI()
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.firstText)
            self.setLayout(self.layout)

        def makeUI(self):
            self.firstText = QGroupBox("Welcome, browse your computer for images to start picture analysis.",
                                       alignment=QtCore.Qt.AlignCenter)
            layout = QHBoxLayout()
            self.addImage = QPushButton('&Add Images')
            self.addImage.clicked.connect(self.getFiles)
            layout.addWidget(self.addImage)
            self.processImage = QPushButton('&Process Image(s)')
            self.processImage.clicked.connect(self.process.display)
            layout.addWidget(self.processImage)
            self.settings = QPushButton('&More Settings')
            self.settings.clicked.connect(self.nextWindow.display)
            layout.addWidget(self.settings)
            self.firstText.setLayout(layout)

        # Grabs the files for image selection... work in progress...

        def getFiles(self):
            global IMAGELIST
            global GROUPS
            file = QFileDialog.getOpenFileNames(
                self, 'Add Files', QtCore.QDir.rootPath())
            files = ""
            layout = QVBoxLayout
            image_generator = loadImages(list(file[0]))
            vectors = []
            for image in image_generator:
                v = similarity.generate_feature_vector(image)
                vectors.append(v)

            threshold = 0.8  # this should be grabbed from whatever the user set it to in the settings
            groups = similarity.group(vectors, threshold=threshold)
            print(groups)
            GROUPS = groups

            image_generator = loadImages(list(file[0]))

            bestof_scores = []

            for image in image_generator:
                # print('Scanning Image...')
                subjects = identifyPeople.crop_subjects(image)
                print("len of subjects", len(subjects))
                blinks = 0
                crops = 0
                for sub in subjects:
                    # identifyPeople.show_img(sub)
                    # print('Scanning Subject...')
                    if blinkDetector.test(sub):
                        blinks += 1
                    if cropDetector.test(sub):
                        crops += 1

                blink_score = (len(subjects) - blinks) / len(subjects)
                crop_score = (len(subjects) - crops) / len(subjects)

                bestof_score = blink_score + crop_score
                bestof_scores.append(bestof_score)
            final = zip(range(len(file[0])), file[0], bestof_scores)

            final = sorted(final, key=lambda x: x[2], reverse=True)
            print(final)
            IMAGELIST = final

    newApp = QApplication(sys.argv)  # Creates application class
    wind = mainWindow()
    wind.show()
    newApp.exec()  # Executes app with the window


if __name__ == '__main__':
    main()
