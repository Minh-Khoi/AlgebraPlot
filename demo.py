from fractions import Fraction
import math
import sympy
from sympy import Symbol
from sympy.solvers import solve as SOLVE



x = 9/4

x = Symbol("x", real=True)
rawResults = SOLVE(2 * (x**3) -4 * (x**2) -5*x -1, x)
for res in rawResults:
    print(res)
# print(rawResults)