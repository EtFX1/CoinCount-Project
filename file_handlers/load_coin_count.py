"""Loads (displays) CoinCount.txt"""
import os


def loadCoinCount():
    with open("stored_data/CoinCount.txt", "r", encoding="utf-8") as file_handler:

        # ? checking if the "CoinCount.txt" is empty
        # * checking if the ".st.size" property of the os.stat() method == 0. If it is, then print "No information has been added yet"
        if os.stat("stored_data/CoinCount.txt").st_size == 0:
            print("No data in CoinCount.txt")
        # * .read() method reads out the contents of "CoinCount.txt"
        contents = file_handler.read()
        print(contents)
        return (contents)
