import csv
import pandas as pd
import plotly_express as pe
import math


# Mean
dataSheet = csv.reader(open(
    'D:\Apps\Python\standard_deviation\class-csv-files\class1.csv', newline=''))
listData = list(dataSheet)

listData.pop(0)

total = 0
for i in listData:
    total = total + int(i[1])

lenOfListData = len(listData)
mean = (total/lenOfListData)
print("Mean: ", mean)


# Graph

df = pd.read_csv(
    'D:\Apps\Python\standard_deviation\class-csv-files\class1.csv')
graph = pe.scatter(df, x='Student Number', y="Marks",
                   color='Student Number', size="Marks", title=" CLASS 1")

graph.update_layout(shapes=[
    dict(
        type='line',
        x0=0, x1=lenOfListData,
        y0=mean, y1=mean
    )])
# graph.show()


# Standert deviation
newData = []

for i in listData:
    newData.append(i[1])

print(newData)

squareList = []

for i in newData:
    a = int(i) - mean
    a = a ** 2

    squareList.append(a)


totalsq = 0
for i in squareList:
    totalsq = totalsq + i


totalsq = totalsq/lenOfListData
std = math.sqrt(totalsq)

print(std)
input()