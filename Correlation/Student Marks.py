import pandas as pd
import plotly_express as px
import csv
import numpy as np


data = csv.reader(open(
    "Correlation-data-files\Student Marks vs Days Present.csv"))

listData = list(data)
listData.pop(0)

marksList = []
daysList = []

for i in listData:
    marks = float(i[1])
    day = float(i[2])

    marksList.append(marks)
    daysList.append(day)

# print(marksList)
# print(daysList)


dataSource = {'x': marksList, 'y': daysList}

correlation = np.corrcoef(dataSource['x'], dataSource['y'])
print(correlation[0, 1])


df = pd.read_csv(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\Student Marks vs Days Present.csv"))

graph = px.scatter(df, x='Marks In Percentage', y='Days Present')

graph.show()