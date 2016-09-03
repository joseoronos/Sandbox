"""
import csv

f = open("items.csv")

csv_f = csv.reader(f)

items = []

for row in csv_f:
    items.append(row)
    #print(row[0])

print(items)

f.close()
"""


def user_choice(item_list):
    user_delete = input("Which one would you like to replace with the letter 'A'?: ")
    thing_count = 0
    new_list = []
    for thing in item_list:
        item = "{}. {}".format(thing_count, thing)
        thing_count += 1
        new_list.append(item)
    for item in new_list:
        if item[0] == user_delete:
            print(user_delete)
            item[3].replace(item[3], "A") + item
    print(new_list)


def main():
    item_list = []
    count = 0
    while count < 5:
        user_input = input("Thing: ")
        item_list.append(user_input)
        count += 1

    thing_count = 0
    for thing in item_list:
        print("{}. {}".format(thing_count ,thing))
        thing_count += 1

    user_choice(item_list)

main()


"""
def main():
    num_list = []
    while True:
        try:
            userInput = int(input("Number: "))
            num_list.append(userInput)
            break
        except ValueError:
            print("Not an integer! Try again.")
            continue

    print(num_list)
main()
"""

