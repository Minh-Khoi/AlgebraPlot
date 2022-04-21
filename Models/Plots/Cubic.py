import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
import Models.Helpers.CubicAndQuarticSolver as Solver
from Models.Helpers.PlotNote import PlotNote
from Models.Plots.Parabol import Parabol


class Cubic:
    
    def __init__(self, paramNums: list[float], selfPlot = True, color = "blue") -> None:
        self.sample = "y = {}x^3 + {}x^2 + {}x+ {}".format(paramNums[0], paramNums[1], paramNums[2], paramNums[3])
        self.paramNumbers = {"a": paramNums[0], "b": paramNums[1], "c": paramNums[2], "d": paramNums[3]}
        self.axes : plt.Axes
        self.noteAxes : plt.Axes
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})
        if (selfPlot is False):
            plt.close(self.fig)
        self.specialNumbers = {}
        self.specialPoints = {}
        self.__defineSpecialness()
        self.x_yOfPoints: dict = {"x": [], "y": []}
        self.color = color
        pass
        
    def __defineSpecialness(self)-> dict:
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        self.specialPoints = {"O": (0, 0), "A": (0, d)}
        # delta = b**2 - 3*a*c
        # k = (9*a*b*c - 2*(b**3) - (27 * (a**2)*d))/ ((abs(delta) ** (3/2))*2)
        # self.specialNumbers["delta"] = delta
        # self.specialNumbers["k"] = k
        self.__findIntersections()
        self.__findExtremePoints()
        self.__findInflectionPoint()
        pass

    def __findIntersections(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        listOfX = Solver.Cubic([a,b,c,d])
        # print(listOfX)
        countIntersections = 0
        for i in range(len(listOfX)):
            if (Solver.is_zero(listOfX[i].imag)):
                x = listOfX[i].real
                # print(x)
                countIntersections += 1
                self.specialPoints["B" + str(countIntersections)] = (x, a* (x**3) + b*(x**2)+c*x+d)
        if countIntersections == 1 :
            self.specialPoints["B"] = self.specialPoints["B1"]
            del self.specialPoints["B1"]

        pass


    def __findExtremePoints(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        derivativeFunc = Parabol(paramNums=[3*a, 2*b, c], selfPlot=False)
        # plt.close(derivativeFunc.fig)
        if (("B1" in derivativeFunc.specialPoints) is False):
            return

        x1 = derivativeFunc.specialPoints["B1"][0]
        y1 = a * (x1**3) + b * (x1**2) + c * x1 + d
        self.specialPoints["P1"] = (x1, y1)

        x2 = derivativeFunc.specialPoints["B2"][0]
        y2 = a * (x2**3) + b * (x2**2) + c * x2 + d
        self.specialPoints["P2"] = (x2, y2)
        pass

    def __findInflectionPoint(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        x = - b / (3*a)
        y = a* (x**3) + b * (x**2) + c * x + d
        self.specialPoints["I"] = (x, y)

        
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
        # print(numList)
        return (sortedList[0], sortedList[-1])

    def specifyRange(self, rangesX=None, rangesY=None) -> dict:
        arrayYOfPoints = []
        arrayXOfPoints = []
        for point in self.specialPoints.values():
            # print(point)
            arrayXOfPoints.append(point[0])
            arrayYOfPoints.append(point[1])
        rangeOX = (self.__findMinMaxInList(arrayXOfPoints)[0] -0.1 , self.__findMinMaxInList(arrayXOfPoints)[1] +0.1 )
        rangeOY = (self.__findMinMaxInList(arrayYOfPoints)[0]-1 , self.__findMinMaxInList(arrayYOfPoints)[1] +1)
        returnedList =  {"Ox": rangeOX, "Oy": rangeOY}
        if (rangesX is not None):
            returnedList["Ox"] = rangesX
        if (rangesY is not None):
            returnedList["Oy"] = rangesY
        return returnedList

    def applyRecipe(self, arrayOfX: np.ndarray) -> np.ndarray:
        returnArray = []
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        for x in arrayOfX:
            returnArray.append(a*math.pow(x, 3) + b * (x**2) + c *x + d)
        return np.array(returnArray, dtype=float)
        pass

    def generatePlot(self, rangesX=None, rangesY=None, drawInMultiPlots=False):
        rangeOX = self.specifyRange(rangesX)["Ox"] 
        rangeOY = self.specifyRange(rangesY)["Oy"]

        xOfPoints = np.arange(rangeOX[0], rangeOX[1], 0.01)
        yOfPoints = self.applyRecipe(xOfPoints)
        if (drawInMultiPlots):
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
            note = PlotNote(axes=self.noteAxes ,specialNumbers=self.specialNumbers, specialPoints=self.specialPoints)

            plt.tight_layout()
            plt.show()

    def check(self, coord: tuple[int]) -> bool:
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        x = coord[0]
        y = coord[1]
        yChecking = a * (x**3) + b*(x**2) + c*x + d
        print("a = {}; b={}; c={}; d={}".format(a,b,c,d))
        print(yChecking)
        return y == yChecking
        


# cubic = Cubic([-4,9,1.6*2,4])
# print(cubic.specialPoints)
# cubic.generatePlot(rangesX=(-2,3))
# for point in cubic.specialPoints.items():
#     if (point[0].find("B") !=-1):
#         x = point[1][0]
#         print(point)
#         print(cubic.check(point[1]))
# print(cubic.check((2,0)))
