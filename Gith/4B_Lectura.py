from gpiozero import Button
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from Ui_Lectura import Ui_MainWindow

class Lectura:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.Inicia)
        self.button = Button(4)
        self.a = "Alto"
        self.b = "Bajo"

    def show(self):
        self.main_win.show()

    def Inicia(self):
        self.button.when_pressed = self.estado_high
        self.button.when_released = self.estado_low

    def estado_high(self):
        self.ui.label.setText(str(self.a))
        self.ui.label.setStyleSheet("color: red")

    def estado_low(self):
        self.ui.label.setText(str(self.b))
        self.ui.label.setStyleSheet("color: blue")

if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Lectura()
    main_win.show()
    sys.exit(app.exec_())
