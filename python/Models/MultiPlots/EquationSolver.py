import numpy as np
import math
import random
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from Models.Plots.Cubic import Cubic
from Models.Plots.Parabol import Parabol
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic
import Models.Helpers.CubicAndQuarticSolver as SOLVER

class EquationSolver:
    def __init__(self, plot_1, plot_2) -> None:
        if (isinstance(plot_1, (Cubic,Line,Parabol,Quartic)) and isinstance(plot_2, (Cubic,Line,Parabol,Quartic))):
            self.priorPlot = plot_1 if (len(plot_1.paramNumbers) > len(plot_2.paramNumbers)) else plot_2
            self.minorPlot = plot_2 if (len(plot_1.paramNumbers) > len(plot_2.paramNumbers)) else plot_1
            self.pseudoPlot = self.__createPseudoPlot( priorPlot= self.priorPlot,minorPlot=self.minorPlot)
            # print(self.pseudoPlot.paramNumbers)
            # print(self.pseudoPlot.sample)
        pass

    def __refomatListKeys(self, keysList : dict) -> list[str]:
        alphabetKeys = ["a", "b", "c", "d", "e"]
        motionIndex = len(self.priorPlot.paramNumbers) - len(self.minorPlot.paramNumbers)
        reformattedList = {}
        # print(motionIndex)
        for (key, number) in keysList.items():
            if (key in alphabetKeys):
                newKey = alphabetKeys[alphabetKeys.index(key) + motionIndex]
                reformattedList[newKey] = number
        # print(reformattedList)
        return reformattedList

    def __createPseudoPlot(self, priorPlot, minorPlot):
        if (isinstance(priorPlot, (Cubic, Line, Parabol, Quartic)) and isinstance(minorPlot, (Cubic, Line, Parabol, Quartic))):
            # print(priorPlot.sample)
            # print(minorPlot.sample)
            paramNumsOfPseudoPlot = []
            for (key, items) in priorPlot.paramNumbers.items():
                minorPlotParamsRefomatted = self.__refomatListKeys(self.minorPlot.paramNumbers)
                # print(minorPlotParamsRefomatted)
                if key in minorPlotParamsRefomatted:
                    paramNumsOfPseudoPlot.append(priorPlot.paramNumbers[key] - minorPlotParamsRefomatted[key])
                else:
                    paramNumsOfPseudoPlot.append(priorPlot.paramNumbers[key] )
                # print(key)
            # print(paramNumsOfPseudoPlot)
            if len(paramNumsOfPseudoPlot) == 2:
                returnedPlot = Line(paramNumsOfPseudoPlot, selfPlot=False)
            if len(paramNumsOfPseudoPlot) == 3:
                returnedPlot = Parabol(paramNumsOfPseudoPlot, selfPlot=False)
            if len(paramNumsOfPseudoPlot) == 4:
                returnedPlot = Cubic(paramNumsOfPseudoPlot, selfPlot=False)
            if len(paramNumsOfPseudoPlot) == 5:
                returnedPlot = Quartic(paramNumsOfPseudoPlot, selfPlot=False)
            return returnedPlot
        pass

    def solve(self):
        if isinstance(self.pseudoPlot, (Cubic, Line, Parabol, Quartic)):
            pseudoSpecialPoints = {}
            countS= 0
            for points in self.pseudoPlot.specialPoints.items():
                name = points[0]
                coord = points[1]
                if ("B" in name):
                    countS += 1
                    x = coord[0]
                    y = self.minorPlot.applyRecipe([coord[0]])[0]
                    pseudoSpecialPoints["S" + str(countS)] = (x,y) 
            return pseudoSpecialPoints
        pass


# cubic = Cubic(paramNums=[4, 2, 1, -1], selfPlot=False,  color="yellow")
# quartic = Quartic(paramNums=[-4, 1, 2, 0, -1], selfPlot=False, color="black")
# print(cubic.paramNumbers)
# print(quartic.paramNumbers)
# eqSolver = EquationSolver(cubic, quartic)
# print(eqSolver.solve())
