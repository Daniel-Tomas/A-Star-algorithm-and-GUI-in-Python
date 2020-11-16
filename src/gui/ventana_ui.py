# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 60, 151, 61))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.desplegable_origen = QtWidgets.QComboBox(self.centralwidget)
        self.desplegable_origen.setGeometry(QtCore.QRect(150, 70, 221, 31))
        self.desplegable_origen.setObjectName("desplegable_origen")
        self.label_origen = QtWidgets.QLabel(self.centralwidget)
        self.label_origen.setGeometry(QtCore.QRect(20, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_origen.setFont(font)
        self.label_origen.setObjectName("label_origen")
        self.label_destino = QtWidgets.QLabel(self.centralwidget)
        self.label_destino.setGeometry(QtCore.QRect(410, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_destino.setFont(font)
        self.label_destino.setObjectName("label_destino")
        self.desplegable_destino = QtWidgets.QComboBox(self.centralwidget)
        self.desplegable_destino.setGeometry(QtCore.QRect(530, 70, 221, 31))
        self.desplegable_destino.setObjectName("desplegable_destino")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_origen.setText(_translate("MainWindow", "TextLabel"))
        self.label_destino.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

