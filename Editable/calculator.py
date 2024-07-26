operation = ""

while operation != "exit":
    print("Input exit as the operation to exit!")
    operation = input("What operation would you like to perform? ")

    first_number_str = input("What is the first number? ")
    second_number_str = input("What is the second number? ")

    # Converting the input strings to numbers
    # See if you can handle decimal numbers, hint google may help you
    first_number = int(first_number)
    second_number = int(second_number)

    output = 0

    # Handling the + or plus operator
    # You could also make this handle "addition" or "add"
    if operation == "+" or operation == "plus":
        output = first_number + second_number

    # Add additional operations here
    # Minus, Modulo, Division, Multiplication, Exponents

    print()
    print("The result was " + str(output))
