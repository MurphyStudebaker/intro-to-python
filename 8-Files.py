"""
FILE I/O
Author: Murphy Studebaker
Week of November 4

Sometimes you want to write a program that reads from or
writes to external files. Common use cases for this are reading
in data as an input for some sort of processing (scraping data off websites,
doing some sort of analysis) or persisting data after your program has ended 
(saving user contacts or information that can be loaded back in)
"""

# FILE OBJECTS
# To access a file, you must first "open" it
document = open('text.txt','r')
# now the variable 'document' is a file object
# for the file 'text.txt' in read mode

# ACCESS MODES
# determine the program's ability to manipulate the file
# r : read only
# w : write, replaces what is in the file with new content
# a : append, writes new content to the end and keeps existing content
# r+ : read and write mode

# must close the document when you are done with it
document.close() 

# READING FROM A FILE
# Files are read through a buffer, so text is consumed
# and the buffer moves forward. To go back to the beginning
# of a file, you must close it and open it again.
document = open('text.txt','r')
whole_document = document.read()
document.close()

document = open('text.txt','r')
document_as_list = document.readlines()
document.close()

print(whole_document)
print(document_as_list)

# Loop through each sentence
document = open('text.txt','r')
for line in document:
    # the variable 'line' is automatically assigned each line in the file
    sentence = line.replace('\n','')
    print(sentence + "!")
document.close()

# WRITING TO A FILE
document = open('text.txt','w')
document.close()
# notice that the tabs and newlines are kept in the file
# also, that 'w' mode replaces everything in the original file

document = open('text.txt','a')
document.write('ART FROM THE INTERNET')
document.close()

# MAKING THINGS EASIER WITH 'WITH' STATEMENTS
# using with automatically closes the file once it's done
with open('text.txt','r+') as f:
    n = 0
    for line in f:
        line = line.replace('\n', '')
        print(str(n) + line)
        n +=1
    f.write(str(n))

"""
# PRACTICE: ADAPTING PIGLATIN PROGRAM
# Modify your piglatin program to read and write from a file
# Your program should read in a file, 
# pass each word in to your word_to_pig function,
# then replace the contents of the file with the version in piglatin.
"""

def word_to_pig(word):
    pig_word = word.lower()
    if word[0] in "aeiou":
        # starts with a vowel, add yay
        pig_word += 'yay'
    else:
        pig_word = pig_word[1:] + pig_word[0] + "ay"
    return pig_word[0].upper() + pig_word[1:]

pig_version = ""
sentences = []
with open('piggy.txt','r') as f:
    for line in f:
        sentence = line.split()
        pig_sentence = []
        for word in sentence:
            pig_sentence.append(word_to_pig(word))
        sentences.append(' '.join(pig_sentence))

with open('piggy.txt','w') as f:
    for sentence in sentences:
        f.write(sentence + '\n')
    #f.writelines(sentences) #can write a list to the file with writelines() function

"""
ERRORS

As I'm sure you're familiar with, sometimes operations in your program can produce errors.
These are useful when debugging to eliminate incorrect coding practices in your program,
but sometimes an unexpected user input can cause an otherwise functioning program to crash.
To account for this, Python lets you implement try/except statements.
"""
try:
    #the block of code to attempt to run
    doesnt_exist = open('does_not_exist.txt','r')
except FileNotFoundError:
    # if a FileNotFoundError occurs in the try block, this runs
    print("That file does not exist.")
except:
    # if any other type of error occurs in the try block, this runs
    print("Something happened. Sorry :(")
# make sure to order your except statements in order of specificity,
# leaving the general 'except' for last
# so you can give specific debugging info to the user
