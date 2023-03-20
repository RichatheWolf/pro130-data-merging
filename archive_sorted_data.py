import csv

data = []
with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data.append(i)
    
headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[2] = data_point[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("archive_dataset_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

with open('archive_dataset_sorted.csv') as input, open('archive_dataset_sorted1.csv', 'w') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row) 