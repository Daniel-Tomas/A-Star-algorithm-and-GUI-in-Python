from PyQt5 import QtCore, QtGui, QtWidgets
from util import resource_path


class Ui_Help_Window(object):
    def setupUi(self, Help_Window):
        Help_Window.setObjectName("Help_Window")
        Help_Window.resize(467, 327)
        Help_Window.setMinimumSize(QtCore.QSize(467, 327))
        Help_Window.setMaximumSize(QtCore.QSize(467, 327))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        Help_Window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(resource_path("image/1200px-Athens_Metro_Logo.svg.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off))
        Help_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Help_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(38, 19, 381, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.pasos = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pasos.setContentsMargins(0, 0, 0, 0)
        self.pasos.setObjectName("pasos")
        self.grupo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        self.grupo.setFont(font)
        self.grupo.setTextFormat(QtCore.Qt.AutoText)
        self.grupo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.grupo.setObjectName("grupo")
        self.pasos.addWidget(self.grupo)
        self.aaron = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.aaron.setFont(font)
        self.aaron.setObjectName("aaron")
        self.pasos.addWidget(self.aaron)
        self.aaron_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.aaron_2.setFont(font)
        self.aaron_2.setObjectName("aaron_2")
        self.pasos.addWidget(self.aaron_2)
        self.fondo = QtWidgets.QFrame(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 571, 441))
        self.fondo.setMinimumSize(QtCore.QSize(571, 441))
        self.fondo.setMaximumSize(QtCore.QSize(571, 441))
        self.fondo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo.setObjectName("fondo")
        self.fondo.raise_()
        self.verticalLayoutWidget.raise_()
        Help_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Help_Window)
        QtCore.QMetaObject.connectSlotsByName(Help_Window)

    def retranslateUi(self, Help_Window):
        _translate = QtCore.QCoreApplication.translate
        Help_Window.setWindowTitle(_translate("Help_Window", "Help"))
        self.grupo.setText(_translate("Help_Window", "Pasos:"))
        self.aaron.setText(_translate("Help_Window", "1. Seleccione Origen"))
        self.aaron_2.setText(_translate("Help_Window", "2. Seleccione Destino"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Help_Window = QtWidgets.QMainWindow()
    ui = Ui_Help_Window()
    ui.setupUi(Help_Window)
    Help_Window.show()
    sys.exit(app.exec_())
