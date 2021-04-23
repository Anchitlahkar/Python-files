import csv
from collections import Counter

dataSheet = open('archive/SOCR-HeightWeight.csv', newline='')
readData = csv.reader(dataSheet)
listdata = list(readData)

listdata.pop(0)
heightData = []

for i in range(len(listdata)):
    num = listdata[i][1]
    heightData.append(float(num))

countData = Counter(heightData)

modeDataRange = {
    '50-60': 0,
    '60-70': 0,
    '70-80': 0,
}

for height, occurrance in countData.items():

    if 50 < float(height) < 60:
        modeDataRange['50-60'] += occurrance

    elif 60 < float(height) < 70:
        modeDataRange['60-70'] += occurrance

    elif 70 < float(height) < 80:
        modeDataRange['70-80'] += occurrance

modeRange, modeOccurrance = 0, 0

for range, occurrance in modeDataRange.items():
    if occurrance > modeOccurrance:
        modeRange, modeOccurrance = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurrance

mode = float((modeRange[0] + modeRange[1]) / 2)
print(mode)

