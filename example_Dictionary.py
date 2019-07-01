import csv

with open('solar_2013.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['월'], row['일'], row[' 1h '])
