from src.gui.ventana_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Metro Atenas")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("metroicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.pushButton.setText("Go!")
        self.label_origen.setText("Origen")
        self.label_destino.setText("Destino")
        self.desplegable_origen.addItem("Hola")
        self.desplegable_origen.addItem("Hola2")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
