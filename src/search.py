import math
from queue import PriorityQueue


class Search:

    def __init__(self):
        self.coordinates = {}
        self.comunications = {}
        self.read_distances('../../../data/distancias')
        self.read_coordinates('../../../data/coordenadas')

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
            linea = int(palabras[3])
            coor.append(linea)
            self.coordinates[estacion] = coor

    def dist_aerea(self, est1, est2):
        coor1 = self.coordinates.get(est1)
        coor2 = self.coordinates.get(est2)
        sq1 = (coor1[0] - coor2[0]) ** 2
        sq2 = (coor1[1] - coor2[1]) ** 2
        distancia = math.sqrt(sq1 + sq2)
        if coor1[2] != coor2[2]:
            distancia += 30
        return distancia * 100 * 1.025

    def dist_est(self, origen, destino):
        com = self.comunications.get(origen)
        res = 0
        for i in range(0, len(com), 2):
            if com[i] == destino:
                res = com[i + 1]
        return res

    def coste_camino(self, camino, velocidad):
        distancia = 0
        for i in range(len(camino) - 1):
            origen = camino[i]
            destino = camino[i + 1]
            distancia = distancia + self.dist_est(origen, destino)
        distancia *= 1.005
        segundos = (distancia / velocidad) * 3600 + 95 * (len(camino) - 1)
        minutos = int(segundos / 60)
        segundos = int(segundos % 60)
        return distancia, minutos, segundos

    def algorithm_astar(self, origen, destino):
        frontier = PriorityQueue()
        frontier.put((0, origen))
        came_from = {}
        came_from[origen] = None
        cost_so_far = {}
        cost_so_far[origen] = 0
        while not frontier.empty():
            current = frontier.get()[1]
            if current == destino:
                break
            com = self.comunications.get(current)
            for i in range(0, len(com), 2):
                next = com[i]
                cost_next = com[i + 1]
                new_cost = cost_so_far[current] + cost_next + self.dist_aerea(next, destino)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put((priority, next))
                    came_from[next] = current
        return came_from

    def obtain_path(self, came_from, origen, destino):
        res = []
        actual = destino
        while True:
            res.append(actual)
            if actual == origen:
                break
            actual = came_from.get(actual)
        res.reverse()
        return res


if __name__ == '__main__':
    path = Search()
    origen = 'Evangelismos'
    destino = 'KAT'
    came_from = path.algorithm_astar(origen, destino)
    camino = path.obtain_path(came_from, origen, destino)
    velocidad = 82.5
    distancia, minutos, segundos = path.coste_camino(camino, velocidad)
    print(f'Camino a realizar: {camino}')
    print("Distancia a recorrer:", "{:.2f}".format(distancia), 'km')
    print(f'Tiempo empleado: {minutos} minutos y {segundos} segundos')
