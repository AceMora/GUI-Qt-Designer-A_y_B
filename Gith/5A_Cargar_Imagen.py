import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from UiCargar_Imagen import Ui_MainWindow

class Imagen:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.buscar_img)

    def show(self):
        self.main_win.show()

    def buscar_img(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Seleccionar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filename:
            image = cv2.imread(filename)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contour_image = np.zeros_like(image)
            cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)
            height, width, channel = contour_image.shape
            bytesPerLine = 3 * width
            qImg = QtGui.QImage(contour_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.ui.label.setPixmap(pixmap)

if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Imagen()
    main_win.show()
    sys.exit(app.exec_())
