# Modulo main.py, utilizado para iniciar laboratorios de graficas:

# Se importa la libreria gl.py para poder utilizar las funciones de OpenGL
from gl import *


# Se crea un canvas para poder dibujar:
glInit(width=1024, height=1024)

glLoadTexture(ObjectFileName='./assets/StarWars.obj',
              textureFileName='./assets/StarWars.bmp')


glInit(width=1024, height=1024)
glApplyTexture(TextureBMPFileName='./assets/IG.bmp', objectFileName='./assets/StarWars.obj',
               scaleFactor=(400, 400, 400), translateFactor=(500, 50, 0))
nombreArchivo = 'SR5.bmp'
glFinish(nombreArchivo)
