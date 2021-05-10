import random
import plotly.figure_factory as ff
import statistics as st

randomNumber = []
countList = []

for i in range(0, 1000):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    total = num1 + num2

    randomNumber.append(total)
    countList.append(i)

mean = st.mean(randomNumber)
median = st.median(randomNumber)
mode = st.mode(randomNumber)

standedDiviasion = st.stdev(randomNumber)

print('Mean: ', mean, '\nMedian: ', median, '\nMode:',
      mode, '\nStanderd Diviasion', standedDiviasion)

graph = ff.create_distplot([randomNumber], ["Result"], show_hist=False)

# graph.show()


def multipleSd():
    sd1_Start, sd1_End = mean - standedDiviasion, mean + standedDiviasion

    sd2_Start, sd2_End = mean - \
        (2 * standedDiviasion), mean + (2 * standedDiviasion)
    sd3_Start, sd3_End = mean - \
        (3 * standedDiviasion), mean + (3 * standedDiviasion)

    counterSD1 = 0
    counterSD2 = 0
    counterSD3 = 0

    for i in range(0, len(randomNumber)):
        value = randomNumber[i]

        if value >= sd1_Start and value <= sd1_End:
            counterSD1 += 1

        if value >= sd2_Start and value <= sd2_End:
            counterSD2 += 1

        if value >= sd3_Start and value <= sd3_End:
            counterSD3 += 1

    perOfSd1 = (counterSD1*100)/len(randomNumber)
    perOfSd2 = (counterSD2*100)/len(randomNumber)
    perOfSd3 = (counterSD3*100)/len(randomNumber)

    print('Sd1: ',perOfSd1)
    print('Sd2: ',perOfSd2)
    print('Sd3: ',perOfSd3)


multipleSd()
