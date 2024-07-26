numberStr = input("Enter the number to count to: ")

# Starting our count at 1
i = 1

# The input number needs to be converted to int so we can compare it to i, a number
number = int(numberStr)

# Here we are seeing if we have reached our input number yet
while i <= number:
    print(i)
    # Need to keep incrementing i, so we keep counting up
    i += 1
