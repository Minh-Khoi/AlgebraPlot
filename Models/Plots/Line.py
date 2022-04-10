import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction
import random
import os
import sys
sys.path.append(os.getcwd())
from Models.Helpers.PlotNote import PlotNote

class Line:

    def __init__(self, paramNums: list[int], selfPlot = True) -> None:
        self.sample = "y = {a}x + {b}".format(a=paramNums[0], b=paramNums[1])
        self.paramNumbers = {"a" : paramNums[0] , "b" : paramNums[1]}
        self.axes : plt.Axes
        self.noteAxes : plt.Axes
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={"width_ratios": (3, 1)})
        if (selfPlot is False):
            plt.close(self.fig)
        self.specialNumbers = {}
        self.specialPoints = ({"O": (0,0)}) 
        if (paramNums[0] != 0 and paramNums[1] !=0)  :
            self.specialPoints["A"] = (0, paramNums[1])
            self.specialPoints["B"] = (-paramNums[1] / paramNums[0], 0)
        pass
    
    def __drawOX(self, rangeOfValue : tuple[int]):
        xOfPoints = np.arange(rangeOfValue[0], rangeOfValue[1], 0.01)
        yOfPoints = np.zeros(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='red')
        pass

    def __drawOY(self, rangeOfValue: tuple[int]):
        yOfPoints = np.arange(int(rangeOfValue[0]), int(rangeOfValue[1]) , 0.01)
        xOfPoints = np.zeros(len(yOfPoints))
        # print(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='red')
        pass

    def __findMinMaxInList(self, numList : tuple[int]) -> tuple[int]:
        sortedList = sorted(numList)
        # print(sortedList)
        return (sortedList[0], sortedList[-1])

    def __specifyRange(self, rangesX = None, rangesY = None) -> dict:
        arrayYOfPoints = []
        arrayXOfPoints = []
        for point in self.specialPoints.values():
            # print(point)
            arrayXOfPoints.append(point[0])
            arrayYOfPoints.append(point[1])
        minMax_X = self.__findMinMaxInList(arrayXOfPoints)
        lengthOnX = minMax_X[1] - minMax_X[0]
        minMax_Y = self.__findMinMaxInList(arrayYOfPoints)
        lengthOnY = minMax_Y[1] - minMax_Y[0]
        lengthOnRange = lengthOnY if (lengthOnX < lengthOnY) else lengthOnX
        rangeOX = (minMax_X[0] - lengthOnRange, minMax_X[1] + lengthOnRange)
        rangeOY = (minMax_Y[0]-lengthOnRange, minMax_Y[1] + lengthOnRange)
        returnedList = {"Ox": rangeOX, "Oy": rangeOY}
        if (rangesX is not None):
            returnedList["Ox"] = rangesX
        if (rangesY is not None):
            returnedList["Oy"] = rangesY
        return returnedList

    def drawPlot(self, rangesX = None, rangesY = None, activeAxes : plt.Axes  = None, activeNote: plt.Axes=None):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        rangeOX = self.__specifyRange(rangesX=rangesX)["Ox"]
        rangeOY = self.__specifyRange(rangesY=rangesY)["Oy"]

        xOfPoints = np.arange(rangeOX[0], rangeOX[1], 0.01)
        yOfPoints = a*xOfPoints + b
        self.__drawOX(rangeOX)
        self.__drawOY(rangeOY)

        self.axes.text(0, 0, "O")
        self.axes.text(0, b,  "A")
        self.axes.text(- b/a ,0, "B")
        if (activeAxes is None):
            self.axes.plot(xOfPoints, yOfPoints)
            self.axes.axis("equal")
        else:
            activeAxes.plot(xOfPoints, yOfPoints)
            activeAxes.axis("equal")
        if (activeNote is None):
            note = PlotNote(axes=self.noteAxes ,specialNumbers=self.specialNumbers, specialPoints=self.specialPoints)

        plt.tight_layout()
        plt.show()
        pass


# line = Line([1/2, -3])
# line.drawPlot(rangesX=[-4, 10])
