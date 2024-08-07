# -*-Python-*-
#      FILE :          string_reverser.py
#      AUTHOR :        Robbie Kubiniec
#      DATE:           July 29, 2024
#      PURPOSE:        Demonstrate how to reverse a string
# 
# Copyright 2024 University of Rochester. All rights reserved.
#



print("Welcome to String Reverser.")
string_to_reverse = input("Please enter any string: ")

# Let's use a variable called `output` to store the reversed string as we build it
output = ""

# -- Index --
# An `index` is a number that represents a position in a string or list.
# For example: in the string 'Hello World!"
# The character at index 0 is 'H' (index counts up from 0)
# The character at index 4 is 'o'
# The character at index 5 is ' ' (a space still counts as a character!)
# The character at index 11 is '!'
# Note that the string has length 12, so but there is no 'index 12'.
# It stops at 11 because it started at 0.
index = 0

# While Loop
# This loop steps through each character in the string, one by one.
# We want it to stop when it gets to the end of the string, so we compare
# index to the length of the string.
# Note that we use index < len(string_to_reverse) rather than <= (less than or equal to).
# Using the information above about index, think about why we use < instead of <=.
while index < len(string_to_reverse):
    # -- Reversing the string --
    # This step right here is the key to reversing the string.
    # How does this work? Try writing each step on a piece of paper to test it yourself.
    # Note that we append (or add) each character to the front of output instead of the end
    output = string_to_reverse[index] + output
    # What would happen if you changed the line to: `output = output + string_to_reverse[index]`?
    # Make a guess, and then try it out!

    # We always want to increase our index by 1 each step through the loop.
    # This makes sure it goes to each character in the string, one by one.
    index += 1
#end of loop

print("Here's your string backwards: ")
print(output)
