from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from library import *
import sys
import os
import wsl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1300, 800)
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
        self.setMaximumHeight(1000)
        self.setMaximumWidth(1000)
        self.setWindowTitle("PhotoBlend")
        self.labels()
        self.buttons()
        self.checkboxes()
        self.sliders()
        self.setIcon()
        self.show()

        self.images_selected = {"image1": False, "image2": False}

    def labels(self):
        self.pane_label = QLabel(self)
        self.pane_label.setStyleSheet("border: 1px solid black")
        self.pane_label.setGeometry(400, 75, 500, 500)

        self.preview_label = QLabel(self)
        self.preview_label.setText("Image preview")
        self.preview_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: white;")
        self.preview_label.setGeometry(600, 25, 100, 25)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Image Selection")
        self.blend_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: white;")
        self.blend_label.setGeometry(137, 25, 100, 30)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Blending Modes")
        self.blend_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: white;")
        self.blend_label.setGeometry(137, 150, 100, 30)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Image Rotations")
        self.blend_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: white;")
        self.blend_label.setGeometry(137, 650, 100, 30)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Other Options")
        self.blend_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: white;")
        self.blend_label.setGeometry(137, 400, 100, 30)

    def buttons(self):
        self.file_select1 = QPushButton("Select the first image", self)
        self.file_select1.setGeometry(75, 70, 200, 30)
        self.file_select1.clicked.connect(self.image1_clicked)

        self.file_select2 = QPushButton("Select the second image", self)
        self.file_select2.setGeometry(75, 100, 200, 30)
        self.file_select2.clicked.connect(self.image2_clicked)

        self.blend = QPushButton("Blend Images", self)
        self.blend.setGeometry(75, 350, 200, 30)
        self.blend.clicked.connect(self.blend_clicked)

        self.rotate_button = QPushButton("Rotate", self)
        self.rotate_button.setText("Rotate Clockwise")
        self.rotate_button.setGeometry(75, 700, 200, 30)
        self.rotate_button.clicked.connect(self.rotate_clicked)

        self.save_button = QPushButton("Save image", self)
        self.save_button.setGeometry(555, 580, 200, 30)
        self.save_button.clicked.connect(self.save_clicked)

    def checkboxes(self):
        self.add_checkbox = QCheckBox(self, "Add")
        self.add_checkbox.setText("Add")
        self.add_checkbox.setGeometry(25, 200, 150, 30)
        self.add_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.subtract_checkbox = QCheckBox(self, "Subtract")
        self.subtract_checkbox.setText("Subtract")
        self.subtract_checkbox.setGeometry(125, 200, 150, 30)
        self.subtract_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.mult_checkbox = QCheckBox(self, "Multiply")
        self.mult_checkbox.setText("Multiply")
        self.mult_checkbox.setGeometry(225, 200, 150, 30)
        self.mult_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.screen_checkbox = QCheckBox(self, "Screen")
        self.screen_checkbox.setText("Screen")
        self.screen_checkbox.setGeometry(25, 250, 150, 30)
        self.screen_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.overlay_checkbox = QCheckBox(self, "Overlay")
        self.overlay_checkbox.setText("Overlay")
        self.overlay_checkbox.setGeometry(125, 250, 150, 30)
        self.overlay_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.light_checkbox = QCheckBox(self, "Lighten")
        self.light_checkbox.setText("Lighten")
        self.light_checkbox.setGeometry(225, 250, 150, 30)
        self.light_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.dark_checkbox = QCheckBox(self, "Darken")
        self.dark_checkbox.setText("Darken")
        self.dark_checkbox.setGeometry(25, 300, 150, 30)
        self.dark_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.dodge_checkbox = QCheckBox(self, "Color Dodge")
        self.dodge_checkbox.setText("Color Dodge")
        self.dodge_checkbox.setGeometry(125, 300, 150, 30)
        self.dodge_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.burn_checkbox = QCheckBox(self, "Color Burn")
        self.burn_checkbox.setText("Color Burn")
        self.burn_checkbox.setGeometry(225, 300, 150, 30)
        self.burn_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.crop_checkbox = QCheckBox(self, "Crop")
        self.crop_checkbox.setText("Crop")
        self.crop_checkbox.setGeometry(150, 450, 150, 30)

        self.gray_checkbox = QCheckBox(self, "Gray Scale")
        self.gray_checkbox.setText("Gray Scale")
        self.gray_checkbox.setGeometry(150, 500, 150, 30)

        self.filters_checkbox = QCheckBox(self, "Filters")
        self.filters_checkbox.setText("Filters")
        self.filters_checkbox.setGeometry(150, 600, 150, 30)

    def update_blend_checkboxes(self):
        # enable checkboxes if one is deselected (meaning none are selected)
        if self.num_checkboxes_selected() == 0:
            self.add_checkbox.setCheckable(True)
            self.subtract_checkbox.setCheckable(True)
            self.mult_checkbox.setCheckable(True)
            self.screen_checkbox.setCheckable(True)
            self.overlay_checkbox.setCheckable(True)
            self.light_checkbox.setCheckable(True)
            self.dark_checkbox.setCheckable(True)
            self.dodge_checkbox.setCheckable(True)
            self.burn_checkbox.setCheckable(True)

        # otherwise, disable all non-checked blend checkboxes
        else:
            if not self.add_checkbox.isChecked():
                self.add_checkbox.setCheckable(False)
            if not self.subtract_checkbox.isChecked():
                self.subtract_checkbox.setCheckable(False)
            if not self.mult_checkbox.isChecked():
                self.mult_checkbox.setCheckable(False)
            if not self.screen_checkbox.isChecked():
                self.screen_checkbox.setCheckable(False)
            if not self.overlay_checkbox.isChecked():
                self.overlay_checkbox.setCheckable(False)
            if not self.light_checkbox.isChecked():
                self.light_checkbox.setCheckable(False)
            if not self.dark_checkbox.isChecked():
                self.dark_checkbox.setCheckable(False)
            if not self.dodge_checkbox.isChecked():
                self.dodge_checkbox.setCheckable(False)
            if not self.burn_checkbox.isChecked():
                self.burn_checkbox.setCheckable(False)

    def sliders(self):
        self.gray_slider = QSlider(Qt.Horizontal, self)
        self.gray_slider.setRange(0, 255)
        self.gray_slider.setTickInterval(1)
        self.gray_slider.setGeometry(150, 550, 100, 30)

    def setIcon(self):
        appIcon = QIcon("./resources/icon.png")
        self.setWindowIcon(appIcon)

    def image1_clicked(self):
        self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())
        if self.image1[0] != '':  # don't update pane if user cancels file opening
            self.pixmap1 = QPixmap(self.image1[0])
            self.pane_label.setPixmap(
                self.pixmap1.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
            self.images_selected["image1"] = True

    def image2_clicked(self):
        self.image2 = QFileDialog.getOpenFileName(self, "Image 2", QDir.homePath())
        if self.image2[0] != '':  # don't update pane if user cancels file opening
            self.pixmap2 = QPixmap(self.image2[0])
            if self.pixmap2.width() != self.pixmap1.width() and self.pixmap2.height() != self.pixmap1.height():
                msgBox = QMessageBox()
                msgBox.setText("Images are not the same size.")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Warning")
                msgBox.exec_()
            else:
                self.pane_label.setPixmap(
                    self.pixmap2.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
                self.images_selected["image2"] = True

    def num_checkboxes_selected(self):
        clicked_counter = 0
        if self.add_checkbox.isChecked():
            clicked_counter += 1
        if self.subtract_checkbox.isChecked():
            clicked_counter += 1
        if self.mult_checkbox.isChecked():
            clicked_counter += 1
        if self.screen_checkbox.isChecked():
            clicked_counter += 1
        if self.overlay_checkbox.isChecked():
            clicked_counter += 1
        if self.light_checkbox.isChecked():
            clicked_counter += 1
        if self.dark_checkbox.isChecked():
            clicked_counter += 1
        if self.dodge_checkbox.isChecked():
            clicked_counter += 1
        if self.burn_checkbox.isChecked():
            clicked_counter += 1

        return clicked_counter

    def blend_clicked(self):
        # check that two images have been selected
        if not self.images_selected["image1"] or not self.images_selected["image2"]:
            msgBox = QMessageBox()
            msgBox.setText("Ensure two images are selected to blend.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        # check for number of blending modes selected
        # this can be updated if certain blending modes are not mutually exclusive
        num_checkboxes = self.num_checkboxes_selected()
        if num_checkboxes == 0:
            msgBox = QMessageBox()
            msgBox.setText("Select a blending mode to blend images.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        elif num_checkboxes > 1:
            msgBox = QMessageBox()
            msgBox.setText("You can only use one blending mode at a time.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        else:
            image1_name = str(self.image1)
            image1_name = image1_name[2:]
            image2_name = str(self.image2)
            image2_name = image2_name[2:]
            image1_name = image1_name[:-19]
            image2_name = image2_name[:-19]

            # call blend functions below based on user selection
            # note that blend modes are mutually exclusive

            # addition blend
            if self.add_checkbox.isChecked():
                call_blend(image1_name, image2_name, "add")
                result = QPixmap("test_image.jpg")
                self.pane_label.setPixmap(
                    result.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
                os.remove("test_image.jpg")

            # subtraction blend
            elif self.subtract_checkbox.isChecked():
                call_blend(image1_name, image2_name, "subtract")
                result = QPixmap("test_image.jpg")
                self.pane_label.setPixmap(
                    result.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
                os.remove("test_image.jpg")

            # update below when the following functions are supported
            # multiply blend
            elif self.mult_checkbox.isChecked():
                pass
            # screen blend
            elif self.screen_checkbox.isChecked():
                pass
            # overlay blend
            elif self.overlay_checkbox.isChecked():
                pass
            # light blend
            elif self.light_checkbox.isChecked():
                pass
            # dark blend
            elif self.dark_checkbox.isChecked():
                pass
            # color dodge blend
            elif self.dodge_checkbox.isChecked():
                pass
            # color burn blend
            elif self.burn_checkbox.isChecked():
                pass

    def crop_clicked(self):
        pass

    def grayscale_clicked(self):
        pass

    def save_clicked(self):
        save_name = QFileDialog.getSaveFileName(self, "Blended Image", QDir.homePath(), "Images (*.png *.xpm *.jpg)")
        self.pane_label.pixmap().save(save_name[0])

    def rotate_clicked(self):
        transform = QTransform().rotate(90.0)
        self.pane_label.setPixmap(self.pane_label.pixmap().transformed(transform))

    def filters_clicked(self):
        pass


if __name__ == '__main__':
    wsl.set_display_to_host()
    app = QApplication(sys.argv)
    window = Window()
    browse1 = QPushButton
    sys.exit(app.exec_())
