# -*-Python-*-
#   FILE:       fibonacci.py
#   AUTHOR:     Riley Adams
#   DATE:       July 26, 2024
#   PURPOSE:    Demostrative program to calculate the fibonacci sequence
#
# Copyright 2024 University of Rochester. All rights reserved.
#


# Doing 10 iterations of the fibonacci sequence
iter = 10

# Defining our first and second numbers
first = 0
second = 1

# Printing the first and second numbers
print(first)
print(second)

i = 0

while i < iter:
    # Getting the next number by adding the first and the second
    next = first + second
    print(next)

    # Shifting the values over
    # First becomes second and second becomes the next value
    first = second
    second = next

    # Incrementing to the next iteration
    i += 1
