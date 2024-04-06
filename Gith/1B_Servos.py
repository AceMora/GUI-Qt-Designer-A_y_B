import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BOARD)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UiServos import Ui_MainWindow

class Servos:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.textEdit.textChanged.connect(self.seleccion)
        self.ui.Slider.valueChanged.connect(self.angulo)
        self.servo = None

    def show(self):
        self.main_win.show()

    def seleccion(self):
        motores = self.ui.textEdit.toPlainText().strip()
        if motores not in ["motor 1", "motor 2"]:
            self.servo = None
            return
        if motores == "motor 1":
            self.servo = 11
        elif motores == "motor 2":
            self.servo = 12
        angle = self.ui.Slider.value()
        self.mover(self.servo, angle)

    def angulo(self):
        valor = str(self.ui.Slider.value())
        self.ui.label_grados.setText(valor)
        angle = int(valor)
        if self.servo:
            self.mover(self.servo, angle)

    def mover(self, servo_pin, angle):
        if servo_pin is None:
            return
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servo_pin, GPIO.OUT)
        pulso = GPIO.PWM(servo_pin, 50)
        pulso.start(1.5)
        
        for i in range(0, angle):
            grados = ((1.0/18.0) * i) + 2.5
            pulso.ChangeDutyCycle(grados)
        sleep(2)
        pulso.stop()
        GPIO.cleanup()

    def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

       
if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Servos()
    main_win.show()
    sys.exit(app.exec_())
