"""
DICTIONARIES & SETS

Dictionaries are a new type of python object that let you store
key-value pairs. Think of them as an actual dictionary, where you have a word
you want to look up (the key) in order to retrieve a definition (the value).
"""

# create an empty dictionary
car = {}
print(type(car))

# add a value pair to a dictionary
car['make'] = "Jeep"
print(car)

# define a dictionary with some initial key-value pairs
# keys CANNOT be duplicates and must be an immutable type (string, int, or tuple)
# values can be of any type, even lists or other dicts
car = {
    'make': 'Jeep',
    'model': 'Wrangler',
    'year': 2019,
    'color': 'Army Green',
    'stickers': ['ZNP', 'YNP']
}
print(car)

# accessing values by their key
# index like you would a list but by key instead of position
print('You drive a {} {}'.format(car['make'], car['model']))

# removing key value pairs from a dictionary
car.pop('color') #will return the value of the deleted key
print(car)

# looping through dictionaries
for key in car:
    print(key)

# checking if key exists in dictionary
if 'year' in car:
    print("Your car is from " + str(car['year']))

# checking if value exists in dictionary with the values() method
if 2019 in car.values():
    print("There is a car from 2019.")

# Difference between dictionaries and sets
# Sets are collections of unordered items
# sets cannot contain duplicates
desserts = {'chocolate cake','apple pie','fudge','peach cobbler'}

# add items to a set
desserts.add('pink salad')
print(desserts) #notice how it isn't added to the end

# delete items from a set
#desserts.remove('pink sad') #throws an error if does not exist
desserts.discard('pink sad') #doesn't throw an error if does not exist
desserts.discard('pink salad')
print(desserts)

# check if an item is in a set
if 'apple pie' in desserts:
    print("Serve me the applie pie")
else:
    print("No dessert for me, please.")

# join unique items from two sets with union
desserts = {'chocolate cake','apple pie','fudge','pumpkin pie'}
thanksgiving = {'turkey','mashed potatoes','pumpkin pie'}
thanksgiving_dinner = thanksgiving.union(desserts)
print(thanksgiving_dinner)

# get items from desserts not in thanksgiving
non_holiday_desserts = desserts.difference(thanksgiving)
print(non_holiday_desserts)

# get items in both sets
thanksgiving_desserts = thanksgiving.intersection(desserts)
print(thanksgiving_desserts)

# a series of responses to survey questions between 1 and 5 (list)
# a single user's settings (dictionary)
# the three different outcomes of a game that cannot change (tuple)
# three different outcomes of a game that change depending on user input (list)
# unique keywords used to classify and compare documents (set)


# PRACTICE
# Write a function that allows a user to add cars to a registry.
# Ask the user if they want to display the registered cars, add a car, or quit.
# If they choose to add a car, ask for the make, model, year, and color
# and then create a dict with that information and store it in a list of dicts.

menu ="""
1. Print registered cars
2. Add a car
3. Quit
"""
cars = []
while True:
    print(menu)
    selection = int(input("Select an option: "))
    if selection < 1 or selection > 3:
        print("Invalid Input")
        continue
    elif selection == 1:
        print(cars)
    elif selection == 2:
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        color = input("Color: ")
        car = { 'make': make, 'model': model, 'year': year, 'color': color }
        cars.append(car)
    elif selection == 3:
        break

# PRACTICE 2
# Add functionality to search through the registry by make or color
def search(key, value):
    matches = []
    for car in cars:
        if car[key] == value:
            matches.append(car)
    return matches

choice = input("Search by make or model?")
if choice == 'make':
    make_search = input("Which make to look up?")
    print(search('make', make_search))
elif choice == 'model':
    model_search = input("Which model to look up?")
    print(search('model', model_search))
else:
    print("Invalid Input")
