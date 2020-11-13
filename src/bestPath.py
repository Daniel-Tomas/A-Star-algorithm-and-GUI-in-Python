class bestPath:
    def readDistances(file):
        f = open(file, 'r')
        dict = {}
        for linea in f:
            palabras = linea.split(";")
            origen = palabras[0]
            destino = palabras[1]
            distancia = palabras[2]
            if not origen in dict.keys():
                com = []
                com.append(destino)
                com.append(float(distancia))
                dict[origen] = com
            else:
                com = dict.get(origen)
                com.append(destino)
                com.append(float(distancia))
        return dict

    if __name__ == '__main__':
        dict = readDistances('distancias')
        print(dict)
