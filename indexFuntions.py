def initExpression(typeOfPlot: str):
    if typeOfPlot == "line":
        return "a*x +b"
    if typeOfPlot == "Parabol":
        return "a * x^2 + b * x + c"
    if typeOfPlot == "cubic":
        return "a * x^3 + b * x^2 + c * x + d"
    if typeOfPlot == "quartic":
        return "a * x^4 + b * x^3 + c * x^2 + d * x + e"
