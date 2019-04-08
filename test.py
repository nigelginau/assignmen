# Open places.csv
csv_file_name = open("places.csv", 'r+')

# Welcome message
print(" Welcome to the Travel Tracker by Nigel Ginau")
print("Menu:\n L - List places \n A - Add new place \n M - Mark a place as visited \n Q - Quit")

list_of_places = 0

user_input = str(input('>>')).upper()

while user_input != "Q":
    # Counter
    len_list = str(csv_file_name.readlines())
    length_of_list = len(len_list)
    if user_input == "L":
        for i in range(1, length_of_list + 1):
            read_list_of_places = str(csv_file_name.readlines())
            print(read_list_of_places)
    elif user_input == "A":
        # for i in range(1, len(list_of_places + 1)):
        name_of_place = [str(input("Name: "))]
        country = [str(input("Country: "))]
        priority = [str(input("Priority: "))]
        if (name_of_place[0]).isnumeric() == True:
            print("Name must be in alphabets")
            name_of_place = [str(input("Name: "))]
        elif (country[0]).isnumeric() == True:
            print("Country must be in alphabets")
            country = [str(input("Country: "))]
        elif priority < ['0']:
            print("Number must be > 0")
            priority = [int(input("Priority: "))]
        elif (priority[0]).isalpha() == True:
            print("Invalid input; enter a valid number")
            priority = [int(input("Priority: "))]

        list_of_places = list_of_places + 1
        print("{},{},{}".format(list_of_places, name_of_place[0], "", "", country[0],
                                "", priority[0]), file=csv_file_name)
        csv_file_name.close()
    elif user_input == "M":
        print(file=csv_file_name)
        place_marked = str(input("Enter the number of a place to mark as visited"))
    elif user_input == "":
        print("Input can not be blank")
        user_input = str(input()).upper()
    else:
        print("Input must be the options in the menu")
        user_input = str(input()).upper()

user_input = str(input(">>")).upper()

csv_file_name.close()
