import csv

dataset1 = []
dataset2 = []

with open('CSV/final.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset1.append(row)


with open('CSV/sorted_data.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset2.append(row)

header_1 = dataset1[0]
header_2 = dataset2[0]

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

headers = header_1 + header_2

planet_data = []

for index, data in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open('CSV/final_data.csv', 'a+') as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planet_data)