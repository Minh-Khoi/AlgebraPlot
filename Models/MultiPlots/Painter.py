import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from Models.Plots.Cubic import Cubic
from Models.Plots.Parabol import Parabol
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic
from Models.Helpers.PlotNote import PlotNote

class Paiter:
    def __init__(self, plotsList: list, colorsList: list) -> None:
        self.plotsList = plotsList
        self.colorsList = colorsList
        pass
