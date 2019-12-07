"""
LOOPS
Author: Murphy Studebaker
Week of 09/16/2019

Loops allow you to iterate through series (like letters in a word)
or repeat code until a condition is False. They are convenient any time
you want your program to repeat code multiple times.
"""
# THE FOR LOOP
# Use for loops when there is an expected amount of times a loop should run
lucky_number = int(input("Enter desired number: "))
for i in range(10):
    print(i)
    if i == lucky_number:
        print("We found the lucky number!")
        break #stops the loop completely

unlucky_number = int(input("Enter nasty number: "))
for i in range(10):
    if i == unlucky_number:
        print("Skipping unlucky number")
        continue #stops current iteration of loop and goes to the next
    print(i)
else:
    print("Goodbye")

# ITERATING THROUGH STRINGS WITH A FOR LOOP
match = True
word1 = "WORD"
word2 = "ORDW"
for letter1 in word1:
    if letter1 not in word2:
        match = False
print(match)

# FOR LOOP PRACTICE
# Write a program that gets a word from the user and prints out the number of
# vowels in that word.

word = input("Enter word:")
vowels = 0
for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter == "u":
        vowels += 1
print("Your word has " + str(letters) + " vowels")

# NESTED FOR LOOP PRACTICE - STAIRCASE
# Get height of staircase from user (ie. number of steps)
# Width and height of staircase will be equal, with each step having one less *
height = int(input("Enter staircase height: "))
width = 1
for step in range(height):
    step_content = ""
    for i in range(width):
        step_content += "*"
    width += 1
    print(step_content)

# THE WHILE LOOP
# While loops are useful when you want to repeat code as long as a condition is met.
# While loops must have a stop condition, a case where the conditional statement
# is no longer true.
while number < 10:
    print(number) #runs infinitely

while number < 10:
    print(number)
    number += number #number increases until it is no longer less than 10


# PRINTING ALL THE EVEN NUMBERS BETWEEN 1 AND 10 WITH LOOPS
# Sometimes, you can accomplish the same task with either kind of loop
print("FOR")
for number in range(11):
    if (number % 2) == 0:
        #number is even
        print(number)

print("WHILE")
number = 0
while number <= 10:
    if (number % 2) == 0:
        print(number," is EVEN")
    else:
        print(number, " is ODD")
    number += 1

# When you don't know how many times a loop should run, use a while loop
import random
match = False
number = random.randint(1,10)

while(match != True):
    guess = int(input("Enter your guess: "))
    if guess == number:
        match = True
        print("YOU WIN!")
    else:
        print("WRONG!")

"""
PRACTICE - COMPOUND INTEREST
Get input from the user for the amount of money to invest, the interest rate,
and the years they plan to invest. Then print out the expected sum of money at
the end of their investment.
"""
inv_years = int(input("Years you plan to invest: "))
inv_amount = float(input("Amount to Invest: "))
inv_interest = float(input("Yearly Interest Rate on Investment: "))

year = 1
balance = inv_amount
while year <= inv_years:
    gains = balance*(inv_interest/100)
    balance += gains
    year += 1
print("After ", inv_years, " years, your balance will be $", balance)


"""
PRACTICE - ATM
Ask the User if they want to make a deposit, a withdrawal, or quit
Each user starts with a balance of 0, and the account has a maximum balance of 500
Users should not be able to withdraw the amount input if it will result in a balance less than 0
or deposit if the amount will exceed the maximum
After each operation (including quit) print the account balance
The program should run until the user decided to quit
"""
print("WELCOME TO YOUR ATM \n 1. Make a Deposit \n 2. Make a Withdrawal \n 3. Quit")
selection = 0
balance = 0
while(True):
    selection = int(input("Enter your selection: "))
    if selection == 1:
        # Deposit
        deposit_amount = float(input("Enter deposit amount: "))
        if (deposit_amount + balance) > 500:
            print("That deposit will exceed the maximum of $500")
        else:
            balance += deposit_amount
    elif selection == 2:
        # Withdrawal
        wd_amount = float(input("Enter your withdrawal amount: "))
        if (balance - wd_amount) < 0:
            print("That withdrawal will overdraw your account.")
        else:
            balance -= wd_amount
    elif selection == 3:
        break
    else:
        selection = int(input("Invalid Selection. Please choose again: "))
    print("Your balance is $" + str(balance))

print("Thank you for using our ATM.")
