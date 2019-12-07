"""
PYTHON BASICS PRACTICE
Author: Murphy Studebaker
Week of 09/02/2019

--- Non-Code Content ---
WRITING & RUNNING PROGRAMS
Python programs are simply text files
The .py extension tells the computer to interperet it as Python code
Programs are run from the terminal, which is a low level interaction with the computer
You must be in the directory of your program in order to run the file correctly
Switch directories by typing: cd <PATH/TO/YOUR/FILE>
(path can be found by right clicking your file and copying the full path)
Once in the right directory, type python (or python3 for Macs) and then the name of your file
EXAMPLE: python MyProgram.py

NAMING CONVENTIONS
Variable names should be lower_case,
cannot contain any python keywords,
and must be descriptive of what the variable represents

OPERATORS
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Rounded Division
**  Exponent (ex 2**2 is 2 to the power of 2)
%   Modulo aka Integer Remainder
<   Less than
==  Equal to
>   Greater than
<=  less than or equal to
>=  greater than or equal to
!=  not equal to
=   assignment (setting a value to a variable)

TYPES
int     Integer     8, 0, -1700
float   Decimal     8.0, .05, -42.5
str     String      "A character", "30", "@#$!!adgHHJ"
bool    Boolean     True, False
"""

"""
NOW FOR THE CODE
"""
# GETTING INPUT AND OUTPUTTING TO CONSOLE
# input is always a string
# saving what the user types in to the variable "name"
name = input("Enter your name: ")
print("Hello, " + name)

"""
MODULES
Modules are libraries of code written by other developers that make performing
certain functions easier. Commonly used modules are the math module (has constants
for pi and e and sqrt() functions) and the random module (randomly generate numbers)
"""
import random
user_id = random.randint(100, 1000)
print("Hello, " + name + "! Your ID is "
      + str(user_id))

# MATHEMATICAL OPERATIONS
import math
radius = float(input("Radius: "))
circ = 2 * math.pi * radius
print("The circumference is " + str(circ))
