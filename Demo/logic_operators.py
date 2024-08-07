# -*-Python-*-
#   FILE:       logic_operators.py
#   AUTHOR:     Riley Adams
#   DATE:       August 07, 2024
#   PURPOSE:    Demostrate logic operators
#
# Copyright 2024 University of Rochester. All rights reserved.
#

# Testing some logic operators
print("Comparison operators")
print("8 == 10: " + str(8 == 10))
print("8 != 10: " + str(8 != 10))

# You can compare strings too!
print("'hello' == 'hello': " + str('hello' == 'hello'))
print("'hello' != 10: " + str('hello' != 10))
print("'True' == True: " + str('True' == True))

print("3 >= 7: " + str(3 >= 7))
print("4 <= 4: " + str(4 <= 4))
print("4 < 4: " + str(4 < 4))
print("1 > 9: " + str(1 > 9))
print()

print("Boolean operators")
print("Not True: " + str(not True))

print("True or True: " + str(True or True))
print("False or True: " + str(False or True))
print("False or False: " + str(False or False))

print("True and True: " + str(True and True))
print("False and True: " + str(False and True))
print("False and False: " + str(False and False))
print()

# Example of combining elements
print("Combining multiple operators")
print("5 > 9 and 3 < 7: " + str(5 > 9 and 3 < 7))
print("5 < 9 and 3 < 7: " + str(5 < 9 and 3 < 7))
