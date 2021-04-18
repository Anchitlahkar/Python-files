import pandas as pd
import plotly_express as pe


df = pd.read_csv('D:/Apps/Python/Data/csv files/data.csv')
print(df)

'''
graph = pe.line(df, x="Year", y="Per capita income",
                color="Country", title="Per Capita Income")
graph = pe.bar(df, x="Country", y="InternetUsers",
               title="Internet Users in Each Country")
'''

graph = pe.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country",
                   title="Population in Per Capita",size_max=60)

graph.show()
