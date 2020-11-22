from src.GUI.Dani.ventana_minimalista_ui import *
from src.search import Search


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Athens Metro")

        self.predetermined_text_origin_comboBox = 'Seleccione Origen'
        self.predetermined_text_destiny_comboBox = 'Seleccione Destino'

        self.fill_comboBoxes()

        # self.pushButton.setText("Go!")
        # self.label_origen.setText("Origen")
        # self.label_destino.setText("Destino")
        # self.desplegable_origen.addItem("Hola")
        # self.desplegable_origen.addItem("Hola2")

    def fill_comboBoxes(self):
        icon_circle_red = QtGui.QIcon()
        icon_circle_green = QtGui.QIcon()
        icon_circle_blue = QtGui.QIcon()
        icon_circle_yellow = QtGui.QIcon()

        icon_circle_red.addPixmap(QtGui.QPixmap("../../../image/circle_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_circle_green.addPixmap(QtGui.QPixmap("../../../image/circle_green.png"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
        icon_circle_blue.addPixmap(QtGui.QPixmap("../../../image/circle_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_circle_yellow.addPixmap(QtGui.QPixmap("../../../image/circle_yellow.png"), QtGui.QIcon.Normal,
                                     QtGui.QIcon.Off)

        self.origin_comboBox.addItem(self.predetermined_text_origin_comboBox)
        self.destiny_comboBox.addItem(self.predetermined_text_destiny_comboBox)

        # self.origin_comboBox.addItem(icon_circle_green,"adios")
        # self.origin_comboBox.addItem(icon_circle_green,str)

        with open('../../../data/coordenadas') as file:
            for linea in file:
                palabras = linea.split(",")
                estacion = palabras[0]
                linea = int(palabras[3])
                if estacion in ['Attikki', 'Omonia', 'Monastiraki', 'Syntagma']:
                    self.origin_comboBox.addItem(icon_circle_yellow, estacion)
                    self.destiny_comboBox.addItem(icon_circle_yellow, estacion)
                elif linea == 1:
                    self.origin_comboBox.addItem(icon_circle_green, estacion)
                    self.destiny_comboBox.addItem(icon_circle_green, estacion)
                elif linea == 2:
                    self.origin_comboBox.addItem(icon_circle_red, estacion)
                    self.destiny_comboBox.addItem(icon_circle_red, estacion)
                elif linea == 3:
                    self.origin_comboBox.addItem(icon_circle_blue, estacion)
                    self.destiny_comboBox.addItem(icon_circle_blue, estacion)

        self.origin_comboBox.currentTextChanged.connect(self.calculate_route)
        self.destiny_comboBox.currentTextChanged.connect(self.calculate_route)

    def calculate_route(self):
        origin = self.origin_comboBox.currentText()
        destiny = self.destiny_comboBox.currentText()
        if origin != self.predetermined_text_origin_comboBox \
                and destiny != self.predetermined_text_destiny_comboBox:
            print("hola")
            path = Search()
            print("Hola2")
            came_from = path.algorithm_astar(origin, destiny)
            camino = path.obtain_path(came_from, origin, destiny)
            velocidad = 82.5
            distancia, minutos, segundos = path.coste_camino(camino, velocidad)
            print(camino)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
