import pandas as pd
import csv
import plotly.graph_objects as go

data = pd.read_csv('data.csv')

dataGroup = data.groupby('level')['attempt'].mean()
print(dataGroup)

graph = go.Figure(go.Bar(
    x=dataGroup, y=['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation='h'
))

graph.show()