import csv
from operator import itemgetter


def load_files():
    f_read = open("items.csv", "r")
    csv_f = csv.reader(f_read)
    items = []
    for row in csv_f:
        items.append(row)
    f_read.close()
    return items


def add_item():
    new_product_info = []
    user_product = input("Item name: ")
    product_price = input("Price: $")
    product_priority = input("Priority: ")
    req = "r"
    new_product_info.append(user_product)
    new_product_info.append(product_price)
    new_product_info.append(product_priority)
    new_product_info.append(req)

    print("{}, ${} (priority {}) added to the shopping list".format(user_product, product_price, product_priority))
    return new_product_info


def main():
    print("Shopping List 0.1 - by Jose Oronos")

    item_list = load_files()

    print("Menu: ")
    print("R - List required items")
    print("C - List completed items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")
    user_choice = input("Please select an option: ").lower()

    while user_choice != "q":
        if user_choice == "r":
            print("You chose R")
            req_list = []
            for thing in item_list:
                if thing[3] == "r":
                    req_list.append(thing)
            if len(req_list) == 0:
                print("No required items")
            else:
                sorted_req_list = sorted(req_list, key=itemgetter(2))
                count = 0
                for item in sorted_req_list:
                    print("{}. {:<19} ${:>7} ({})".format(count, item[0], item[1], item[2]))
                    count += 1
        elif user_choice == "c":
            print("You chose C")
            cmp_list = []
            for thing in item_list:
                if thing[3] == "c":
                    cmp_list.append(thing)
            if len(cmp_list) == 0:
                print("No completed items")
            else:
                sorted_cmp_list = sorted(cmp_list, key=itemgetter(2))
                count = 0
                for item in sorted_cmp_list:
                    print("{}. {:<19} ${:>7} ({})".format(count, item[0], item[1], item[2]))
                    count += 1
        elif user_choice == "a":
            print("You chose A")
            new_item = add_item()
            item_list.append(new_item)
        elif user_choice == "m":
            print("You chose M")
        else:
            print("Invalid option, please choose again")
        print("Menu: ")
        print("R - List required items")
        print("C - List completed items")
        print("A - Add new item")
        print("M - Mark an item as completed")
        print("Q - Quit")
        user_choice = input("Please select an option: ").lower()

    file_save = open("items.csv", "w")
    for item in item_list:
        item = ",".join(item)
        file_save.write(str(item) + "\n")
    file_save.close()

    print("Done")


main()
