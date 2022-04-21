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
        self.axes : plt.Axes = None
        self.noteAxes: plt.Axes = None
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [1, 1]})
        self.listOfColors = [ "black", "green", "blue", "orange", "yellow", "grey", "pink", "purple"]
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
        rangeOXY = self.specifyRange(self.plotsList)
        # print(rangeOXY)
        rangeOX = rangeOXY["rangeOnX"]
        rangeOY = rangeOXY["rangeOnY"]
        self.__drawOX(rangeOfValue=rangeOX)
        self.__drawOY(rangeOfValue=rangeOY)
        for plot in self.plotsList:
            if (isinstance(plot, (Line, Parabol,Cubic, Quartic))):
                plot.generatePlot(drawInMultiPlots=True, rangesX=rangeOX, rangesY=rangeOY)
                xOfPoints = plot.x_yOfPoints["x"]
                yOfPoints = plot.x_yOfPoints["y"]
                if (plot.color is not None):
                    color = plot.color
                    if color in self.listOfColors:
                        indexOfChoosenColor = self.listOfColors.index(color)
                        del self.listOfColors[indexOfChoosenColor]
                else:
                    color = self.__chooseColor()
                    pass
                self.axes.plot(xOfPoints,yOfPoints,color=color)

                # mark the point on plot
                for point in plot.specialPoints.items():
                    name = point[0]
                    coord = point[1]
                    self.axes.text(coord[0], coord[1], name, color=color)
        self.__markCrossPoints()
        self.axes.axis("equal")
        
        plt.tight_layout()
        plt.show()

    def __markCrossPoints(self):
        if len(self.plotsList) == 2:
            listOfCrossPoints = EquationSolver(self.plotsList[0], self.plotsList[1]).solve()
            for point in listOfCrossPoints.items:
                name = point[0]
                coord = point[1]
                self.axes.text(coord[0], coord[1], name , color="#036954")
        elif len(self.plotsList) == 3:
            i= 0
            j = 1
            while 1 + i < len(self.plotsList):
                # print("loop at i={}, j={}".format(i,j) )
                if i+j == len(self.plotsList):
                    i += 1
                    j = 1
                else :
                    listOfCrossPoints = EquationSolver(self.plotsList[i], self.plotsList[i+j]).solve()
                    # print(self.plotsList[i].sample)
                    # print(self.plotsList[i+j].sample)
                    # print("---------")
                    for point in listOfCrossPoints.items():
                        # print(point)
                        name = point[0]
                        coord = point[1]
                        self.axes.text(coord[0], coord[1], name, color="#036954")
                    j+=1
            MultiNotes().initMultiNotes(self.noteAxes, plotInstances=self.plotsList)
        pass

cubic = Cubic(paramNums=[4, 2, 1, -1], selfPlot=False,  color="green")
quartic = Quartic(paramNums=[-4, 1, 2, 0,-1], selfPlot=False, color="black")
line = Line(paramNums=[1,-2], selfPlot=False, color="blue")
listOfPlot = [cubic,quartic, line]
# for plot in listOfPlot:
#     print(plot.sample)
#     print(plot.specialPoints)

painter = Painter(plotsList=listOfPlot)
painter.drawPlots()
