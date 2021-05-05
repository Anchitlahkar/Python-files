import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("SOCR-HeightWeight.csv")

heightList = df["Height(Inches)"].tolist()

print(heightList)

graph = ff.create_distplot([heightList], ["Height"], show_hist=False)

graph.show()
