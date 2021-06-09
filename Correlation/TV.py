import pandas as pd
import plotly_express as px
import csv
import numpy as np

data = csv.reader(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\Size of TV,_Average time spent watching TV in a week (hours).csv"))

listData = list(data)
listData.pop(0)

TvList = []
timeList = []

for i in listData:
    tv = float(i[0])
    time = float(i[1])

    TvList.append(tv)
    timeList.append(time)

# print(TvList)
# print(timeList)


dataSource = {'x': TvList, 'y': timeList}

correlation = np.corrcoef(dataSource['x'], dataSource['y'])
print(correlation[0, 1])


df = pd.read_csv(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\Size of TV,_Average time spent watching TV in a week (hours).csv"))

graph = px.scatter(df, x='Size of TV', y='\tAverage time spent watching TV in a week')

graph.show()