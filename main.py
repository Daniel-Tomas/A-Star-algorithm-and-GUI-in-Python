from PySide2.QtWidgets import QApplication
from src.gui.ventana import MainWindow
import sys

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    myApp.exec_()
    sys.exit(0)
