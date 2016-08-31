import csv


def main():
    print("Shopping List 0.1 - by Jose Oronos")

    f = open("items.csv")
    csv_f = csv.reader(f)
    items = []
    for row in csv_f:
        items.append(row)

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
            for thing in items:
                if thing[3] == "r":
                    req_list.append(thing)
            if len(req_list) == 0:
                print("No required items")
            else:
                print(req_list)
        elif user_choice == "c":
            print("You chose C")
            cmp_list = []
            for thing in items:
                if thing[3] == "c":
                    cmp_list.append(thing)
            if len(cmp_list) == 0:
                print("No completed items")
            else:
                print(cmp_list)
        elif user_choice == "a":
            print("You chose A")
            new_product_info = []
            user_product = input("Item name: ")
            product_price = input("Prioe: $")
            product_priority = input("Priority: ")
            req = "r"
            new_product_info.append(user_product)
            new_product_info.append(product_price)
            new_product_info.append(product_priority)
            new_product_info.append(req)
            items.append(new_product_info)
            print("{}, ${} (priority {}) added to the shopping list".format(user_product, product_price, product_priority))
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
    print("Done")


main()
