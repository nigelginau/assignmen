def method_name():
    # Open places.csv
    csv_file_name = open("places_01.csv", 'r+')
    # Welcome message
    print(" Welcome to the Travel Tracker by Nigel Ginau")
    print("Menu:\n L - List places \n A - Add new place \n M - Mark a place as visited \n Q - Quit")
    # Add prompt for user to input option from menu
    user_input = str(input('>>')).upper()
    # Grab number of list of places
    number_list_of_places = len(csv_file_name.readlines())
    while user_input != "Q":  # Continue  while loop until user input is Q

        if user_input == "L":  # List all places in "places.csv" file
            csv_file_name = open("places.csv", 'r+')
            file_content = csv_file_name.read()
            print(format(file_content))

        elif user_input == "A":  # Add new places onto "places.csv" file
            name_of_place = [str(input("Name: "))]
            country = [str(input("Country: "))]
            priority = [str(input("Priority: "))]

            # Error checking
            if (name_of_place[0]).isnumeric() == True:  # User input is a number
                print("Name must be in alphabets")
                name_of_place = [str(input("Name: "))]
            elif (country[0]).isnumeric() == True:  # User input is a number
                print("Country must be in alphabets")
                country = [str(input("Country: "))]
            elif priority < ['0']:  # User input is less than 0
                print("Number must be > 0")
                priority = [int(input("Priority: "))]
            elif (priority[0]).isalpha() == True:  # User input is a letter
                print("Invalid input; enter a valid number")
                priority = [int(input("Priority: "))]

            # Print the new place to the "places.csv" file
            print("{0}.{1:<10} in {2:<10} priority {3:<10}".format(number_list_of_places + 1, name_of_place[0],
                                                                   country[0],
                                                                   priority[0]), file=csv_file_name)

        elif user_input == "M":  # Mark a place as visited
            print(file=csv_file_name)
            place_marked = str(input("Enter the number of a place to mark as visited"))
        elif user_input == "":  # Instruct user to enter a valid input option for the meny
            print("Input can not be blank")
            user_input = str(input('>>')).upper()
        else:  # Instruct user to enter a valid option
            print("Input must be the options in the menu")
            user_input = str(input('>>')).upper()

        # User enters "Q" to end while loop and quit "ticket_tracker.py"
        user_input = str(input(">>")).upper()
    # Close "places.csv" file
    csv_file_name.close()


method_name()