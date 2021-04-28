import pandas as pd
import plotly_express as px
import csv
import numpy as np


data = csv.reader(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\cups of coffee vs hours of sleep.csv"))

listData = list(data)
listData.pop(0)

total = 0
for i in listData:
    total += int(i[1])

mean = total/(len(listData))


coff = []
sleep = []

for i in listData:
    c = float(i[1])
    s = float(i[2])

    coff.append(c)
    sleep.append(s)

# print(coff)
# print(sleep)


dataSource = {'x': coff, 'y': sleep}

correlation = np.corrcoef(dataSource['x'], dataSource['y'])
print(correlation[0, 1])



'''
df = pd.read_csv(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\cups of coffee vs hours of sleep.csv"))

graph = px.scatter(df, x='Coffee in ml', y='sleep in hours',
                   title="Cups of coffee vs Hours of sleep.")

lenData = len(listData)

graph.update_layout(
    shapes=[dict(type='line', y0=mean, y1=mean, x0=0, x1=lenData)])

graph.show()
'''