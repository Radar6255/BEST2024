# -*-Python-*-
#   FILE:       echo.py
#   AUTHOR:     Riley Adams
#   DATE:       July 26, 2024
#   PURPOSE:    Program to echo input back to the user
#
# Copyright 2024 University of Rochester. All rights reserved.
#


# Setting an initial message, this just needs to not be "exit"
message = ""

# While the user hasn't exited
while message != "exit":
    # Getting the user input
    message = input("Enter your message, input exit to exit: ")

    # Echoing back to the user
    print(message)
