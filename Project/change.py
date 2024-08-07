# -*-Python-*-
#   FILE:       change.py
#   AUTHOR:     Riley Adams
#   DATE:       August 05, 2024
#   PURPOSE:    A program to generate the required change to give someone
#
# Copyright 2024 University of Rochester. All rights reserved.
#

priceStr = input("Price of item: ")
amountGivenStr = input("Amount of money given: ")

price = float(priceStr)
amountGiven = float(amountGivenStr)

changeGiven = 0

while changeGiven > price - amountGiven:
    pass
