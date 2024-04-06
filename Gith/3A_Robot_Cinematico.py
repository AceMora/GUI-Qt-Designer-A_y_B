import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UiRobot import Ui_MainWindow

class Robot_Cinematico:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.comboBox.currentIndexChanged.connect(self.cargar_en_label)

    def show(self):
        self.main_win.show()

    def cargar_en_label(self):
        selec_robot = self.ui.comboBox.currentText()
        descripcion = ""
        cargar_imagen = ""
        if selec_robot == "Robot_Cartesiano":
            descripcion = "Es un robot PPP, el cual tiene tres movimientos lineales y perpendiculares entre sí, en los tres ejes cartesianos X, Y y Z. Este tipo de robot se emplea en trabajos de carga, desplazamiento y descarga de materiales, en aplicaciones de sellado, ensamblaje, manejo de máquinas-herramientas, y soldadura al arco."
            cargar_imagen = "robot_cartesiano.jpg"
        elif selec_robot == "Robot_Cilindrico":
            descripcion = "Es un robot RPP, que cuenta con una articulación rotacional y dos prismáticas. Son utilizados en operaciones de ensamblaje, manejo de máquinas-herramientas, soldaduras por puntos, y manejo, vaciado y moldeado de metales, Los robots cilíndricos utilizan un sistema de coordenadas 3-D con un eje de referencia preferido y una distancia relativa desde él para determinar la posición del punto. La distancia a un posicionamiento de referencia seleccionado y la dirección relativa de los ejes, y la distancia a la vertical del eje desde un plano de referencia designado se utilizan a menudo para especificar la ubicación del punto."
            cargar_imagen = "OIP.jpeg"
        elif selec_robot == "Robot_Esferico":
            descripcion = "Es un robot RRP, el cual tiene dos articulaciones rotacionales y una prismática; aplicado en máquinas-herramientas, soldaduras por puntos, vaciado de metales, frezado, soldadura a gas, y soldadura al arco.La carcasa esférica generalmente está construida de plástico translúcido sólido, material opaco o flexible para mecanismos de accionamiento únicos y otras aplicaciones especiales, esta carcasa esférica sellará el robot del entorno externo. Hay robots esféricos reconfigurables que pueden convertir la superficie esférica en varias configuraciones y realizar otras tareas además de rodar"
            cargar_imagen = "polar-robot.jpg"
        
        
        self.ui.label_3.setText(descripcion)
        pixmap = QtGui.QPixmap(cargar_imagen)
        self.ui.label_4.setPixmap(pixmap)
        self.ui.label_4.setScaledContents(True)


if __name__ =="__main__":
    app =QApplication(sys.argv)
    main_win = Robot_Cinematico()
    main_win.show()
    sys.exit(app.exec_())
