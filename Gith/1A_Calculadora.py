import sys
import math
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UiCalculadora import Ui_MainWindow

class Calculadora:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.mostrar_resultado)
        self.ui.pushButton_2.clicked.connect(self.resta)
        self.ui.pushButton_3.clicked.connect(self.mult)
        self.ui.pushButton_4.clicked.connect(self.div)
        self.ui.pushButton_7.clicked.connect(self.residuo)
        self.ui.pushButton_8.clicked.connect(self.sen)
        self.ui.pushButton_6.clicked.connect(self.cos)
        self.ui.pushButton_5.clicked.connect(self.tan)
        self.ui.pushButton_11.clicked.connect(self.cot)
        self.ui.pushButton_9.clicked.connect(self.sec)
        self.ui.pushButton_10.clicked.connect(self.csc)

    def show(self):
        self.main_win.show()

    def mostrar_resultado(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            num2 = float(self.ui.textEdit_2.toPlainText())
            resultado = num1 + num2
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def resta(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            num2 = float(self.ui.textEdit_2.toPlainText())
            resultado = num1 - num2
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def mult(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            num2 = float(self.ui.textEdit_2.toPlainText())
            resultado = num1 * num2
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def div(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            num2 = float(self.ui.textEdit_2.toPlainText())
            resultado = num1 / num2
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def residuo(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            num2 = float(self.ui.textEdit_2.toPlainText())
            resultado = num1 % num2
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def sen(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = math.sin(num1)  
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def cos(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = math.cos(num1)
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def tan(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = math.tan(num1)
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def cot(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = 1 / math.tan(num1)
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def sec(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = 1 / math.cos(num1)
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")

    def csc(self):
        try:
            num1 = float(self.ui.textEdit.toPlainText())
            resultado = 1 / math.sin(num1)
            self.ui.label_2.setText(str(resultado))
        except ValueError:
            self.ui.textEdit_3.setText("Error: Ingrese números válidos")
       
if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Calculadora()
    main_win.show()
    sys.exit(app.exec_())
