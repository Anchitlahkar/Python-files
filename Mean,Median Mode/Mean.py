import csv

dataSheet = open('archive/SOCR-HeightWeight.csv', newline='')
readData = csv.reader(dataSheet)
listdata = list(readData)

listdata.pop(0)
heightData = []

for i in range(len(listdata)):
    num = listdata[i][1]
    heightData.append(float(num))

heightDataLen = len(heightData)

total = 0

for i in heightData:
    total = total + i

mean = total/heightDataLen

print(mean)
