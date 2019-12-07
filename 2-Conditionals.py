"""
CONDITIONAL STATEMENTS
Author: Murphy Studebaker
Week 09/09/2019

Conditional statements are used to control the flow of logic in your programs
A conditional statement is anything that can be evaluated to either True or False
"""

# THE BASIC IF STATEMENT
time = "day"
if time == "day":
    # program will execute this block if TRUE, ignore if FALSE
    # proper indentation is VERY important
    print("It is light out.")

# can also evaluate just a boolean variable
daytime == True
if daytime:
    print("It is light out.")

# can perform all comparison operations
grade = 70
if grade >= 70:
    print("You pass.")

# Once block is executed or ignored, goes on with program
if grade >= 70:
    print("You pass.")
print("Your grade was " + grade) #runs whether or not statement is True

"""
IN CLASS ASSIGNMENT
Write a program that prompts the user for the temperature (in Farenheit) and
print out what they should wear based on the following rules:

If the temperature is less than 70, they should wear pants.
If the temperature is greater than or equal to 70, they should wear shorts.
If the temperature is less than 0, tell them to just stay inside.
"""

# MORE FANCY IF STATEMENTS
# can combine expressions with and/or
daytime = True
good_weather = False

if daytime and good_weather:
    print("Play outside.")

if daytime or good_weather:
    print("Play outside anyway.")

# THE IF/ELSE STATEMENT
if daytime and good_weather:
    #runs if statement is true
    print("Play outside.")
else:
    #runs if statement is false
    print("Read a book.")
#runs if true and runs if false because it's not part of the statement
print("Have a good day.")

# USING "NOT" KEYWORD
daytime = False

if not daytime:
    print("It's dark.")

# NESTED IF STATEMENTS
if grade >= 70:
    print("YOU PASS")
    if grade == 100:
        print("AND YOU GOT A PERFECT SCORE!")
elif grade < 70:
    print("YOU FAIL")

# NESTED IF STATEMENTS PRACTICE
if temp < 0:
    print("Just stay inside")
elif temp < 70:
    if rainy == "Y":
        print("Wear pants and a raincoat")
    elif rainy == "N":
        print("Wear pants and a t-shirt")
elif temp >= 70:
    if rainy == "Y":
        print("Wear shorts and a raincoat")
    elif rainy == "N":
        print("Wear shorts and a t-shirt")
else:
    print("YOUR TEMPERATURE IS INVALID")

# MORE PRACTICE
# ask for hourly wage and hours worked
# calculate how much money made per week with overtime being > 40 hours
# ask what the overtime hourly wage is if they have worked overtime, then factor that into calculation

# USING CONDITIONLS FOR A MENU
print( "MENU: \n 1. Inspirational Quote \n 2. Song Lyric \n 3. Passage from a Book or Poem")
selection = int(input("Enter your selection: "))

if selection == 1:
    #print quote
elif selection == 2:
    #print lyric
elif: selection == 3:
    #print passage
else:
    print("Your selection is invalid.")
    quit()
