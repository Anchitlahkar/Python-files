import plotly.figure_factory as ff
import pandas as pd
import statistics as st

df = pd.read_csv("SOCR-HeightWeight.csv")

heightList = df["Height(Inches)"].tolist()

# graph = ff.create_distplot([heightList], ["Height"], show_hist=False)

# graph.show()


def calculate():
    mean = st.mean(heightList)
    std = st.stdev(heightList)

    sd1_Start, sd1_End = mean - std, mean + std
    sd2_Start, sd2_End = mean - (2*std), mean + (2*std)
    sd3_Start, sd3_End = mean - (3*std), mean + (3*std)

    counterStd1 = 0
    counterStd2 = 0
    counterStd3 = 0

    for i in range(0, len(heightList)):
        value = heightList[i]

        if value >= sd1_Start and value <= sd1_End:
            counterStd1 += 1

        if value >= sd2_Start and value <= sd2_End:
            counterStd2 += 1

        if value >= sd3_Start and value <= sd3_End:
            counterStd3 += 1

    perOfSd1 = (counterStd1*100)/len(heightList)
    perOfSd2 = (counterStd2*100)/len(heightList)
    perOfSd3 = (counterStd3*100)/len(heightList)

    print('Sd1 %: ',perOfSd1)
    print('Sd2 %: ',perOfSd2)
    print('Sd3 %: ',perOfSd3)
    
calculate()