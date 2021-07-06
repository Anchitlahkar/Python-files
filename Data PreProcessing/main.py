import csv

data = []
with open('CSV/data_table_2.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]

planet_data = data[1:]

# converting all planet names to lower case
for data_point in planet_data:
    data_point[0] = data_point[0].lower()

# Sorting Planet in alphabatical order
planet_data.sort(key=lambda planet_data: planet_data[0])

with open('CSV/sorted_data.csv', 'a+') as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planet_data)

