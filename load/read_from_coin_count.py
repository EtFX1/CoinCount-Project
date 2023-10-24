import os
import json


def readFromCoinCount():
    volunteer_list = []

    # Check if the file exists and is not empty
    if os.path.exists("CoinCount.txt") and os.path.getsize("CoinCount.txt") > 0:
        # Open the file in read mode
        with open("CoinCount.txt", "r", encoding="utf-8") as file:
            volunteer_list = json.load(file)
    else:
        print("no data has been input yet")

    return volunteer_list
