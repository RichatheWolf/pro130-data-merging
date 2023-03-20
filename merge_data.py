import csv

data1 = []
data2 = []
with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data1.append(i)

with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data2.append(i)

header1 = data1[0]
planet_data_1 = data2[1:]
header2 = data2[0]
planet_data_2 = data2[1:]

headers = header1 + header2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("merged_data.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
