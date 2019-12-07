"""
STRINGS
Author: Murphy Studebaker
Week of 09/30/2019

Ah, the amazing string. Strings are a type of variable that contain a series of
characters. They can be alphanumeric (abc123) or symbols (!@#), but are always
represented between quotation marks (single or double)
"""

# STRINGS ARE INDEXABLE
# You can get the character at a certain position in a string by indexing.
# name_of_string[position]
# Strings are index 0 (meaning the first character has a position of 0, not 1)
college = "Chapman University"
print("First letter: " + college[0])
print("Last letter: " + college[-1])
print("First Word: " + college[0:7])
print("Length: " + str(len(college)))

# can also index with an int variable
for index in range(len(college)):
    print(str(index) + ": " + college[index])

# strings are immutable, so you can't change one letter
# you have to reassign the entire string
sign = "Hollywood"
sign[6] = "e"
sign[7] = "e"
print(sign)
sign = "Hollyweed"
print(sign)

# Strings can be changed to all upper or lowercase using methods
print("UPPER(): " + sign.upper())
print("LOWER(): "+ sign.lower())

# when comparing strings, equality is case sensitive
print("Chapman" == "chapman")

"""
PRACTICE - PALINDROME
A palindrome is a word spelled the same way backwards and forewords.
Write a program that checks if a word is a palindrome or not.
"""
word = "racecar"
palindrome = True
i = 0
while i < len(word):
    compare = -(i+1)
    if word[i] != word[compare]:
        palindrome = False
        break
    i += 1
print(palindrome)


# Strings have lots of handy methods to do certain tasks
# find() gets the index of a substring within a bigger string
# it will return -1 if the substring does not exist
sentence = "It was the best of times, it was the worst of times."
print(sentence.find('best'))

if sentence.find('random') == -1:
    print("Not in string")

# replace() will find all instances of the first string and replace them
# with the second string
script = "Dwight Dwit Dwight"
print(script.replace("Dwight","Samuel L. Chang"))

# Different ways to format prints
# use curly braces as a placeholder
# format in order
welcome = "Hi, {} {}!"
print(welcome.format("Murphy","Studebaker"))
#format with numbers as order
welcome_nums = "Hi, {1} {0}!"
last_name = "Studebaker"
first_name = "Murphy"
print(welcome_nums.format(last_name, first_name))
#format with variable names
welcome_vars = "Hi, {fn} {ln}!"
print(welcome_vars.format(fn = "Murphy", ln = "Studebaker"))

# can concatenate (or glue together) strings with +
full_name = first_name + " " + last_name + "!"
print("Hi, " + full_name)

#format to specific decimal places
total = 15.342
print("Your total is ${:.2f}".format(total))

# Practice Problems
# get lyrics from an explicit song and replace all of the cuss words with friendlier version
# get a string from users and print it back out without any vowels
# get a dna sequence and print out its compliment
# A & T, G & C

# this is a multi-line string
song = """
    I see you driving round town
    with the girl I love,
    and I'm like, fuck you (ooo)
"""

print(song.replace('fuck','forget'))
