import base64
import json
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from Controller.controller import Controller


def convertListOfStringNumber(params: list[str]):
    newList = []
    for pa in params:
        newList.append((Fraction(pa)))
    return newList


dataJSONencoded = sys.argv[2]

# print(dataJSONencoded)
datasJSON = base64.b64decode(dataJSONencoded).decode("utf-8")
# print((datasJSON))
datas = json.loads(datasJSON)
if (len(datas)>1):
    listOfPlots = []
    for plotInfo in datas:
        parametersList = convertListOfStringNumber(plotInfo["parameters"])
        plotInfo["parameters"] = parametersList
        listOfPlots.append(plotInfo)
    Controller().initMultiPlots(listOfPlots)
else:
    plotInfo = datas[0]
    parametersList = convertListOfStringNumber(plotInfo["parameters"])
    Controller().initSinglePlot(plotInfo["type"],parametersList, plotInfo["color"])


