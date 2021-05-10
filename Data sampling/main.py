import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random

df = pd.read_csv("data.csv")

data = df["temp"].tolist()

mean = st.mean(data)
Std = st.stdev(data)

print(' Mean: ', mean, '\n', 'Std: ', Std)

meanData = []

for a in range(0, 1000):
    spData = []

    for i in range(0, 500):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]

        spData.append(value)

    spDataMean = st.mean(spData)
    meanData.append(spDataMean)           


meanOfMeanData = st.mean(meanData)
stdOfMeanData = st.stdev(meanData)     # standered error of the mean/ sampling error

print("\n Mean: ", meanOfMeanData)
print("\n STD : ", stdOfMeanData)

# graph = ff.create_distplot([meanData], ["Temp"], show_hist=False)
# graph.show()