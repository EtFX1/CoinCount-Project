import os


#! Reading from CoinCount.txt
# * """CoinCount.txt contains all user data """

def loadCoinCount():
    with open("CoinCount.txt", "r", encoding="utf-8") as file_handler:

        # * checking if the ".st.size" property of the os.stat() method == 0. If it is, then print "No information has been added yet"
        if os.stat("CoinCount.txt").st_size == 0:
            return ("No data has been input yet")
        else:
            # * .read() method reads out the contents of "CoinCount.txt"
            contents = file_handler.read()
            return (contents)
