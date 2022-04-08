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


class Quartic:
    def __init__(self, paramNums: list[float]) -> None:
        self.paramNumbers = {"a": paramNums[0] , "b": paramNums[1], "c": paramNums[2], "d": paramNums[3], "e": paramNums[4]}
        self.sample = "y= {} * x^4 + {} * x^3 + {} * x^2 + {} * x + {}".format(paramNums[0], paramNums[1], 
                                                                                            paramNums[2], paramNums[3], paramNums[4])
        self.axes : plt.Axes = None
        self.axesForNote: plt.Axes = None
        self.fig, (self.axes, self.axesForNote) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})
        self.specialNumbers = {}
        self.specialPoints = {}
        self.__defineSpecialness()
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
        # self.__findExtremePoints()
        # self.__findInflectionPoint()
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
            if (Solver.is_zero(listOfX[1].imag)):
                x = listOfX[i].real
                countIntersections += 1
                self.specialPoints["B" + str(countIntersections)] = (x, a* (x**3) + b*(x**2)+c*x+d)
        if countIntersections == 1 :
            self.specialPoints["B"] = self.specialPoints["B1"]
            del self.specialPoints["B1"]


# quart = Quartic([-1,-3,6,4,-1])
# print(quart.specialPoints)
