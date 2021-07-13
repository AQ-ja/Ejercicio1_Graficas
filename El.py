# TODO EL CODIGO USADO, PARTE DEL CODIGO VISTO EN CLASE
import struct


#Empezando las funciones 

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])


BLACK = color(0,0,0)
WHITE = color(1,1,1)

#Trabaja con los espacios (osea los pixeles)
class Renderer(object):
    def __init__(self, width, height):
        self.curr_color = WHITE
        self.clear_color = BLACK
        self.glCreateW(width, height)

    def glCreateW(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    def glCColor(self, r, g, b):
        self.clear_color = color(r, g, b)


    def glClear(self):
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]

    #Color de las barras
    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)

    #Color de los puntos
    def glCColor2(self, r, g, b):
        self.bars_color = color(r, g, b)


    def glPoint(self, x, y):
        self.pixels[x][y] = self.curr_color


    def glBars(self, x, y):
        self.pixels[x][y] = self.bars_color
    

    def glFinished(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color Table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
