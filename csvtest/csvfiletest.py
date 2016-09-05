"""
Name: Jose Oronos
Date: 
"""

import csv
from operator import itemgetter

"""
Pseudocode for load_files function

define function as load_files()
    set f_read = open file "items.csv" in read mode
    set csv_f = csv.reader(f_read)
    items = empty list
    for row in csv_f:
        append row into items
    close f_read
    return list

"""


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
    while user_product.isspace() or user_product == "":
        print("Item input cannot be blank")
        user_product = str(input("Item name: "))

    while True:
        try:
            product_price = float(input("Price: $"))
            while product_price < 0:
                print("Price must be >= 0")
                product_price = float(input("Price: "))
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

    print("{}, ${:.2f} (priority {}) added to the shopping list".format(user_product, product_price, product_priority))
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
            return item_display_list

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
        return sorted_req_list


"""
Pseudocode for mark_item function

define function as mark_item(m_list):
    set list_with_count = empty list
    set marked_item = empty list
    set count = 0
    for items in m_list
        set item_info = count, product name, product price, priority, and mark
        append item_info into list_with_count
        increment count by 1

    set stop_check = True
    while stop_check = True:
        Try this:
            set count_list = empty list
            for items in list_with_count:
                append count to count_list

            set user_mark = user input
            while user_mark is not in count_list:
                display "Invalid item number"
                set user_mark = user input

            for items in list_with_count:
                if count == user_mark:
                    set mark == "c"
                    append product name into marked_item
                    append product price into marked_item
                    append priority into marked_item
                    append mark into marked_item
            stop_check = False
        detects a value error:
            display "Invalid input;  enter a valid number"
            continue Try

        display "(Product name) marked as completed"
        return marked_item
"""


def mark_item(m_list):
    list_with_count = []
    marked_item = []
    count = 0
    for item in m_list:
        item_info = [count, item[0], item[1], item[2], item[3]]
        list_with_count.append(item_info)
        count += 1

    stop_check = True
    while stop_check == True:
        try:
            count_list = []
            for item in list_with_count:
                count_list.append(item[0])

            user_mark = int(input("Enter the number of an item to mark as completed: "))
            while user_mark not in count_list:
                print("Invalid item number")
                user_mark = int(input("Enter the number of an item to mark as completed: "))

            for item in list_with_count:
                if item[0] == user_mark:
                    item[4] = "c"
                    marked_item.append(item[1])
                    marked_item.append(item[2])
                    marked_item.append(item[3])
                    marked_item.append(item[4])
            stop_check = False
        except ValueError:
            print("Invalid input; enter a valid number")
            continue

    print("{} marked as completed".format(marked_item[0]))
    return marked_item


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
            item_display(item_list, user_choice)
        elif user_choice == "c":
            print("You chose C")
            item_display(item_list, user_choice)
        elif user_choice == "a":
            print("You chose A")
            new_item = add_item()
            item_list.append(new_item)
        elif user_choice == "m":
            print("You chose M")
            m_list = item_display(item_list, user_choice)
            if len(m_list) == 0:
                print("No required items")
            else:
                comp_item = mark_item(m_list)
                for item in item_list:
                    if item[0] == comp_item[0]:
                        item_list.remove(item)
                        item_list.append(comp_item)
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

    print("{} items saved to items.csv".format(len(item_list)))

    print("Have a nice day :)")


main()
