import numpy as np
import math
import matplotlib.pyplot as plt
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from Models.Helpers.PlotNote import PlotNote



class Parabol:
    def __init__(self, paramNums : list[float], selfPlot = True, color=None) -> None:
        self.sample = "y= {}x^2 + {}x + {}".format(paramNums[0], paramNums[1], paramNums[2])
        self.paramNumbers = {"a":paramNums[0], "b":paramNums[1], "c":paramNums[2]}
        self.axes : plt.Axes = None
        self.axesForNote: plt.Axes = None
        self.fig, (self.axes, self.axesForNote) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})
        if selfPlot is False :
            plt.close(self.fig)
        self.specialNumbers = {}
        self.specialPoints = {}
        self.__defineSpecialness()
        self.x_yOfPoints= {"x": [], "y": []}
        self.color = color
        pass
        
    def __defineSpecialness(self)-> dict:
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        delta = b**2 - 4*a*c
        self.specialNumbers["delta"] = (delta)
        self.specialPoints = {"O": (0, 0), "A": (0, c)}
        intersectionWithOX_1 = ((-b - math.sqrt(delta)) / (2*a)) if (delta >=0) else None
        intersectionWithOX_2 = ((-b + math.sqrt(delta)) / (2*a)) if (delta > 0) else None
        if intersectionWithOX_1 is not None:
            self.specialPoints["B1"] = (intersectionWithOX_1, 0) 
        if intersectionWithOX_2 is not None:
            self.specialPoints["B2"] = (intersectionWithOX_2, 0) 
        self.specialPoints["P"] = (-b/(2*a) , - delta/(4*a))
        pass

    def __findMinMaxInList(self, numList: tuple[int]) -> tuple[int]:
        sortedList = sorted(numList)
        # print(sortedList)
        return (sortedList[0], sortedList[-1])

    def specifyRange(self, rangesX=None, rangesY=None) -> dict:
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

    def __applyRecipe(self, arrayOfX: np.ndarray) -> np.ndarray:
        returnArray = []
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        for x in arrayOfX:
            returnArray.append(a*math.pow(x,2) + b *x +c)
        return np.array(returnArray, dtype=float)
        pass

    def __drawOX(self, rangeOfValue: tuple[int]):
        xOfPoints = np.arange(rangeOfValue[0], rangeOfValue[1], 0.01)
        yOfPoints = np.zeros(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='red')
        pass

    def __drawOY(self, rangeOfValue: tuple[int]):
        yOfPoints = np.arange(int(rangeOfValue[0]), int(rangeOfValue[1]), 0.01)
        xOfPoints = np.zeros(len(yOfPoints))
        # print(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='red')
        pass

    def generatePlot(self, rangesX=None, rangesY=None, drawInMultiPlots=False):
        rangeOX = self.specifyRange(rangesX=rangesX)["Ox"]
        rangeOY = self.specifyRange(rangesY=rangesY)["Oy"]
        xOfPoints = np.arange(rangeOX[0], rangeOX[1], 0.01)
        yOfPoints = self.__applyRecipe(xOfPoints)
        if drawInMultiPlots:
            self.x_yOfPoints["x"] = xOfPoints
            self.x_yOfPoints["y"] = yOfPoints
        else:
            self.__drawOX(rangeOfValue=rangeOX)
            self.__drawOY(rangeOfValue=rangeOY)
            self.axes.plot(xOfPoints, yOfPoints, color=self.color)
            self.axes.axis("equal")
            # mark every points
            for point in self.specialPoints.items():
                name = point[0]
                coord = point[1]
                self.axes.text(coord[0], coord[1], name)
            note = PlotNote(axes=self.axesForNote, specialNumbers=self.specialNumbers, specialPoints=self.specialPoints)
            plt.tight_layout()
            plt.show()


# parab = Parabol([-1.4,5,2])
# print(parab.specialPoints)
# parab.generatePlot(rangesY=[-10,10],rangesX=[-3,6])
