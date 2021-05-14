import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("CSV Files\studentMarks.csv")
data1 = pd.read_csv("CSV Files\data1.csv")
data2 = pd.read_csv("CSV Files\data2.csv")
data3 = pd.read_csv("CSV Files\data3.csv")


mathsScore = df["Math_score"].tolist()
data1List = data1["Math_score"].tolist()
data2List = data2["Math_score"].tolist()
data3List = data3["Math_score"].tolist()

data1_Mean = st.mean(data1List)
data2_Mean = st.mean(data2List)
data3_Mean = st.mean(data3List)

mean_MathsScore = st.mean(mathsScore)
std_MathsScore = st.stdev(mathsScore)


print("Mean: ", mean_MathsScore)
print("Std: ", std_MathsScore)

mathsMean = []

for i in range(0, 1000):
    spMean = []
    for i in range(0, 100):
        randomIndex = random.randint(0, len(mathsScore)-1)
        value = mathsScore[randomIndex]

        spMean.append(value)

    totalmean = st.mean(spMean)
    mathsMean.append(totalmean)

sp_MathMean = st.mean(mathsMean)
sp_MathStd = st.stdev(mathsMean)

print("MathsMean: ", sp_MathMean)
print("MathsSTD: ", sp_MathStd)


Std1_Start, Std1_End = sp_MathMean - sp_MathStd, sp_MathMean + sp_MathStd

Std2_Start, Std2_End = sp_MathMean - 2 * \
    (sp_MathStd),  sp_MathMean + 2 * (sp_MathStd)

Std3_Start, Std3_End = sp_MathMean - 3 * \
    (sp_MathStd),  sp_MathMean + 3 * (sp_MathStd)


graph = ff.create_distplot([mathsMean], ["Math Mean"], show_hist=False)
graph.add_trace(go.Scatter(x=[st.mean(mathsMean), st.mean(mathsMean)],
                           y=[0, 0.2], mode='lines', name="Mean"))


# sd1 Trace
graph.add_trace(go.Scatter(x=[Std1_Start, Std1_Start],
                           y=[0, 0.2], mode='lines', name="Std1 Start"))
graph.add_trace(go.Scatter(x=[Std1_End, Std1_End],
                           y=[0, 0.2], mode='lines', name="Std1 End"))


# sd2 trace
graph.add_trace(go.Scatter(x=[Std2_Start, Std2_Start],
                           y=[0, 0.2], mode='lines', name="Std2 Start"))
graph.add_trace(go.Scatter(x=[Std2_End, Std2_End],
                           y=[0, 0.2], mode='lines', name="Std2 End"))

# sd 3 trace
graph.add_trace(go.Scatter(x=[Std3_Start, Std3_Start],
                           y=[0, 0.2], mode='lines', name="Std3 Start"))
graph.add_trace(go.Scatter(x=[Std3_End, Std3_End],
                           y=[0, 0.2], mode='lines', name="Std3 End"))


# Data1
graph.add_trace(go.Scatter(x=[data1_Mean, data1_Mean],
                           y=[0, 0.2], mode='lines', name="data1"))

# Data2
graph.add_trace(go.Scatter(x=[data2_Mean, data2_Mean],
                           y=[0, 0.2], mode='lines', name="data2"))

# Data3
graph.add_trace(go.Scatter(x=[data3_Mean, data3_Mean],
                           y=[0, 0.2], mode='lines', name="data3"))


# z_score

z_scoreData1 = (data1_Mean - mean_MathsScore)/st.stdev(data1List)
z_scoreData2 = (data2_Mean - mean_MathsScore)/st.stdev(data2List)
z_scoreData3 = (data3_Mean - mean_MathsScore)/st.stdev(data3List)

print('\nZ_Score Data1: ', z_scoreData1)
print('Z_Score Data2: ', z_scoreData2)
print('Z_Score Data3: ', z_scoreData3)


# graph.show()
