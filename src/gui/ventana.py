from PyQt5 import QtWidgets, QtGui
from gui.ventana_ui import Ui_MainWindow
from gui import about_ui, help_ui
from util import resource_path
from search import AStar


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.predetermined_text_origin_comboBox = 'Seleccione Origen'
        self.predetermined_text_destiny_comboBox = 'Seleccione Destino'

        self.fill_comboBoxes()

        self.no_edition_table()

        self.make_stations_invisible()

        # Menu bar
        self.menu_help = QtWidgets.QAction("Help")
        self.menu_about = QtWidgets.QAction("About us")

        self.menuBar.addAction(self.menu_help)
        self.menuBar.addAction(self.menu_about)

        self.menu_help.triggered.connect(self.to_help)
        self.menu_about.triggered.connect(self.to_about)

    def fill_comboBoxes(self):
        icon_circle_red = QtGui.QIcon()
        icon_circle_green = QtGui.QIcon()
        icon_circle_blue = QtGui.QIcon()
        icon_circle_yellow = QtGui.QIcon()

        icon_circle_red.addPixmap(QtGui.QPixmap(resource_path("image/circle_red.png")),
                                  QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_circle_green.addPixmap(
            QtGui.QPixmap(resource_path("image/circle_green.png")), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        icon_circle_blue.addPixmap(
            QtGui.QPixmap(resource_path("image/circle_blue.png")), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        icon_circle_yellow.addPixmap(
            QtGui.QPixmap(resource_path("image/circle_yellow.png")), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)

        self.origin_comboBox.setToolTip("Origen")
        self.destiny_comboBox.setToolTip("Destino")

        self.origin_comboBox.addItem(self.predetermined_text_origin_comboBox)
        self.destiny_comboBox.addItem(self.predetermined_text_destiny_comboBox)

        with open(resource_path("data/coordenadas")) as file:
            for linea in file:
                palabras = linea.split(",")
                estacion = palabras[0]
                linea = int(palabras[3])
                if estacion in ['Attiki', 'Omonia', 'Monastiraki', 'Syntagma']:
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
            functionality = AStar()
            came_from = functionality.algorithm_astar(origin, destiny)
            path = functionality.obtain_path(came_from, origin, destiny)

            speed = 82.5
            distance, minutes, seconds = functionality.coste_camino(path, speed)
            stations_number = len(path)
            self.set_text(minutes, seconds, stations_number, distance)

            # Path
            self.clear_list()
            self.print_list(path)
            self.print_route(path)

    def print_route(self, path):
        self.make_stations_invisible()
        path = [f"i_{station.replace(' ', '_')}" for station in path]
        i_paradas = self.frame_paradas.children()
        for i in i_paradas:
            if i.objectName() in path:
                i.setVisible(True)

    def make_stations_invisible(self):
        for i in self.frame_paradas.children():
            i.setVisible(False)

    def print_list(self, path):
        self.stations_list.setRowCount(len(path))
        cont = 1
        cont2 = 0
        for i in path:
            num = QtWidgets.QTableWidgetItem(str(cont))
            num.setTextAlignment(4)
            parada = QtWidgets.QTableWidgetItem(i)
            # parada.setTextAlignment(4)
            self.stations_list.setItem(cont2, 0, num)
            self.stations_list.setItem(cont2, 1, parada)
            cont += 1
            cont2 += 1

    def clear_list(self):
        self.stations_list.clearContents()
        self.stations_list.setRowCount(1)

    def no_edition_table(self):
        self.stations_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stations_list.setDragDropOverwriteMode(False)
        self.stations_list.setSelectionMode(False)
        self.stations_list.horizontalHeader().setStretchLastSection(True)
        self.stations_list.setAlternatingRowColors(True)
        self.stations_list.setColumnWidth(0, 120)

    def menu_bar(self):
        connect_us = self.actionUs
        connect_us.triggered.connect(self.to_about)
        connect_help = self.actionHelp
        connect_help.triggered.connect(self.to_help)

    def to_about(self):
        self.ab_window = about_ui.QtWidgets.QMainWindow()
        ab_ui = about_ui.Ui_AboutWindow()
        ab_ui.setupUi(self.ab_window)
        self.ab_window.show()

    def to_help(self):
        self.help_window = help_ui.QtWidgets.QMainWindow()
        he_ui = help_ui.Ui_Help_Window()
        he_ui.setupUi(self.help_window)
        self.help_window.show()

    def set_text(self, minutes, seconds, stations_number, distance):
        self.time_value.setText(f'{minutes} min. {seconds} s.')
        self.stations_value.setText(str(stations_number))
        self.distances_value.setText(f'{distance:.2f} Km')