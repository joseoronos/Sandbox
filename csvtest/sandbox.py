import csv



def load_data():
    with open("items.csv", "r") as test_file:
        test_file_reader = csv.reader(test_file)
        file_list = []
        for row in test_file_reader:
            file_list += [row]

    test_file.close()
    return file_list


def show_required_list(file_list):
    for item in file_list:
        if item[3] == "r":
            print(item)


def show_completed_list(file_list):
    for item in file_list:
        if item[3] == "c":
            print(item)


def main():
    print("Shopping List 0.1 - by Jose Oronos")
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
            required_items = load_data()
            show_required_list(required_items)
        elif user_choice == "c":
            print("You chose C")
            completed_items = load_data()
            show_completed_list(completed_items)
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
