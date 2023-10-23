#! Reading from CoinCount.txt
# * """Updates CoinCount.txt with the contents of volunteer_list """

def updateCoinCount(volunteer_list):
    with open("CoinCount.txt", "a", encoding="utf-8") as file_handler:

        # * .read() method reads out the contents of "CoinCount.txt"

        dict_str = str(volunteer_list)
        contents = file_handler.write(dict_str + "\n")
        return (contents)
