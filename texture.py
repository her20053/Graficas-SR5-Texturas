from struct import *
from utilities import color


class Texture:

    def __init__(self, ruta):

        self.ruta = ruta

        with open(self.ruta, 'rb') as imagen:

            imagen.seek(10)

            headerSize = unpack('=l', imagen.read(4))[0]

            imagen.seek(18)

            self.ancho = unpack('=l', imagen.read(4))[0]
            self.alto = unpack('=l', imagen.read(4))[0]

            imagen.seek(headerSize)

            self.pixeles = []

            for y in range(self.alto):
                self.pixeles.append([])
                for x in range(self.ancho):
                    b = ord(imagen.read(1))
                    g = ord(imagen.read(1))
                    r = ord(imagen.read(1))
                    self.pixeles[y].append(
                        color(r, g, b)
                    )

    def getColor(self, tx, ty):
        x = round(tx * self.ancho)
        y = round(ty * self.alto)

        return self.pixeles[y][x]

    def get_color_with_intensity(self, tx, ty, intensity):
        x = round(tx * self.ancho)
        y = round(ty * self.alto)

        b = round(self.pixeles[y][x][0] * intensity)
        g = round(self.pixeles[y][x][1] * intensity)
        r = round(self.pixeles[y][x][2] * intensity)

        return color(r, g, b)
