from src.GUI.Dani.ventana_minimalista_ui import *
from src.search import Search
from src.GUI.Dani import about_ui, help_ui


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.predetermined_text_origin_comboBox = 'Seleccione Origen'
        self.predetermined_text_destiny_comboBox = 'Seleccione Destino'

        self.fill_comboBoxes()

        self.make_stations_invisible()

        # Menu bar
        self.menu_help = QtWidgets.QAction("Help")
        self.menu_about = QtWidgets.QAction("About us")

        self.menuBar.addAction(self.menu_help)
        self.menuBar.addAction(self.menu_about)

        self.menu_help.triggered.connect(self.to_help)
        self.menu_about.triggered.connect(self.to_about)

        # List result

        # No edition
        self.stations_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stations_list.setDragDropOverwriteMode(False)
        self.stations_list.setSelectionMode(False)
        # self.stations_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.stations_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)

        # Establecer el número de filas
        self.stations_list.setRowCount(50)

        names = ['KAT', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7',
                 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2',
                 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3',
                 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4',
                 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5',
                 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6', 'KAT7', 'KAT2', 'KAT3', 'KAT4', 'KAT5', 'KAT6',
                 'KAT7']
        cont = 1
        cont2 = 0
        for i in names:
            num = QtWidgets.QTableWidgetItem(str(cont))
            num.setTextAlignment(4)
            parada = QtWidgets.QTableWidgetItem(i)
            parada.setTextAlignment(4)
            self.stations_list.setItem(cont2, 0, num)
            self.stations_list.setItem(cont2, 1, parada)
            cont += 1
            cont2 += 1

        # Limpiar la table
        # self.stations_list.clear()

        '''
        nombre_columnas = ("Numero", "Parada")
        self.header = QtWidgets.QHeaderView()
        self.stations_list.setHorizontalHeader(self.header)
        # self.stations_list.setHorizontalHeader()
        
        self.numero = QtWidgets.QAction("Numero")
        self.parada = QtWidgets.QAction("Parada")

        self.stations_list.addAction(self.numero)
        self.stations_list.addAction(self.parada)

        self.numero.setVisible(False)
        self.parada.setVisible(False)
        '''

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

        self.origin_comboBox.setToolTip("Origen")
        self.destiny_comboBox.setToolTip("Destino")

        self.origin_comboBox.addItem(self.predetermined_text_origin_comboBox)
        self.destiny_comboBox.addItem(self.predetermined_text_destiny_comboBox)

        with open('../../../data/coordenadas') as file:
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
            functionality = Search()
            came_from = functionality.algorithm_astar(origin, destiny)
            path = functionality.obtain_path(came_from, origin, destiny)

            speed = 82.5
            distance, minutes, seconds = functionality.coste_camino(path, speed)
            stations_number = len(path)
            self.set_text(minutes, seconds, stations_number, distance)

            self.print_route(path)

    def make_stations_invisible(self):
        for i in self.frame_paradas.children():
            i.setVisible(False)

    def print_route(self, path):
        self.make_stations_invisible()
        path = [f"i_{station.replace(' ', '_')}" for station in path]
        i_paradas = self.frame_paradas.children()
        for i in i_paradas:
            if i.objectName() in path:
                i.setVisible(True)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
