"""Updates CoinCount.txt with the contents of volunteer_list """
import json


def updateCoinCount(volunteer_list):
    with open("stored_data/CoinCount.txt", "w", encoding="utf-8") as file_handler:

        # * .read() method reads out the contents of "CoinCount.txt"

        json.dump(volunteer_list, file_handler, indent=4)
        contents = file_handler.write("\n")
        print("CoinCount.txt updated")
        print()
        return (contents)
