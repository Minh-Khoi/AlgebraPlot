from Controller.controller import Controller
from fractions import Fraction
import os
import sys
sys.path.append(os.getcwd())
from indexFuntions import initExpression
from Models.Plots.Cubic import Cubic
from Models.Plots.Line import Line
from Models.Plots.Quartic import Quartic 
from Models.Plots.Parabol import Parabol
from Models.MultiPlots.Painter import Painter

print("You want to draw single plots or multiple plots on a figure??")
print("Type 1: draw single plots on each single figures")
print("Type 2 :draw multiple plots on a single figure")
print("Bạn muốn vẽ từng đồ thị riêng hay vẽ nhiều đồ thị trên một hệ tọa độ??")
print("Nhập 1: vẽ các đồ thị trên từng hệ tọa độ riêng")
print("Nhập 2: vẽ nhiều đồ thị trên một hệ tọa độ duy nhất")
choosen = input("Your require - Câu trả lời của bạn: ")

if choosen == '1':
    print("\nChoose the type of plot you want to draw (Type in english lowercase)")
    print("Chọn loại đồ thị hàm số (hàm số bậc 1: 'line', hàm số bậc 2: 'parabol', hàm số bậc 3: 'cubic', hàm số bặc 4: 'quartic'")
    typeOfPlot = input("Your require - Câu trả lời của bạn: ")

    print("\nType parameter numbers. The parameters must be seperated to each others with comma")
    print("Nhập tham số. Các tham số cách nhau bởi dấu phẩy ','")
    paramsNums = [float(Fraction(i)) for i in input().split(",")]

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

    Controller().initSinglePlot(typeOfPlot=typeOfPlot, paramNums= paramsNums, rangeX=rangeX, rangeY=rangeY, color=color )
else:
    print("How many plots do you want to draw?? (You can ask our painter to draw maximum 03 plot)")
    numOfPlot = input("Your answer: ")
    dataPlots = []
    for i in range(numOfPlot):
        plotInfos = {}
        print("Plot number {}:".format(i+1) )
        plotInfos["type"] = input("    Choose the type of plot")
        
    pass
