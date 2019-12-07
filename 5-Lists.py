"""
LISTS & TUPLES
Author: Murphy Studebaker
Week of 10/21/2019

Lists are a type of object in python that can store several values
They are indexable starting at 0 (like strings) and mutable (unlike strings),
so you can add and remove items from a list without creating a new  object.
Lists can store mixed values (i.e. ints and strings)

Tuples are similar to lists, except they are immutable, meaning you cannot
change the contents of the list.


#the humble python list
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

#indexing lists
print(days_of_week[0]) #first position
print(days_of_week[-1]) #last position
print(len(days_of_week)) #length

# MANIPULATING LISTS
#add an item to the end of a list with append()
days_of_week.append("Saturday")
days_of_week.append("Sunday")
days_of_week.append("The Weekend")
print(days_of_week)

# remove the last item in the list with pop()
days_of_week.pop()
print(days_of_week)

# remove an item by value
days_of_week.remove('Monday')
print(days_of_week)

# remove an item by index
del days_of_week[0]
print(days_of_week)

# insert an item by index
days_of_week.insert(4, "Another Saturday")
print(days_of_week)

# find the index of an item by value
funday = days_of_week.index('Sunday')

# change an item at a specific position
days_of_week[funday] = "Funday"
print(days_of_week)

# SORTING LISTS
midterm_grades = [80,80,95,98,95,77,83,65,98,100,62]

# THERE ARE TWO WAYS TO SORT LISTS
# sorted() returns the sorted list as a new variable
# default is ascending
sorted_grades = sorted(midterm_grades)
print(sorted_grades)

# .sort() sorts the list in place, and does not make a copy
print(midterm_grades)
midterm_grades.sort()
print(midterm_grades)

# can set parameter reverse to True on either method
print(sorted(midterm_grades, reverse=True))
midterm_grades.sort(reverse=True)
print(midterm_grades)

# TUPLES
# Tuples are like lists except they are UNCHANGEABLE
# Use a tuple when you want to force the contents to be permanent
my_tuple = ('This','is','a','tuple')

# you can still index them
print(my_tuple[3])

# but you can't add, remove, or manipulate items
my_tuple[3] = 'illegal operation' #this won't work
print(my_tuple)

# LIST PRACTICE
# Find the median of a list of integers
def get_median(numbers):
    sorted_list = sorted(numbers)
    median = 0
    if (len(numbers) % 2) == 0:
        # even length, need to get avg of two middle nums
        m1 = sorted_list[len(numbers) // 2]
        m2 = sorted_list[(len(numbers) // 2) - 1]
        median = (m1 + m2)/2
    else:
        # odd length, just get the middle number
        median = sorted_list[(len(numbers) // 2)]
    return median

midterm_grades = [80,80,95,98,95,77,83,65,98,100,0]
print(sorted(midterm_grades))
print(get_median(midterm_grades))
print(midterm_grades)

# MAKING LISTS FROM STRINGS AND VICE VERSA
# Split a big string into a list of smaller strings with .split()
my_sentence = "Pandas are cool"
words = my_sentence.split() #default splits by spaces
print(words)

things = "bears,beets,battlestar galactaca"
separate_things = things.split(',') #whatever you put in parentheses splits the string
print(separate_things) #notice how battlestar galactaca is not split up

# You can make a string out of a list with .join()
things_again = ' '.join(separate_things) #whatever you put before join will be between items
print(things_again)
things_and = ' and '.join(separate_things)
print(things_and)

# MORE PRACTICE
# Write a function that returns a list of only the unique letters in a string
def get_unique(input_string):
    seen = []
    for letter in input_string:
        if letter in seen:
            # not unique
            continue
        else:
            # unique because we haven't seen it before
            seen.append(letter)
    return seen

print(get_unique('banana'))

# Now change the above function to take in a sentence and return a list of
# only the unique words, in alphabetical order
def get_unique(input_string):
    seen = []
    words = input_string.split()
    for word in words:
        if word in seen:
            # not unique
            continue
        else:
            # unique because we haven't seen it before
            seen.append(word)
    return seen

print(sorted(get_unique("hey hey what's up")))

# Write a function that takes an input list of at least 5 songs and
# returns a list of the songs in randomly shuffled order
import random
def shuffle_playlist(songs):
    #initializes an array with placeholders the length
    #of the input list songs
    shuffled_songs = ["Song"] * len(songs)
    indexes = []
    for song in songs:
        new_index = random.randint(0, len(songs)-1)
        while (new_index in indexes):
            new_index = random.randint(0, len(songs)-1)
        shuffled_songs[new_index] = song
        indexes.append(new_index)
    return shuffled_songs

print(shuffle_playlist(['Mr Brightside','Wonderwall','Yeah 3X',"Stacy's Mom",'Burnin Up']))
"""
def func1(a_list,b_list):
    c = sorted(b_list)
    c.remove(3)
    print(c)
    c += a_list
    return c

a = [6,5,2,8]
b = [0,-4,7,3]
c = func1(a,b)
print(c)
