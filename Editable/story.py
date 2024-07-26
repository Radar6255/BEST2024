name = input("Welcome traveller, what is your name? ")

questing = input("Would you like a quest, " + name + "?(y/n) ")

if questing == "y":
    print()
    print()
    print("    1. Free the villagers from the evil dragon!")
    print("    2. Find the missing servant")
    print("    3. Clean the town hall")

    option = input("Please select a quest from the board above! ")
    if option == "1":
        print("Fight the dragon")
        # Continue the story here, be sure to add decisions
    elif option == "2":
        print("Find the servant")
        # Continue the story here, be sure to add decisions
    elif option == "3":
        print("Clean the town hall")
        # Continue the story here, be sure to add decisions
else:
    print("You chose to rest and work another day")
    # You could continue the story here too!
