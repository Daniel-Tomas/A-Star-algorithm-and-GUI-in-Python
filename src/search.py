import math
from queue import PriorityQueue
import copy


class Search:

    def __init__(self):
        self.coordinates = {}
        self.comunications = {}
        self.read_distances('..\data\distancias')
        self.read_coordinates('..\data\coordenadas')

    def read_distances(self, file):
        f = open(file, 'r')
        for linea in f:
            palabras = linea.split(";")
            origen = palabras[0]
            destino = palabras[1]
            distancia = palabras[2]
            if not origen in self.comunications.keys():
                com = []
                com.append(destino)
                com.append(float(distancia))
                self.comunications[origen] = com
            else:
                com = self.comunications.get(origen)
                com.append(destino)
                com.append(float(distancia))

    def read_coordinates(self, file):
        f = open(file, 'r')
        for linea in f:
            palabras = linea.split(",")
            estacion = palabras[0]
            coor = []
            latitud = float(palabras[1])
            coor.append(latitud)
            longitud = float(palabras[2])
            coor.append(longitud)
            self.coordinates[estacion] = coor

    def dist_aerea(self, est1, est2):
        coor1 = self.coordinates.get(est1)
        coor2 = self.coordinates.get(est2)
        sq1 = (coor1[0] - coor2[0]) ** 2
        sq2 = (coor1[1] - coor2[1]) ** 2
        distancia = math.sqrt(sq1 + sq2)
        return distancia * 100 * 1.025

    def dist_est(self, origen, destino):
        com = self.comunications.get(origen)
        for i in range(0, len(com), 2):
            if com[i] == destino:
                return com[i + 1]

    def distancia_camino(self, camino):
        res = 0
        for i in range(len(camino) - 1):
            origen = camino[i]
            destino = camino[i + 1]
            res = res + self.dist_est(origen, destino)
        return res

    def algorithm_astar(self, origen, destino):
        visitados = []
        opciones = PriorityQueue()
        stations = {}
        camino = [origen]
        stations[origen] = camino
        distancia = {}
        distancia[origen] = 0
        actual = origen
        while destino not in visitados:
            if actual in visitados:
                continue
            visitados.append(actual)
            com = self.comunications.get(actual)
            dist_actual = distancia.get(actual)
            for i in range(0, len(com), 2):
                siguiente = com[i]
                dist_siguiente = dist_actual + self.dist_est(actual, siguiente) + self.dist_aerea(actual,siguiente)
                opciones.put((dist_siguiente, siguiente))
            siguiente = opciones.get()[1]
            dist_siguiente = distancia.get(actual) + self.dist_est(actual, siguiente)
            distancia[siguiente] = dist_siguiente
            cam_siguiente = copy.copy(stations[actual])
            cam_siguiente.append(siguiente)
            stations[siguiente] = cam_siguiente
            actual = siguiente
        return stations.get(destino)


if __name__ == '__main__':
    path = Search()
    print(path.comunications)
    print(path.coordinates)
    res = path.algorithm_astar('Piraeus', 'Moschato')
    print(res)
    print(path.dist_est('Piraeus', 'Faliro'))
