# Libreria GL utilizada para comunicarse con el render:
from render import *
import render
import texture

objetoRender = None

# GLInit crea una nuevo objeto Render con las dimensiones indicadas por el usuario:


def glInit(width, height):
    glCreateWindow(width, height)


def glCreateWindow(width, height):
    global objetoRender
    objetoRender = Render(width, height)


# GlClear limpia la ventana de dibujo:


def glClear():
    objetoRender.clear()


# GLClearColor especifica el color de fondo de la ventana de dibujo:


def glClearColor(r, g, b):
    objetoRender.clear_color = color(round(255*r), round(255*g), round(255*b))
    glClear()


# GLColor estabelece el color de dibujo:

def glColor(r, g, b):
    objetoRender.current_color = color(
        round(255*r), round(255*g), round(255*b))


def glApplyTexture(TextureBMPFileName, objectFileName, scaleFactor, translateFactor):
    glClearColor(0, 0, 0)
    glClear()
    objetoRender.texture = texture.Texture(TextureBMPFileName)
    glRenderObject(objectFileName, scaleFactor, translateFactor)


def glLoadTexture(ObjectFileName, textureFileName):

    textura = texture.Texture(textureFileName)

    objetoRender.framebuffer = textura.pixeles

    cubo = render.Obj(ObjectFileName)

    glColor(1, 1, 1)

    for cara in cubo.faces:

        face = cara['face']

        if len(face) == 3:

            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1

            vt1 = V3(
                cubo.tvertices[ft1][0] * textura.ancho,
                cubo.tvertices[ft1][1] * textura.ancho
            )
            vt2 = V3(
                cubo.tvertices[ft2][0] * textura.ancho,
                cubo.tvertices[ft2][1] * textura.ancho
            )
            vt3 = V3(
                cubo.tvertices[ft3][0] * textura.ancho,
                cubo.tvertices[ft3][1] * textura.ancho
            )

            glLine(vt1, vt2)
            glLine(vt2, vt3)
            glLine(vt3, vt1)

    glFinish("textura_vertices_SR5.bmp")


# GLLine especifica una linea entre dos vertices:


def glLine(v1, v2):
    objetoRender.line(v1, v2)

# GLTriangle crea un triangulo con los vertices especificados:


def glTriangle(A, B, C, col):
    objetoRender.current_color = color(
        round(255*col[0]), round(255*col[1]), round(255*col[2]))
    objetoRender.barycentricTriangle(A, B, C)

# GLPoint crea un punto en la posicion (x, y)


def glPoint(x, y):
    objetoRender.point(x, y)

# GLRenderObject especifica el nombre, la escala y la posicion del objeto a renderizar:


def glRenderObject(name, scaleFactor, translateFactor):
    objetoRender.renderObject(name, scaleFactor, translateFactor)

# GLFinish especifica el nombre del archivo en el que se guardara la imagen y termina el dibujo:


def glFinish(fileName):
    objetoRender.write(fileName)
