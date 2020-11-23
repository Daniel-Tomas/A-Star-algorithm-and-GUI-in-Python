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
        MainWindow.resize(1100, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.image_container = QtWidgets.QFrame(self.centralwidget)
        self.image_container.setGeometry(QtCore.QRect(0, 0, 550, 600))
        self.image_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_container.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_container.setLineWidth(20)
        self.image_container.setMidLineWidth(20)
        self.image_container.setObjectName("image_container")
        self.metro_image = QtWidgets.QLabel(self.image_container)
        self.metro_image.setGeometry(QtCore.QRect(0, 0, 550, 600))
        self.metro_image.setStyleSheet("background-color: rgb(205, 236, 255);")
        self.metro_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.metro_image.setText("")
        self.metro_image.setPixmap(QtGui.QPixmap("../../../image/map.png"))
        self.metro_image.setScaledContents(False)
        self.metro_image.setWordWrap(True)
        self.metro_image.setObjectName("metro_image")
        self.options_container = QtWidgets.QFrame(self.centralwidget)
        self.options_container.setGeometry(QtCore.QRect(550, 0, 550, 600))
        self.options_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_container.setObjectName("options_container")
        self.comboBox = QtWidgets.QComboBox(self.options_container)
        self.comboBox.setGeometry(QtCore.QRect(70, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.options_container)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../image/flag.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.options_container)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../image/mapa-color.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.options_container)
        self.listView.setGeometry(QtCore.QRect(60, 260, 441, 271))
        self.listView.setObjectName("listView")
        self.metro_image_2 = QtWidgets.QLabel(self.options_container)
        self.metro_image_2.setGeometry(QtCore.QRect(-410, -160, 1261, 781))
        self.metro_image_2.setText("")
        self.metro_image_2.setPixmap(QtGui.QPixmap("../../../image/metro-difuminado.jpg"))
        self.metro_image_2.setScaledContents(True)
        self.metro_image_2.setObjectName("metro_image_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.options_container)
        self.comboBox_3.setGeometry(QtCore.QRect(350, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.metro_image_2.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.listView.raise_()
        self.comboBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Seleccione Origen"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Seleccione Destino"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

