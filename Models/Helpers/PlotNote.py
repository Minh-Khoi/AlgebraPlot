import numpy as np 
import matplotlib.pyplot as plt
from fractions import Fraction

class PlotNote:

    def __formatNumberShowed(self, number: float):
        fraction = Fraction(number)
        if (fraction.numerator > 10000 or fraction.denominator > 10000):
            return float("{:.4f}".format(number))
        return fraction
        pass

    def __init__(self, axes: plt.Axes = None, specialPoints: dict = None, specialNumbers : dict = None, multiNotes = False) -> None:
        showedString = ""
        showedString += "Special points: \n"
        for point in specialPoints.items():
            showedString += "   {}: ({};{}) \n".format(point[0], self.__formatNumberShowed(point[1][0]), 
                                                                                self.__formatNumberShowed(point[1][1]) )

        showedString += "Discriminant: \n"
        for num in specialNumbers.items():
            showedString += "   {}: {} \n".format(num[0], self.__formatNumberShowed(num[1]))
            pass

        if (multiNotes is True):
            return
        axes.axis("off")
        axes.text(0, 0, showedString)
        pass
