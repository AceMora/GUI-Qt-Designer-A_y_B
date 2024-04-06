import RPi.GPIO as GPIO
import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from Ui_Escritura import Ui_MainWindow

GPIO.setwarnings(False)

class Escritura:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.Led_1)
        self.ui.pushButton_3.clicked.connect(self.Led_2)
        self.ui.Slider_uno.valueChanged.connect(self.Sl_Led3)
        self.ui.Slider_dos.valueChanged.connect(self.Sl_Led4)
        self.led_state = False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        self.pwm_led3 = GPIO.PWM(15, 100)
        self.pwm_led3.start(0)
        self.pwm_led4 = GPIO.PWM(13, 100)
        self.pwm_led4.start(0)
     
    def show(self):
        self.main_win.show()

    def Led_1(self):
        self.led_state = not self.led_state
        LED = 16
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED, GPIO.OUT)

        if self.led_state:
            GPIO.output(LED, GPIO.HIGH)
            self.ui.pushButton.setStyleSheet("color: red")
        else:
            GPIO.output(LED, GPIO.LOW)
            self.ui.pushButton.setStyleSheet("")

    def Led_2(self):
        self.led_state = not self.led_state
        LED = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED, GPIO.OUT)

        if self.led_state:
            GPIO.output(LED, GPIO.HIGH)
            self.ui.pushButton_3.setStyleSheet("color: yellow")
        else:
            GPIO.output(LED, GPIO.LOW)
            self.ui.pushButton_3.setStyleSheet("")

    def Sl_Led3(self,value):
        self.pwm_led3.ChangeDutyCycle(value)

    def Sl_Led4(self,value):
        self.pwm_led4.ChangeDutyCycle(value)
        
if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Escritura()
    main_win.show()
    sys.exit(app.exec_())
