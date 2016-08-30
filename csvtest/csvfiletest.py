import csv

"""
def main():
    with open('items.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        dates = []
        colors = []
        for row in readCSV:
            color = row[3]
            date = row[0]

            dates.append(date)
            colors.append(color)

        print(dates)
        print(colors)

main()
"""

"""
def main():
    with open('items.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in readCSV:
            product = row[0]
            product_cost = row[1]
            priority = row[2]
            print("{}.{} {} {}".format(count, product, product_cost, priority))
            count += 1
main()
"""

"""
def main():
    with open('items.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            signal = row[3]
            if signal == "c":
                print(row)
main()
"""
                

