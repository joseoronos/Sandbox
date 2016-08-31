import csv

f = open("items.csv")

csv_f = csv.reader(f)

items = []

for row in csv_f:
    items.append(row)
    #print(row[0])

print(items)

f.close()
