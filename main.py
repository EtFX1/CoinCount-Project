"""modules"""

import sys

from volunteer_info_utils.handle_volunteer_info import handleVolunteerInfo

from file_handlers.read_from_instructions import readFromInstructions

from file_handlers.load_coin_count import loadCoinCount

from file_handlers.clear_coin_count import clearCoinCount

from file_handlers.read_from_coin_count import readFromCoinCount


print()
print("Welcome to the coin counter!")

# * data structure to hold all volunteer's information, which is stored in readFromCoinCount()
volunteer_list = readFromCoinCount()
print(len(volunteer_list))


def addVolunteer():
    if len(volunteer_list) == 6:
        print("Volunteer list is full. (Type 'EXIT' to exit the application)")
    else:
        handleVolunteerInfo(volunteer_list)

# @! Entry point to the application


def main():

    print()

    # * prints out instructions
    readFromInstructions()

    # * while that runs infinitely (to allow the user add as many volunteers as they want)
    while True:

        print()

        valid_commands = ["ADD", "NEW", "DISPLAY",
                          "VIEW", "CLEAR", "HELP", "EXIT"]

        # * Getting user's input

        user_response = input("> ").upper().strip()

        #! doing something different based on user input
        if user_response not in valid_commands:
            print("Please type in valid command")
            print()
            continue

        # * allows a user to add a new volunteer
        if user_response == "ADD" or user_response == "NEW":
            print()
            addVolunteer()

        # * allows a user to see "CoinCount.txt"
        if user_response == "DISPLAY" or user_response == "VIEW":
            print("(Type 'CLEAR' to clear volunteer list)")
            print()
            loadCoinCount()

        # * allows a user to delete all the data from "CoinCount.txt" and "the volunteer list"
        if user_response == "CLEAR":
            volunteer_list.clear()
            clearCoinCount()

        # * allows a user to see the instructions once again
        if user_response == "HELP":
            readFromInstructions()

        # * allows a user to exit the program
        if user_response == "EXIT":
            sys.exit(
                "Thank you for using the Coin Counter App! We appreciate your hard work in counting all the coins.")

    print("Maximum number of volunteers added")


"""
go back to the home after every volunteer is added
when the list is full, notify the user
"""


# todo: make sure you get this explained
if __name__ == "__main__":
    main()

# todo: one more thing: be able to delete a volunteer
