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
from Models.Helpers.MultiNotes import MultiNotes

class Painter:
    def __init__(self, plotsList: list) -> None:
        if len(plotsList) > 3:
            print("too many plots. Please choose maximum 3")
            return
        self.plotsList = plotsList
        self.axes : plt.Axes = None
        self.noteAxes: plt.Axes = None
        self.fig, (self.axes, self.noteAxes) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})
        self.listOfColors = [ "black", "green", "blue", "orange", "yellow", "grey", "pink", "purple"]
        pass


    def __chooseColor(self):
        numColor = random.randint(0, len(self.listOfColors) - 1)
        color = self.listOfColors[numColor]
        del self.listOfColors[numColor]
        return color

    def drawPlots(self):
        for plot in self.plotsList:
            if (isinstance(plot, (Line, Parabol,Cubic, Quartic))):
                plot.generatePlot(drawInMultiPlots=True)
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
        self.axes.axis("equal")
        
        plt.tight_layout()
        plt.show()

                
        

cubic = Cubic(paramNums=[4, 2, 1, -1], selfPlot=False, color="pink")
quartic = Quartic(paramNums=[-4, 1, 2, 0,-1], selfPlot=False, color="orange")
line = Line(paramNums=[1,-2], selfPlot=False, color="blue")
listOfPlot = [cubic,quartic, line]

painter = Painter(plotsList=listOfPlot)
painter.drawPlots()
