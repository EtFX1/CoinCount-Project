"""modules"""

import sys
from handlers_utils.handlers import handlers
from file_handlers.read_from_instructions import readFromInstructions
from file_handlers.load_coin_count import loadCoinCount
from file_handlers.clear_coin_count import clearCoinCount


print()
print("Welcome to the coin counter!")
# @! Entry point to the application


def main():

    # todo: add comments in this function
    print()
    # * prints out instructions
    readFromInstructions()

    # * while that runs infinitely
    while True:

        print("\n")

        valid_commands = ["ADD", "NEW", "DISPLAY",
                          "VIEW", "CLEAR", "HELP", "EXIT"]

        # * Getting user response

        user_response = input("> ").upper().strip()

        if user_response not in valid_commands:
            print("Please type in valid command")
            print()
            continue
        if user_response == "ADD" or user_response == "NEW":
            handlers()
        if user_response == "DISPLAY" or user_response == "VIEW":
            print("(Type 'CLEAR' to clear volunteer list)")
            print()
            loadCoinCount()
        if user_response == "CLEAR":
            clearCoinCount()
        if user_response == "HELP":
            readFromInstructions()
        if user_response == "EXIT":
            sys.exit(
                "Thank you for using the Coin Counter App! We appreciate your hard work in counting all the coins.")


# todo: make sure you get this explained
if __name__ == "__main__":
    main()


"""

first volunteer gets added
volunteer data gets stored in CoinCount.txt
asks if they want to add another volunteer
if they do:
    another volunteer gets added
    volunteer data gets stored in CoinCount.txt
if they don't:
    list displays 
    volunteer data gets stored in CoinCount.txt


steps:
handling the writing of one volunteer to coin count

handling the writing of >= 2 volunteers to coin count (or adding another volunteer to coin count)

handling updating an already existing volunteer


if volunteer's info was previously stored:

extract their info from volunteer_list and add it to current_volunteer_info
modify current volunteer info
DONT append current volunteer info to volunteer list
"""

# @! Asking the user


# todo: fix bug that doesn't allow the name to be shown when the same user comes back
# todo: perfect statements
# todo: if user should type in "BACK", they go back to the instructions
