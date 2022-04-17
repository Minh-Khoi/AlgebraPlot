from fractions import Fraction
import matplotlib.pyplot as plt
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

    def __init__(self) -> None:
        pass

    def initMultiNotes(self, axesNotes: plt.Axes = None, plotInstances : list = [] )-> str:
        showedString =''
        for plot in plotInstances:
            if (isinstance(plot, (Line,Parabol,Cubic, Quartic))):
                showedString += plot.sample + ":\n"
                for point in plot.specialPoints.items():
                    showedString += "    {}: ({}, {}) \n".format(point[0], point[1][0], point[1][0])
        axesNotes.axis("off")
        axesNotes.text(0, 0, showedString)
        pass
