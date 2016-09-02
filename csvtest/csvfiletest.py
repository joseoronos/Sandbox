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

    user_product = str(input("Item name: "))
    while user_product == " " or user_product == "":
        print("Item input cannot be blank")
        user_product = str(input("Item name: "))

    while True:
        try:
            product_price = int(input("Price: $"))
            while product_price <= 0:
                print("Price must be >= 0")
                product_price = int(input("Price: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
            continue

    while True:
        try:
            product_priority = int(input("Priority: "))
            while product_priority != 1 and product_priority != 2 and product_priority != 3:
                print("Priority must be 1, 2 or 3")
                product_priority = int(input("Priority: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
            continue

    req = "r"

    new_product_info.append(user_product)
    new_product_info.append(str(product_price))
    new_product_info.append(str(product_priority))
    new_product_info.append(req)

    print("{}, ${} (priority {}) added to the shopping list".format(user_product, product_price, product_priority))
    return new_product_info


def item_display(item_list, user_choice):
    item_display_list = []
    for item_info in item_list:
        if item_info[3] == user_choice:
            item_display_list.append(item_info)

    if user_choice == "m":
        for item_info in item_list:
            if item_info[3] == "r":
                item_display_list.append(item_info)

    if len(item_display_list) == 0:
        if user_choice == "r":
            print("No required items")
        elif user_choice == "c":
            print("No completed items")
    else:
        sorted_req_list = sorted(item_display_list, key=itemgetter(2))
        count = 0
        total = []
        for item in sorted_req_list:
            print("{}. {:<19} ${:>7.2f} ({})".format(count, item[0], float(item[1]), item[2]))
            total.append(item[1])
            count += 1
        float_total = [float(i) for i in total]
        print("The expected price for {} items: ${}".format(count, sum(float_total)))
    return item_display_list


def main():
    print("Shopping List 1.0 - by Jose Oronos")

    item_list = load_files()

    print("{} items loaded from items.csv".format(len(item_list)))

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
            r_list = item_display(item_list, user_choice)
        elif user_choice == "c":
            print("You chose C")
            c_list = item_display(item_list, user_choice)
        elif user_choice == "a":
            print("You chose A")
            new_item = add_item()
            item_list.append(new_item)
        elif user_choice == "m":
            print("You chose M")
            m_list = item_display(item_list, user_choice)
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

    """

    for item in item_list:
        print(item)

    """

    print("Done")


main()
