import numpy as np
import matplotlib.pyplot as plt
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
from Models.MultiPlots.MultiNotes import MultiNotes
from Models.MultiPlots.EquationSolver import EquationSolver 

class Painter:
    def __init__(self, plotsList: list) -> None:
        if len(plotsList) > 3 or len(plotsList) ==1:
            print("Number of plots must be 2 or 3")
            return
        self.plotsList = plotsList
        self.listOfCrossPoints = []
        self.axes : plt.Axes = None
        self.noteAxes: plt.Axes = None
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, figsize=(15,6), gridspec_kw={'width_ratios': [1, 1]})
        self.listOfColors = [ "black", "green", "blue", "orange", "yellow", "grey", "pink", "purple"]
        pass

    def __formatNumberShowed(self, number: float):
        fraction = Fraction(number)
        if (fraction.numerator > 10000 or fraction.denominator > 10000):
            return float("{:.4f}".format(number))
        return fraction
        pass

    def __chooseColor(self):
        numColor = random.randint(0, len(self.listOfColors) - 1)
        color = self.listOfColors[numColor]
        del self.listOfColors[numColor]
        return color
        
    def __findMinMaxInList(self, numList: tuple[int]) -> tuple[int]:
        sortedList = sorted(numList)
        # print(numList)
        return (sortedList[0], sortedList[-1])

    def __drawOX(self, rangeOfValue: list[float]):
        xOfPoints = np.arange(rangeOfValue[0], rangeOfValue[1], 0.01)
        yOfPoints = np.zeros(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='#F60673')
        pass

    def __drawOY(self, rangeOfValue: list[float]):
        yOfPoints = np.arange(int(rangeOfValue[0]), int(rangeOfValue[1]), 0.01)
        xOfPoints = np.zeros(len(yOfPoints))
        # print(len(xOfPoints))
        self.axes.plot(xOfPoints, yOfPoints, color='#F60673')
        pass

    

    def specifyRange(self, plotsList: list,rangeX = None, rangeY=None) -> dict:
        rangeOnX = [-0.1,0.1]
        rangeOnY = [-1,1 ]
        if (rangeX is not None and  rangeY is not None):
            return {"rangeOnX": rangeX, "rangeOnY": rangeY}

        for plot in plotsList:
            if (isinstance(plot, (Line, Parabol, Cubic, Quartic))):
                rangeOXY = plot.specifyRange(rangesX=rangeX,rangesY=rangeY)
                if (rangeOXY["Ox"][0] < rangeOnX[0]):
                    rangeOnX[0] = rangeOXY["Ox"][0]
                if (rangeOXY["Ox"][1] > rangeOnX[1]):
                    rangeOnX[1] = rangeOXY["Ox"][1]
                if (rangeOXY["Oy"][0] < rangeOnY[0]):
                    rangeOnY[0] = rangeOXY["Oy"][0]
                if (rangeOXY["Oy"][1] > rangeOnY[1]):
                    rangeOnY[1] = rangeOXY["Oy"][1]
        return {"rangeOnX": rangeOnX, "rangeOnY": rangeOnY}


    def drawPlots(self, rangeX = None, rangeY=None):
        rangeOXY = self.specifyRange(self.plotsList, rangeX=rangeX, rangeY= rangeY)
        # print(rangeOXY)
        rangeOX = rangeOXY["rangeOnX"]
        rangeOY = rangeOXY["rangeOnY"]
        self.__drawOX(rangeOfValue=rangeOX)
        self.__drawOY(rangeOfValue=rangeOY)
        for plot in self.plotsList:
            if (isinstance(plot, (Line, Parabol, Cubic, Quartic))):
                self.__markCrossPoints()
                color = plot.color
                
                # mark the point on plot
                for point in plot.specialPoints.items():
                    name = point[0]
                    coord = point[1]
                    self.axes.text(coord[0], coord[1], name, color=color)
                    
                # mark the cross points and adjust the range of figure concurrently
                for crossPoint in self.listOfCrossPoints.items():
                    name = crossPoint[0]
                    coord = crossPoint[1]
                    self.axes.text(coord[0], coord[1], name, color="#9806F6")
                    if (coord[0] > rangeOX[1]):
                        rangeOX[1] = coord[0]
                    if (coord[0] < rangeOX[0]):
                        rangeOX[0] = coord[0]
                    if (coord[1] < rangeOY[0]):
                        rangeOY[0] = coord[1]
                    if (coord[1] > rangeOY[1]):
                        rangeOY[1] = coord[1]

                plot.generatePlot(drawInMultiPlots=True, rangesX=rangeOX, rangesY=rangeOY)
                xOfPoints = plot.x_yOfPoints["x"]
                yOfPoints = plot.x_yOfPoints["y"]
                self.axes.plot(xOfPoints,yOfPoints,color=color)

        self.axes.axis("equal")
        
        plt.tight_layout()
        plt.show()

    def __markCrossPoints(self):
        crossNote = ""
        if len(self.plotsList) == 2:
            self.listOfCrossPoints = EquationSolver(self.plotsList[0], self.plotsList[1]).solve()
            crossNote += "    '{}' cross with '{}': \n".format(self.plotsList[0].sample, self.plotsList[1].sample)
            # print(crossNote)
            for point in self.listOfCrossPoints.items():
                name = point[0]
                x = self.__formatNumberShowed(point[1][0])
                y = self.__formatNumberShowed(point[1][1])
                crossNote += "        {} : ({}, {}) \n".format(name, x, y)
        elif len(self.plotsList) == 3:
            i= 0
            j = 1
            while 1 + i < len(self.plotsList):
                if i+j == len(self.plotsList):
                    i += 1
                    j = 1
                else :
                    crossNote += "    '{}' cross with '{}': \n".format(self.plotsList[i].sample, self.plotsList[i+j].sample)
                    self.listOfCrossPoints = EquationSolver(self.plotsList[i], self.plotsList[i+j]).solve()
                    for point in self.listOfCrossPoints.items():
                        name = point[0]
                        coord = point[1]
                        x = self.__formatNumberShowed(point[1][0])
                        y = self.__formatNumberShowed(point[1][1])
                        crossNote += "        {} : ({}, {}) \n".format(name, x, y)
                    j+=1
                    crossNote +=";"
        MultiNotes(moreNotes=crossNote).initMultiNotes(self.noteAxes, plotInstances=self.plotsList)
        pass

# cubic = Cubic(paramNums=[4, 2, 1, -1], selfPlot=False,  color="green")
# quartic = Quartic(paramNums=[-4, 1, 2, 0,-1], selfPlot=False, color="black")
# line = Line(paramNums=[1,-2], selfPlot=False, color="blue")
# listOfPlot = [cubic,quartic, line]
# # for plot in listOfPlot:
# #     print(plot.sample)
# #     print(plot.specialPoints)

# painter = Painter(plotsList=listOfPlot)
# painter.drawPlots()
