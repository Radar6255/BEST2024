# Setting an initial message, this just needs to not be "exit"
message = ""

# Stripping the message from the user to remove trailing whitespace, such as enter keys
while message.strip() != "exit":
    # Getting the user input
    message = input("Enter your message, input exit to exit: ")
    # Echoing back to the user
    print(message)
