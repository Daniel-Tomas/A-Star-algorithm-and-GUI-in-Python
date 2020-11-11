from PySide2.QtWidgets import QApplication, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Esto es una prueba")
        self.setGeometry(300, 300, 300, 300)

        self.setMaximumHeight(600)
        self.setMinimumHeight(200)
        self.setMaximumWidth(600)
        self.setMinimumWidth(200)
        self.show()


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
