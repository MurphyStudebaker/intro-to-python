"""
FUNCTIONS
Author: Murphy Studebaker
Week of 10/14/2019

Functions allow you organize your programs,
remove duplicate operations, and simplify complex computations
by separating your code into reusable chunks.

They have two main parts:
1. PARAMETERS (Inputs)
Variables passed into the function to be used inside the function
2. RETURNS (Outputs)
the object (or objects) returned by the function

And they must have a definition before they are called in the program.
"""

# Functions must first be defined
def hello_world(name): #get name as an input parameter
    # add any logic or computations here
    return ("Hello, " + name + "!") #send this value back

# Then they can be called throughout the code
print(hello_world("Murphy")) #pass in Murphy as name and print the returned value


# Parameters can have default values
def hello_world(name="world"):
    return ("Hello, " + name + "!")
# when no paramter is given, the value is set to the default
print(hello_world())

# TOTAL PRICE FUNCTION
# don't need to be same variable name, just need to be in same order
def get_total_price(subtotal, tax_rate):
    tax = subtotal * (tax_rate/100)
    return (subtotal + tax)

sub = float(input("Subtotal: "))
tr = float(input("Tax rate: $"))
#pass in sub and tr for subtotal and tax rate
print("Your total is ", get_total_price(sub, tr))

# VARIABLES ARE LOCAL TO THE FUNCTION
# Be weary of your variable names, as parameter names will take precedence over
# variables with the same name outside of the function
number = 0

def change_number(number):
    print(number*2)

another_variable = 4
change_number(another_variable)

# PRACTICE
# 1. Write a function that takes a grade (0 - 100)
# and return its letter value (A, B, C)
def get_letter_grade(number_grade):
    letter_grade = ""
    if number_grade > 90:
        letter_grade = "A"
    elif number_grade > 80:
        letter_grade = "B"
    elif number_grade > 70:
        letter_grade = "C"
    elif number_grade > 60:
        letter_grade = "D"
    elif number_grade > 0:
        letter_grade = "F"
    else:
        letter_grade = "INVALID"
    return letter_grade

# Write a function that calculates the cost of a vacation
def get_trip_cost(days, hostel_cost, food_allowance, plane_ticket):
    return ((days*hostel_cost) + (days*food_allowance) + plane_ticket)

# Write a function that takes in a number from 1-12
# and returns the corresponding month as a string
def to_month(number):
    month = ""
    if number == 1:
        month = "January"
    elif number == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    return month

# Write a function that takes a MM/DD/YYYY date
# And returns it written out as a string
def write_date(date):
    month = date[0:2]
    day = date[3:5]
    year = date[6:]
    if month == '01':
        print("January " + day +", "+year)
    # elif through all the months

write_date('01/12/2019')
