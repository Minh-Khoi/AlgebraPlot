import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
import Models.Helpers.CubicAndQuarticSolver as Solver
from Models.Helpers.PlotNote import PlotNote
from Models.Plots.Cubic import Cubic
from Models.Plots.Parabol import Parabol


class Quartic:
    def __init__(self, paramNums: list[float], selfPlot = True, color=None) -> None:
        self.paramNumbers = {"a": paramNums[0] , "b": paramNums[1], "c": paramNums[2], "d": paramNums[3], "e": paramNums[4]}
        self.sample = "y= {} * x^4 + {} * x^3 + {} * x^2 + {} * x + {}".format(paramNums[0], paramNums[1], 
                                                                                            paramNums[2], paramNums[3], paramNums[4])
        self.axes : plt.Axes = None
        self.noteAxes: plt.Axes = None
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})
        if (selfPlot is False): 
            plt.close(self.fig)
        self.specialNumbers = {}
        self.specialPoints = {}
        self.__defineSpecialness()
        self.x_yOfPoints : dict = {"x": [], "y": []}
        self.color = color
        pass

         
    def __defineSpecialness(self)-> dict:
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        e = self.paramNumbers["e"]
        self.specialPoints = {"O": (0, 0), "A": (0, e)}
        # print(self.specialPoints)
        self.__findIntersections()
        self.__findExtremePoints()
        self.__findInflectionPoints()
        pass

    def __findIntersections(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        e = self.paramNumbers["e"]
        listOfX = Solver.Quartic([a,b,c,d,e])
        # print(Solver.is_zero(listOfX[1].imag))
        countIntersections = 0
        for i in range(len(listOfX)):
            if (Solver.is_zero(listOfX[i].imag)):
                x = listOfX[i].real
                # print(x)
                countIntersections += 1
                self.specialPoints["B" + str(countIntersections)] = (x, a* (x**4) + b*(x**3)+c*(x**2)+d * x + e)
        if countIntersections == 1 :
            self.specialPoints["B"] = self.specialPoints["B1"]
            del self.specialPoints["B1"]

    def __findExtremePoints(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        e = self.paramNumbers["e"]
        derivativeFunc = Cubic(paramNums=[4*a , 3*b , 2*c , d], selfPlot=False)
        # plt.close(derivativeFunc.fig)
        # print(derivativeFunc.specialPoints)
        if (("B1" in derivativeFunc.specialPoints or "B" in derivativeFunc.specialPoints) is False):
            return
        countExtremePoint = 0
        for point in derivativeFunc.specialPoints.items():
            # print(point)
            if ("B" in point[0]):
                countExtremePoint +=1
                x = point[1][0]
                y = a* (x**4) + b* (x**3)+ c* (x**2) + d*x +e
                self.specialPoints["P" + str(countExtremePoint)] = (x,y)
        if countExtremePoint == 1:
            self.specialPoints["P"] = self.specialPoints["P1"]
            del self.specialPoints["P1"]
        pass

    def __findInflectionPoints(self):
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        e = self.paramNumbers["e"]
        twoLevelDerivativeFunc = Parabol(paramNums=[4*3*a, 3*2*b, 2*c], selfPlot=False)
        # plt.close(twoLevelDerivativeFunc.fig)
        if ("B2" in twoLevelDerivativeFunc.specialPoints):
            x1 = twoLevelDerivativeFunc.specialPoints["B1"][0]
            y1 = a* (x1**4) + b * (x1**3) + c* (x1**2) + d*x1 +e
            self.specialPoints["I1"]  = (x1,y1)

            x2 = twoLevelDerivativeFunc.specialPoints["B2"][0]
            y2 = a* (x2**4) + b * (x2**3) + c* (x2**2) + d*x2 +e
            self.specialPoints["I2"]  = (x2,y2)


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
        e = self.paramNumbers["e"]
        for x in arrayOfX:
            returnArray.append(a*math.pow(x, 4) + b * (x**3) + c * (x**2) + d*x +e)
        return np.array(returnArray, dtype=float)
        pass

    def generatePlot(self, rangesX=None, rangesY=None, drawInMultiPlots = False):
        rangeOX = self.specifyRange(rangesX)["Ox"] 
        rangeOY = self.specifyRange(rangesY)["Oy"] 
        
        xOfPoints = np.arange(rangeOX[0], rangeOX[1], 0.01)
        yOfPoints = self.applyRecipe(xOfPoints)
        if (drawInMultiPlots):
            self.x_yOfPoints["x"] = xOfPoints
            self.x_yOfPoints["y"] = yOfPoints
        else : 
            self.__drawOX(rangeOfValue=rangeOX)
            self.__drawOY(rangeOfValue=rangeOY)

            self.axes.plot(xOfPoints, yOfPoints, color=self.color)
            self.axes.axis("equal")

            # mark every points
            for point in self.specialPoints.items():
                name = point[0]
                coord = point[1]
                self.axes.text(coord[0], coord[1], name)
            note = PlotNote(axes=self.noteAxes, specialNumbers=self.specialNumbers, specialPoints=self.specialPoints)

            plt.tight_layout()
            plt.show()

    def check(self, coord: tuple[int]) -> bool:
        a = self.paramNumbers["a"]
        b = self.paramNumbers["b"]
        c = self.paramNumbers["c"]
        d = self.paramNumbers["d"]
        e = self.paramNumbers["e"]
        x = coord[0]
        y = coord[1]
        yChecking = a * (x**4) + b*(x**3) + c*(x**2) + d*x + e
        print("a = {}; b={}; c={}; d={}; e = {}".format(a, b, c, d,e))
        print(yChecking)
        return y == yChecking


# quart = Quartic(paramNums=[-1, -1, 3, 3, 0])
# # print(quart.specialPoints)
# quart.generatePlot(rangesX=[-5,5])
