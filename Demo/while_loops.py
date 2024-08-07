# -*-Python-*-
#      FILE :          while_loops.py
#      AUTHOR :        Robbie Kubiniec
#      DATE:           August 7, 2024
#      PURPOSE:        Demonstrate the while loop
# 
# Copyright 2024 University of Rochester. All rights reserved.
#


# A while loop is just like an if statement,
# but the only difference is that the code "inside" (tabbed in)
# will run over and over until the conditional statement is false

number = 1
# This first loop will keep running as long as number is less than or equal to 10.
# What do you think number will be after the loop is done?
while number <= 10:
    print("First loop: " + str(number))
    number = number + 1 # number goes up by one each time through the loop

print("After the first loop, number = " + str(number))

done_looping = False

# not all while loops are based on numbers. Some use "boolean" variables (True or False) to keep track.
while not done_looping:
    print("Second loop: " + str(number))
    number = number * 2 # number doubles each time through the loop!
    if number > 500:
        done_looping = True
        # We'll set done_looping to True when number is bigger than 500
        # so what is number set to when this happens? Make a prediction before you run the code!

print("After the second loop, number = " + str(number))

# Did this number surprise you? See if you can work out how number got to its final value by tracing back the steps of the algorithm!
