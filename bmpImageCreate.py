__author__ = 'levitan'

from PIL import Image
import numpy as np
from numpy import *


def bmpImageCreateRGB(x, y, name, function):
    c = Image.new("RGB", (x, y))
    meshArray = function(x, y)
    for i in range(0, x):
        for j in range(0, y):
            c.putpixel([i, j], (int(meshArray[i][j]), int(meshArray[i][j]), int(meshArray[i][j])))
    # c.show()
    c.save("%s.bmp" % name)


def bmpImageCreateWB8Bit(x, y, name, function):
    c = Image.new("L", (x, y))
    meshArray = function(x, y)
    for i in range(0, x):
        for j in range(0, y):
            c.putpixel([i, j], int(meshArray[i][j]))
    # c.show()
    c.save("%s.bmp" % name)


def bmpImageCreateWB1Bit(x, y, name, funtion):
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
    meshArray = zeros((x, y))
    width = 0
    Black = True
    for i in range(x):
        if Black:
            meshArray[i][:] = 255
            if width == gridWidth:
                width = 0
                Black = not Black
        elif width == gridWidth:
            width = 0
            Black = not Black
        width += 1
    return meshArray


def funSinLine(x, y):
    gridWidth = int(x / 20)
    meshArray = zeros((x, y))
    for i in range(x):
        meshArray[i, :] = abs(sin(pi * i / gridWidth) ** 2 * 255)
    return meshArray


def funLaguerre(x, y):
    meshArray = zeros((x, y))
    c = [1, 1, 1, 1, 1]
    max = abs(np.polynomial.laguerre.lagval2d(x, y, c))
    for i in range(x):
        for j in range(y):
            meshArray[i, j] = abs(np.polynomial.laguerre.lagval2d(i, j, c)) * 255 / max
            # print meshArray[i,j]
            if meshArray[i, j] > 255:
                meshArray[i, j] = 255
    return meshArray


def funCicle(x, y):
    if x < y:
        cicleR = int(x / 4)
    else:
        cicleR = int(y / 4)
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
    # bmpImageCreateRGB(912, 1140, 'Laguerre', funLaguerre)
    bmpImageCreateWB8Bit(912, 1140, 'WB8BitSinLine', funSinLine)
    # bmpImageCreateWB1Bit(912, 1140, 'WBLine', funLine)
