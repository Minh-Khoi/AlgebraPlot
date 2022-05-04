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

    def __init__(self, paramNums: list[float], selfPlot = True, color = None) -> None:
        self.sample = "y = {a}x + {b}".format(a=paramNums[0], b=paramNums[1])
        self.paramNumbers = {"a" : paramNums[0] , "b" : paramNums[1]}
        self.axes : plt.Axes
        self.noteAxes : plt.Axes
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={"width_ratios": (3, 1)})
        if (selfPlot is False):
            plt.close(self.fig)
        self.specialNumbers = {}
        self.specialPoints = {"O": (0,0)}
        self.x_yOfPoints = {"x": [], "y": []}
        if (paramNums[0] != 0 and paramNums[1] !=0)  :
            self.specialPoints["A"] = (0, paramNums[1])
            self.specialPoints["B"] = (-paramNums[1] / paramNums[0], 0)
        self.color = color
        pass
    
    def __drawOX(self, rangeOfValue : tuple[int]):
        xOfPoints = np.arange(rangeOfValue[0], rangeOfValue[1], 0.01)
        yOfPoints = np.zeros(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='#F60673')
        pass

    def __drawOY(self, rangeOfValue: tuple[int]):
        yOfPoints = np.arange(int(rangeOfValue[0]), int(rangeOfValue[1]) , 0.01)
        xOfPoints = np.zeros(len(yOfPoints))
        # print(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='#F60673')
        pass

    def __findMinMaxInList(self, numList : tuple[int]) -> tuple[int]:
        sortedList = sorted(numList)
        # print(sortedList)
        return (sortedList[0], sortedList[-1])

    
    def applyRecipe(self, arrayOfX: np.ndarray) -> np.ndarray:
        returnArray = []
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        for x in arrayOfX:
            returnArray.append(a * x + b)
        return np.array(returnArray, dtype=float)
        pass

    def specifyRange(self, rangesX = None, rangesY = None) -> dict:
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

    def generatePlot(self, rangesX=None, rangesY=None, drawInMultiPlots=False):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        rangeOX = self.specifyRange(rangesX=rangesX)["Ox"]
        rangeOY = self.specifyRange(rangesY=rangesY)["Oy"]

        xOfPoints = np.arange(rangeOX[0], rangeOX[1], 0.01)
        yOfPoints = a*xOfPoints + b
        if drawInMultiPlots:
            self.x_yOfPoints["x"] = xOfPoints
            self.x_yOfPoints["y"] = yOfPoints
        else:
            self.__drawOX(rangeOX)
            self.__drawOY(rangeOY)
            
            self.axes.text(0, 0, "O")
            self.axes.text(0, b,  "A")
            self.axes.text(- b/a ,0, "B")
            self.axes.plot(xOfPoints, yOfPoints, color=self.color)
            self.axes.axis("equal")
        
            note = PlotNote(axes=self.noteAxes ,specialNumbers=self.specialNumbers, specialPoints=self.specialPoints)

            plt.tight_layout()
            plt.show()
        pass


# line = Line([1/2, -3])
# line.generatePlot(rangesX=[-4, 10], color="orange")
