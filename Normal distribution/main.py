import random
import plotly_express as pe
import plotly.figure_factory as ff

randomNumber = []
countList = []

for i in range(0, 100):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    total = num1 + num2

    randomNumber.append(total)
    countList.append(i)

graph = ff.create_distplot([randomNumber], ["Result"], show_hist=False)

graph.show()
