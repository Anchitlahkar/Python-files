import csv

dataSheet = open('archive/SOCR-HeightWeight.csv', newline='')
readData = csv.reader(dataSheet)
listdata = list(readData)

listdata.pop(0)
heightData = []

for i in range(len(listdata)):
    num = listdata[i][1]
    heightData.append(float(num))

heightData.sort()
heightDataLen = len(heightData)

if heightDataLen % 2 == 0:
    md1 = heightData[heightDataLen // 2]
    md2 = heightData[heightDataLen // 2 + 1]
    median = (md1+md2)/2
    print(median)

else:
    median = heightData[heightDataLen // 2 + 1]
    print(median)
