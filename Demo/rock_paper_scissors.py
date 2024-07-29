# -*-Python-*-
#      FILE :          rock_paper_scissors.py
#      AUTHOR :        Robbie Kubiniec
#      DATE:           July 18, 2024
#      PURPOSE:        Demonstrate a simple game of rock paper scissors
# 
# Copyright 2024 University of Rochester. All rights reserved.
#

# -- Random numbers --
# In order to generate a random event, we use the "random" module
# A module is a piece of code that python provides for you to use if you want it
# All you have to do is declare 'input <module_name>' and you're all set.
import random # Declare the 'random' module

# Seeding
# Computers generate random numbers by starting with a 'seed' and performing a bunch
# of unpredictable modifications until the number "could be anything", so it appears random.
# A seed is simply a number that changes every time we run the program.
# By default, python uses the current time, measured to the millisecond. 
# Each time you run the program, you'll see a different random result, 
# because the seed is different,
# because the time is always changing.
random.seed()

# After we generate a seed, we use the function 'randint' to get a random integer
# This function lets us specify a range, so we will ask for a random integer
# between 0 - 2.  In other words, there are three possible outcomes: 0, 1, and 2.
r = random.randint(0, 2)

# -- Computer choice --
# Once we have a random integer, we can use it to have the computer appear to pick their choice randomly.
print("Welcome to Rock Paper Scissors! Challenge the computer to a game!")
if r == 0:
    cpu_choice = "Rock"
elif r == 1:
    cpu_choice = "Scissors"
elif r == 2:
    cpu_choice = "Paper"


# -- Player input --
# raw_input is a python function that allows you to prompt the user for an input
# Whatever they enter as input becomes a string and gets assigned to the `player_choice` variable
player_choice = raw_input("Ready? Rock Paper Scissors Shoot: ")

# -- Check Player input
# Rock Paper Scissors only works if both players pick one of the three options, but the user might not follow the rules!
# If the player inputs anything other than `Rock`, `Paper`, or `Scissors`, we will ask them to try again.
# Notice that this is a while loop.
# Consider: If we replace the word 'while' with 'if', how does the program change? Does it still work?
# What happens if the user inputs an invalid choice more than once?
while player_choice != "Rock" and player_choice != "Paper" and player_choice != "Scissors":
    print("Oops! That's not a valid choice. Please pick Rock, Paper, or Scissors...")
    player_choice = raw_input("Ready? Rock Paper Scissors Shoot: ")
#end of loop
# Fun fact: The process of checking to make sure the user does what we expect, and fixing things when they go wrong,
# is called **Error Handling**. Handling Errors gracefully is an essential part of writing good code.
# Software engineers live by the mantra: "Never trust the user!"

# Once the player has chosen, the cpu reveals their choice:
print("I choose " + cpu_choice)


# -- Check who wins --
# In order to check who wins, we need to compare the player's choice to the computer's choice.
# We need to make sure we consider all possible outcomes.
if player_choice == cpu_choice:
    print("Tie!")
if player_choice == "Rock" and cpu_choice == "Paper":
    print("Paper covers rock. I win!")
elif player_choice == "Rock" and cpu_choice == "Scissors":
    print("Rock crushes scissors. You win!")
elif player_choice == "Paper" and cpu_choice == "Rock":
    print("Paper covers rock. You win!")
elif player_choice == "Paper" and cpu_choice == "Scissors":
    print("Scissors cut paper. I win!")
elif player_choice == "Scissors" and cpu_choice == "Rock":
    print("Rock crushes scissors. You win!")
elif player_choice == "Scissors" and cpu_choice == "Paper":
    print("Scissors cut paper. I win!")
