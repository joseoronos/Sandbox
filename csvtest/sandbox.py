import csv

def output_data():
    with open("items.csv", "r") as test_file:
        test_file_reader = csv.reader(test_file)
        file_list = []
        for row in test_file_reader:
            if len(row) != 0:
                file_list = file_list + [row]

    test_file.close()

    for item in file_list:
        print(item)

def main():
    in_file = open("items.csv", "r")
    print("Shopping List 0.1 - by Jose Oronos")
    print("Menu: ")
    print("""R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit""")
    user_choice = input("Please select an option: ").lower()
    while user_choice != "q":
        if user_choice == "r":
            print("You chose R")
            output_data()
        elif user_choice == "c":
            print("You chose C")
        elif user_choice == "a":
            print("You chose A")
            ting_name = input("Enter ting: ")
            ting_price = input("Enter price of ting: ")
            ting_priority = input("Enter priority of ting: ")
            req = "r"
            with open("items.csv", "a") as test_file:
                test_file_writer = csv.writer(test_file)
                test_file_writer.writerow([ting_name, ting_price, ting_priority, req])
            test_file.close()
        elif user_choice == "m":
            print("You chose M")
        print("""R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit""")
        user_choice = input("Please select an option: ").lower()
    print("Done")

main()

