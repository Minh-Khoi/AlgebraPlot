from fractions import Fraction

def initExpression(typeOfPlot: str):
    if typeOfPlot == "line":
        return "a*x +b"
    if typeOfPlot == "parabol":
        return "a * x^2 + b * x + c"
    if typeOfPlot == "cubic":
        return "a * x^3 + b * x^2 + c * x + d"
    if typeOfPlot == "quartic":
        return "a * x^4 + b * x^3 + c * x^2 + d * x + e"


def initPlotInfos(codeTypeOfPlot: str):
    paramNums = []
    if (codeTypeOfPlot == "1"):
        typeOfPlot = "line"
        lenOfParamNums = 2
    elif (codeTypeOfPlot == "2"):
        typeOfPlot = "parabol"
        lenOfParamNums = 3
    elif (codeTypeOfPlot == "3"):
        typeOfPlot = "cubic"
        lenOfParamNums = 4
    elif (codeTypeOfPlot == "4"):
        typeOfPlot = "quartic"
        lenOfParamNums = 5

    print("\nType parameter numbers: {} ".format(initExpression(typeOfPlot)))
    print("Nhập tham số: {} ".format(initExpression(typeOfPlot)))
    arrayOfParamsName = ["a", "b", "c", "d", "e"]
    for i in range(lenOfParamNums):
        paramNums.append(
            Fraction(input("        {} = ".format(arrayOfParamsName[i]))))
    return [paramNums, typeOfPlot]


