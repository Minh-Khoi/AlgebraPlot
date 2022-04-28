import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from Models.Plots.Cubic import Cubic
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic 
from Models.Plots.Parabol import Parabol
from Models.MultiPlots.Painter import Painter

class Controller:
    def __init__(self) -> None:
        pass

    def initSinglePlot(self, typeOfPlot:str, paramNums:list[float], color = None, rangeX=None, rangeY=None):
        if typeOfPlot == "line" :
            if len(paramNums) != 2:
                error = "There must be and only be 02 - two parameters"
                print(error)
                return
            else:
                line = Line(paramNums=paramNums, color=color)
                line.generatePlot(rangesX=rangeX, rangesY= rangeY)
        elif typeOfPlot == "parabol":
            if len(paramNums) != 3:
                error = "There must be and only be 03 - three parameters"
                print(error)
                return
            else:
                parabol = Parabol(paramNums=paramNums, color=color)
                parabol.generatePlot(rangesX=rangeX, rangesY=rangeY)
        elif typeOfPlot == "cubic":
            if len(paramNums) != 4:
                error = "There must be and only be 04 - four parameters"
                print(error)
                return
            else:
                cubic = Cubic(paramNums=paramNums, color=color)
                cubic.generatePlot(rangesX=rangeX, rangesY=rangeY)
        elif typeOfPlot == "quartic":
            if len(paramNums) != 4:
                error = "There must be and only be 05 - five parameters"
                print(error)
                return
            else:
                quartic = Quartic(paramNums=paramNums, color=color)
                quartic.generatePlot(rangesX=rangeX, rangesY=rangeY)

    def initMultiPlots(self, dataPlots: list[dict], rangeX=None, rangeY=None):
        if len(dataPlots) > 3:
            print("Too many plots. Please choose only 3 or fewer")
        i =0
        plotsList = []
        error = ""
        for plotInfo in dataPlots:
            typeOfPlot = plotInfo["type"]
            paramNums = plotInfo["paramNums"]
            color = plotInfo["color"]
            if typeOfPlot == "line":
                if len(paramNums) != 2:
                    error += "The line plot (number {}) must be and only be 02 - two parameters \n".format(i)
                else:
                    line = Line(paramNums=paramNums, color=color, selfPlot=False)
                    plotsList.append(line)
            if typeOfPlot == "quartic":
                if len(paramNums) != 5:
                    error += "The quartic plot (number {}) must be and only be 05 - five parameters \n".format(i)
                else:
                    quartic = Quartic(paramNums=paramNums, color=color, selfPlot=False)
                    plotsList.append(quartic)
            if typeOfPlot == "parabol":
                if len(paramNums) != 3:
                    error += "The parabol plot (number {}) must be and only be 03 - three parameters \n".format(i)
                else:
                    parabol = Parabol(paramNums=paramNums, color=color,selfPlot= False)
                    plotsList.append(parabol)
            if typeOfPlot == "cubic":
                if len(paramNums) != 4:
                    error += "The cubic plot (number {}) must be and only be 04 - four parameters \n".format(i)
                else:
                    cubic = Cubic(paramNums=paramNums, color=color, selfPlot=False)
                    plotsList.append(cubic)
            i +=1
        if len(error) > 0:
            print(error)
            return
        painter = Painter(plotsList=plotsList)
        painter.drawPlots(rangeX=rangeX, rangeY=rangeY)
        pass
