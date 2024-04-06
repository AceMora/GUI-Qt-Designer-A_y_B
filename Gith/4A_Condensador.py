from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 450, 351, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 500, 351, 16))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(30, 540, 351, 16))
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 170, 701, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 10, 231, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo_ecci.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 420, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 470, 231, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 520, 301, 16))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 0, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 60, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "R"))
        self.label_4.setText(_translate("MainWindow", "C"))
        self.label_5.setText(_translate("MainWindow", "V"))
        self.label_8.setText(_translate("MainWindow", "2024 - 1"))
        self.label_6.setText(_translate("MainWindow", "Andres Acevedo Cod 55305"))
        self.label_7.setText(_translate("MainWindow", "Hector Patarroyo Cod 54528"))
        self.label_9.setText(_translate("MainWindow", "Ingenieria Mecatronica"))
        self.label_10.setText(_translate("MainWindow", "Carlos Bejarano Cod "))

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        
        self.horizontalSlider.valueChanged[int].connect(self.valor_res)
        self.horizontalSlider_2.valueChanged[int].connect(self.valor_cap)
        self.horizontalSlider_3.valueChanged[int].connect(self.valor_volt)

        self.plot_figure = plt.figure()
        self.plot_canvas = FigureCanvas(self.plot_figure)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plot_canvas)
        self.graphicsView.setLayout(layout)

        self.resistencia = 1
        self.capacitancia = 1
        self.voltaje = 1

    def valor_res(self, value):
        self.resistencia = value
        self.label_3.setText(f"Resistencia: {value}")
        self.crear_graf()

    def valor_cap(self, value):
        self.capacitancia = value* 1e-6
        self.label_4.setText(f"Capacitancia: {value}")
        self.crear_graf()

    def valor_volt(self, value):
        self.voltaje = value
        self.label_5.setText(f"Voltaje: {value}")
        self.crear_graf()

    def crear_graf(self):
        t = np.linspace(0, 5 * self.resistencia * self.capacitancia, 1000)
        carga = self.voltaje * (1 - np.exp(-t / (self.resistencia * self.capacitancia)))
        descarga = self.voltaje * np.exp(-t / (self.resistencia * self.capacitancia))

        self.plot_figure.clear()
        plt.plot(t, carga, label='Carga')
        plt.plot(t, descarga, label='Descarga')
        plt.title('Carga y descarga de un capacitor en un circuito RC')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Voltaje (V)')
        plt.legend()
        self.plot_canvas.draw()
        plt.ylim(0, self.voltaje)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
