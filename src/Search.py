import math


class Search:

    def __init__(self):
        self.coordinates = {}
        self.comunications = {}

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

    def calc_distance(self, est1, est2):
        coor1 = self.coordinates.get(est1)
        coor2 = self.coordinates.get(est2)
        sq1 = (coor1[0] - coor2[0]) ** 2
        sq2 = (coor1[1] - coor2[1]) ** 2
        distancia = math.sqrt(sq1 + sq2)
        return int((distancia*100000)*1.09)


if __name__ == '__main__':
    path = Search()
    path.read_distances('distancias')
    print(path.comunications)
    path.read_coordinates('coordenadas')
    print(path.coordinates)
    print(path.calc_distance('Kifissia', 'KAT'))
    print(path.calc_distance('Kifissia', 'Marousi'))
    print(path.calc_distance('KAT', 'Marousi'))
