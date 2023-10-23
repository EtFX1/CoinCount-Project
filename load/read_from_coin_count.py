import os
# * reads the contents of CoinCount.txt into the volunteer list


def readFromCoinCount():
    # Open the file in read mode
    with open("CoinCount.txt", "r", encoding="utf-8") as file:

        # ? checking if the "CoinCount.txt" is empty
        # * checking if the ".st.size" property of the os.stat() method == 0. If it is, then print "No information has been added yet"
        if os.stat("CoinCount.txt").st_size == 0:

            volunteer_list = []
            return volunteer_list

        else:

            # Read each line (each line is a string representation of a volunteer_list)
            for line in file:
                # Convert the string representation of the volunteer_list to a volunteer_list
                dict_entry = eval(line.strip())  # Use eval with caution

                # Append the volunteer_list to the list
                volunteer_list = (dict_entry)

            return volunteer_list
