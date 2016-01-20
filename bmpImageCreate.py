__author__ = 'levitan'

from PIL import Image
from numpy import *


def bmpImageCreateRGB(x, y, name, function):
    c = Image.new("RGB", (x, y))
    meshArray = function(x, y)
    for i in range(0, x):
        for j in range(0, y):
            c.putpixel([i, j], (int(meshArray[i][j]), int(meshArray[i][j]), int(meshArray[i][j])))
    # c.show()
    c.save("%s.bmp" % name)


def bmpImageCreateWB(x, y, name, funtion):
    c = Image.new('1', (x, y))
    meshArray = funtion(x, y)
    for i in range(x):
        for j in range(y):
            if int(meshArray[i, j] > 0):
                meshArray[i, j] = 0
            else:
                meshArray[i, j] = 1
            c.putpixel([i, j], meshArray[i, j])
    c.save("%s.bmp" % name)


def funLine(x, y):
    gridWidth = int(x / 50)
    meshAarry = zeros((x, y))
    width = 0
    Black = True
    for i in range(x):
        if Black:
            meshAarry[i][:] = 255
            if width == gridWidth:
                width = 0
                Black = not Black
        elif width == gridWidth:
            width = 0
            Black = not Black
        width += 1
    return meshAarry


def funCicle(x, y):
    cicleR = int(x / 4)
    meshArray = zeros((x, y))
    for i in range(x):
        for j in range(y):
            if ((i - int(x / 2)) ** 2 + (j - int(y / 2)) ** 2) < cicleR ** 2:
                meshArray[i][j] = 255
    return meshArray


def funRandom(x, y):
    meshArray = zeros((x, y))
    for i in range(x):
        for j in range(y):
            meshArray[i, j] = random.randint(0, 255)
    return meshArray


def ImageTest():
    #bmpImageCreateRGB(912, 1140, 'Random', funRandom)
    bmpImageCreateWB(912,1140,'WBCicle',funCicle)
    bmpImageCreateWB(912,1140,'WBLine',funLine)
