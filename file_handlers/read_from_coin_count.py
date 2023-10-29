"""copies the contents of "CoinCount.txt" to the "volunteer_list" list (only if CoinCount.txt is not empty)"""
import os
import json


def readFromCoinCount():
    volunteer_list = []

    # Check if the file exists and is not empty
    if os.path.exists("stored_data/CoinCount.txt") and os.path.getsize("stored_data/CoinCount.txt") > 0:
        # Open the file in read mode
        with open("stored_data/CoinCount.txt", "r", encoding="utf-8") as file:
            volunteer_list = json.load(file)
    else:
        print("No data has been input yet")

    return volunteer_list
