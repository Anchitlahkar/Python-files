import pandas as pd
import plotly_express as px
import csv
import numpy as np


data = csv.reader(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"))

listData = list(data)
listData.pop(0)

total = 0
for i in listData:
    total += int(i[1])

mean = total/(len(listData))

temp = []
ice = []

for i in listData:
    t = float(i[0])
    ic = float(i[1])

    temp.append(t)
    ice.append(ic)

# print(temp)
# print(ice)


dataSource = {'x': temp, 'y': ice}

correlation = np.corrcoef(dataSource['x'], dataSource['y'])
print(correlation[0,1])


'''
df = pd.read_csv(open(
    "D:\Apps\Python\Correlation\Correlation-data-files\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"))

graph = px.scatter(df, x='Temperature', y='Ice-cream Sales')

graph.update_layout(
    shapes=[dict(type='line', y0=mean, y1=mean, x0=0, x1=25)])

# graph.show()
'''
