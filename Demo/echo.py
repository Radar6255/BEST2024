# Setting an initial message, this just needs to not be "exit"
message = ""

# While the user hasn't exited
while message != "exit":
    # Getting the user input
    message = input("Enter your message, input exit to exit: ")

    # Echoing back to the user
    print(message)
