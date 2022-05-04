from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import os
import sys
sys.path.append(os.getcwd())
from Models.Plots.Cubic import Cubic
from Models.Plots.Parabol import Parabol
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic

class MultiNotes:

    def __formatNumberShowed(self, number: float):
        fraction = Fraction(number)
        if (fraction.numerator > 10000 or fraction.denominator > 10000):
            return float("{:.4f}".format(number))
        return fraction
        pass

    def __init__(self, moreNotes: str = None) -> None:
        if moreNotes is not None and len(moreNotes) > 0:
            self.moreNotes = moreNotes 
            self.lenOfCrossNotes = len(moreNotes.split(";"))
        # print(moreNotes)
        self.colorList = []
        self.showedStringArray = []
        pass

    def rainbow_text(self,x, y, strings, colors, orientation='horizontal', ax: plt.Axes=None, **kwargs):
        """
        Take a list of *strings* and *colors* and place them next to each
        other, with text strings[i] being shown in colors[i].

        Parameters
        ----------
        x, y : float
            Text position in data coordinates.
        strings : list of str
            The strings to draw.
        colors : list of color
            The colors to use.
        orientation : {'horizontal', 'vertical'}
        ax : Axes, optional
            The Axes to draw into. If None, the current axes will be used.
        **kwargs
            All other keyword arguments are passed to plt.text(), so you can
            set the font size, family, etc.
        """
        if orientation == 'vertical':
            kwargs.update(rotation=90, verticalalignment='bottom')
        for s, c in zip(strings, colors):
            countLines = s.count("\n") 
            text = ax.text(x, y, s + " ", color=c, **kwargs)
            y += countLines * 0.065

    def initMultiNotes(self, axesNotes: plt.Axes = None, plotInstances : list = [] )-> str:
        showedStringTotal =""
        self.colorList = []
        ct =0
        # print("what happens??")
        for plot in plotInstances:
            ct += 1
            showedString = ""
            if (isinstance(plot, (Line, Parabol, Cubic, Quartic))):
                showedString += "    " +plot.sample + ":\n"
                for point in plot.specialPoints.items():
                    name = point[0]
                    xVl = self.__formatNumberShowed(point[1][0])
                    yVl = self.__formatNumberShowed(point[1][1])
                    showedString += "        {}: ({}, {}) \n".format(name, xVl,yVl)
            showedStringTotal += showedString + ";"
            self.colorList.append(plot.color)
        showedStringTotal +=  self.moreNotes 
        for i in range(self.lenOfCrossNotes):
            self.colorList.append("#9806F6")
        # print(showedStringTotal)
        axesNotes.axis("off")
        self.showedStringArray = showedStringTotal.split(";")
        self.__addTitleNotes(len(plotInstances))
        self.rainbow_text(x=0, y=0, strings=self.showedStringArray, colors=self.colorList, ax=axesNotes)
        pass

    def __addTitleNotes(self, lenOfPlots : int):
        self.showedStringArray.append( "Cross points:")
        self.colorList.append("#E03A0E")
        self.showedStringArray.insert(lenOfPlots, "Plots special points:")
        self.colorList.insert(lenOfPlots,"#E03A0E")
