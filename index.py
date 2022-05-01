from Controller.controller import Controller
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from indexFuntions import initExpression, initPlotInfos
from Models.Plots.Cubic import Cubic
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic 
from Models.Plots.Parabol import Parabol
from Models.MultiPlots.Painter import Painter

print("How many plots you want to draw in a frame??")
print("Bạn muốn vẽ bao nhiêu đồ thị trong một khung hình.")
numOfPlotsOnFigure = input("Your require - Câu trả lời của bạn: ")

try:
    if numOfPlotsOnFigure not in ["1","2","3"]:
        print("OOPs!! You can only draw maximum 3 plots in a frame")
    elif numOfPlotsOnFigure == '1':
        print("\nChoose the type of plot you want to draw: entry 1 for 'line', 2 for 'parabol', 3 for 'cubic', 4 for 'quartic'")
        print("Chọn loại đồ thị hàm số: nhập '1' đối với hàm số bậc nhất, '2' cho hàm số bậc 2, '3' cho hàm số bậc 3, và '4' cho hàm số bậc 4")
        codeTypeOfPlot = input("Your require - Câu trả lời của bạn: ")

        plotInfos = initPlotInfos(codeTypeOfPlot)
        paramNums = plotInfos[0]
        typeOfPlot = plotInfos[1]

        color = input("\n Choose color - chọn màu đồ thị: ")
        if len(color) == 0:
            color = None

        print("\nDefine the range on horizontal axis: 'start, end'")
        print("Xác định phạm vi đồ thị trên trục hoành: 'tọa độ đầu', 'tọa độ cuối")
        rangeXraw = input().split(",")
        if len(rangeXraw) <= 1:
            rangeX = None
        else:
            rangeX = [float(Fraction(i)) for i in rangeXraw]

        print("\nDefine the range on vertical axis: 'start, end'")
        print("Xác định phạm vi đồ thị trên trục tung: 'tọa độ đầu', 'tọa độ cuối'")
        rangeYraw = input().split(",")
        if len(rangeYraw) <= 1:
            rangeY = None
        else:
            rangeY = [float(Fraction(i)) for i in rangeYraw]

        Controller().initSinglePlot(typeOfPlot=typeOfPlot, paramNums= paramNums, rangeX=rangeX, rangeY=rangeY, color=color )
    else:
        dataPlots = []
        for i in range(int(numOfPlotsOnFigure)):
            plotDatas = {}
            print("Plot number {}:".format(i+1) )
            codeOfPlotType= \
                input("    Choose the type of plot. entry 1 for 'line', 2 for 'parabol', 3 for 'cubic', 4 for 'quartic'\n" +
                    "    Chọn loại đồ thị hàm số: nhập '1' đối với hàm số bậc nhất, '2' cho hàm số bậc 2, '3' cho hàm số bậc 3," +
                    " và '4' cho hàm số bậc 4\n\t")
            
            plotInfos = initPlotInfos(codeTypeOfPlot=codeOfPlotType)
            paramNums = plotInfos[0]
            typeOfPlot = plotInfos[1]

            color = input("\n    Choose color - chọn màu đồ thị: ")
            if len(color) == 0:
                color = None
            plotDatas["type"] = typeOfPlot
            plotDatas["paramNums"] = paramNums
            plotDatas["color"] = color
            dataPlots.append(plotDatas)

        print("\nDefine the range on horizontal axis: 'start, end'")
        print("Xác định phạm vi đồ thị trên trục hoành: 'tọa độ đầu', 'tọa độ cuối")
        rangeXraw = input().split(",")
        if len(rangeXraw) <= 1:
            rangeX = None
        else:
            rangeX = [float(Fraction(i)) for i in rangeXraw]

        print("\nDefine the range on vertical axis: 'start, end'")
        print("Xác định phạm vi đồ thị trên trục tung: 'tọa độ đầu', 'tọa độ cuối'")
        rangeYraw = input().split(",")
        if len(rangeYraw) <= 1:
            rangeY = None
        else:
            rangeY = [float(Fraction(i)) for i in rangeYraw]
        
        Controller().initMultiPlots(dataPlots=dataPlots,rangeX=rangeX, rangeY= rangeY)

        pass
except Exception as e:
    print("You have entried unsuitable values")
    print(str(e))