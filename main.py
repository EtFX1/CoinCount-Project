"""modules"""

from pprint import pprint
import sys
from handlers import handlers
from file_handlers.read_from_instructions import readFromInstructions
from file_handlers.load_coin_count import loadCoinCount
from file_handlers.clear_coin_count import clearCoinCount


print()
print("Welcome to the coin counter!")
# @! Entry point to the application


def main():

    # * while that runs infinitely
    while True:

        print()

        # * prints out instructions
        readFromInstructions()
        print()

        valid_responses = ["ADD", "NEW", "DISPLAY",
                           "VIEW", "CLEAR", "HELP", "EXIT"]

        # * Getting user response

        user_response = input("> ").upper().strip()

        if user_response not in valid_responses:
            print("Please type in valid response")
            print()
            continue
        if user_response == "ADD" or user_response == "NEW":
            handlers()
        if user_response == "DISPLAY" or user_response == "VIEW":
            print("Clear to clear volunteer list")
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
