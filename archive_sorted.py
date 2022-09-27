import csv

data = []

with open("PSCompPars_2022.09.24_04.02.38.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
planet_data = data[1:]

#Converting all planet names to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[2])


with open("tarini.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#remove blank lines
with open('tarini.csv') as input, open('tarini1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)
