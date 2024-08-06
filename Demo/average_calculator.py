# -*-Python-*-
#   FILE:       average_calculator.py
#   AUTHOR:     Riley Adams
#   DATE:       August 6, 2024
#   PURPOSE:    Demostrative program to calculate a grade average
#
# Copyright 2024 University of Rochester. All rights reserved.
#

# Getting the number of grades to average
gradeNum = int(input("How many grades: "))

# Starting at grade 0 and a sum of 0
gradeSum = 0
i = 0

# Looping until we have the grades needed
while i < gradeNum:
    # Getting the grade and converting it to float
    grade = float(input("Grade: "))

    # Summing up the grades and incrementing to the next grade
    gradeSum = gradeSum + grade
    i += 1

# Calculating the average, converting to string, and printing it
print("Average " + str(gradeSum / gradeNum))
