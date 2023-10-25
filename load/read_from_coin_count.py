import os
import json

# * copies the contents of "CoinCount.txt" to the "volunteer_list" list (CoinCount.txt is not empty)


def readFromCoinCount():
    volunteer_list = []

    # Check if the file exists and is not empty
    if os.path.exists("CoinCount.txt") and os.path.getsize("CoinCount.txt") > 0:
        # Open the file in read mode
        with open("CoinCount.txt", "r", encoding="utf-8") as file:
            volunteer_list = json.load(file)
    else:
        print("No data has been input yet")

    return volunteer_list
