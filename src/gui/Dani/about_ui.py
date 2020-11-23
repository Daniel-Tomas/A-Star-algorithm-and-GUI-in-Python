# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(586, 354)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        AboutWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../image/1200px-Athens_Metro_Logo.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 10, 452, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aaron = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.aaron.setFont(font)
        self.aaron.setObjectName("aaron")
        self.verticalLayout.addWidget(self.aaron)
        self.sergio = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.sergio.setFont(font)
        self.sergio.setObjectName("sergio")
        self.verticalLayout.addWidget(self.sergio)
        self.daniel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.daniel.setFont(font)
        self.daniel.setObjectName("daniel")
        self.verticalLayout.addWidget(self.daniel)
        self.juan = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.juan.setFont(font)
        self.juan.setObjectName("juan")
        self.verticalLayout.addWidget(self.juan)
        self.xiao = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.xiao.setFont(font)
        self.xiao.setObjectName("xiao")
        self.verticalLayout.addWidget(self.xiao)
        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 24))
        self.menubar.setObjectName("menubar")
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWindow)
        self.statusbar.setObjectName("statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About"))
        self.aaron.setText(_translate("AboutWindow", "Aaron Cabero Blanco"))
        self.sergio.setText(_translate("AboutWindow", "Sergio Sanchez-Carvajales Francoy"))
        self.daniel.setText(_translate("AboutWindow", "Daniel Tomas Sanchez"))
        self.juan.setText(_translate("AboutWindow", "Juan Diego Valencia Marin"))
        self.xiao.setText(_translate("AboutWindow", "Xiao Peng Ye"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())

