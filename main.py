"""modules"""

import sys
from volunteer_info_utils.handle_volunteer_info import handleVolunteerInfo
from file_handlers.read_from_instructions import readFromInstructions
from file_handlers.load_coin_count import loadCoinCount
from file_handlers.clear_coin_count import clearCoinCount


print()
print("Welcome to the coin counter!")


# @! Entry point to the application
def main():

    print()

    # * prints out instructions
    readFromInstructions()

    # * while that runs infinitely (to allow the user add as many volunteers as they want)
    while True:

        print("\n")

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
            handleVolunteerInfo()

        # * allows a user to see "CoinCount.txt"
        if user_response == "DISPLAY" or user_response == "VIEW":
            print("(Type 'CLEAR' to clear volunteer list)")
            print()
            loadCoinCount()

        # * allows a user to delete all the data from "CoinCount.txt"
        if user_response == "CLEAR":
            clearCoinCount()

        # * allows a user to see the instructions once again
        if user_response == "HELP":
            readFromInstructions()

        # * allows a user to exit the program
        if user_response == "EXIT":
            sys.exit(
                "Thank you for using the Coin Counter App! We appreciate your hard work in counting all the coins.")


# todo: make sure you get this explained
if __name__ == "__main__":
    main()
