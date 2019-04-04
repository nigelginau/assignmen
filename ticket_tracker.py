# Open places.csv
csv_file_name = open("places.csv", 'w')

# Welcome message
print(" Welcome to the Travel Tracker by Nigel Ginau")
print("Menu:\n L - List places \n A - Add new place \n M - Mark a place as visited \n Q - Quit")

list_of_places = [0]

for i in range(0, len(list_of_places)):
    name_of_place = [str(input("Name: "))]
    country = [str(input("Country: "))]
    priority = [int(input("Priority: "))]
print(name_of_place, file=csv_file_name)
csv_file_name.close()
