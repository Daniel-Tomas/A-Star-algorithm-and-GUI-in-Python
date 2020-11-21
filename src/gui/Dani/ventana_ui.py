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
        MainWindow.resize(1102, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.image_container = QtWidgets.QFrame(self.centralwidget)
        self.image_container.setGeometry(QtCore.QRect(20, 30, 581, 631))
        self.image_container.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.image_container.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_container.setFrameShadow(QtWidgets.QFrame.Raised)

        self.image_container.setLineWidth(20)
        self.image_container.setMidLineWidth(20)
        self.image_container.setObjectName("image_container")
        self.metro_image = QtWidgets.QLabel(self.image_container)
        self.metro_image.setGeometry(QtCore.QRect(10, 10, 561, 601))
        self.metro_image.setText("")
        self.metro_image.setPixmap(QtGui.QPixmap("../../../image/map.png"))
        self.metro_image.setScaledContents(False)
        self.metro_image.setObjectName("metro_image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

