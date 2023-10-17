""" Loads up the coinCount.txt file"""
from loadCoinCount import loadCoinCount

print("Print a welcome message later")
print()

print(loadCoinCount())
print()


# * stores all of the volunteers' information
# todo: store in a separate module
volunteer_list = []

# * stores the current volunteer's information
current_volunteer_info = []

# * stores the information for each type of coin
coins_information = [
    {
        "Coin Type (£)": 2,
        "Bag Value (£)": 20,
        "Coin weight (g)": 12
    },
    {
        "Coin Type (£)": 1,
        "Bag Value (£)": 20,
        "Coin weight (g)": 8.75
    },
    {
        "Coin Type (£)": 0.50,
        "Bag Value (£)": 10,
        "Coin weight (g)": 8.00
    },
    {
        "Coin Type (£)": 0.20,
        "Bag Value (£)": 10,
        "Coin weight (g)": 5.00
    },
    {
        "Coin Type (£)": 0.10,
        "Bag Value (£)": 5,
        "Coin weight (g)": 6.50
    },
    {
        "Coin Type (£)": 0.05,
        "Bag Value (£)": 5,
        "Coin weight (g)": 2.35
    },
    {
        "Coin Type (£)": 0.02,
        "Bag Value (£)": 1,
        "Coin weight (g)": 7.12
    },
    {
        "Coin Type (£)": 0.50,
        "Bag Value (£)": 1,
        "Coin weight (g)": 3.56
    }
]

#!Initialising counter variables to 0

# * stores the running total of the VALUE of bags weighed
bags_value_counter = 0

# * stores the running total of the NUMBER of bags weighed
bags_weighed = 0

# * stores the running total of the NUMBER of bags weighed INCORRECTLY
bags_weighed_incorrectly = 0

# * stores the running total of the NUMBER of bags weighed CORRECTLY
bags_weighed_correctly = 0


# @! Handling the VOLUNTEER'S NAME

#! Collection and verification of data type
while True:

    # * collecting the volunteer’s name input
    volunteer_name_input = input("Input volunteer name: ").title()

    # * verifying that the user types in letters not numbers
    if not volunteer_name_input.isalpha():
        print("Please type in an actual name, with letters!")
        print()
        continue
    print("Name accepted.")
    print()
    break

# * checking if volunteer list is empty
# ? ("[] is a falsy value, so not turns [] to true)
if not volunteer_list:

    # * creating a dictionary to store information for a new user
    current_volunteer_info.append({"Volunteer Name": volunteer_name_input})
    print(f"Hello {volunteer_name_input}!")
    print()

# * if volunteer_list is not empty
else:

    # * iterates over each dictionary in "volunteer_list"
    for volunteer_info in volunteer_list:

        # * volunteer's name
        volunteer_name = volunteer_info["Volunteer Name"]

        # * checking if the user's name was previously stored in "volunteer_list"
        if volunteer_name_input == volunteer_name:

            # * if the user's name is found in volunteer_list, then we add their information (volunteer_info) to the "current_volunteer_info" list
            current_volunteer_info.append(volunteer_info)
            print(f"Welcome back {volunteer_name}! Here is your old data")
            print(volunteer_info)
        else:

            # * if their name wasn't previously stored, then they are a new user, so we create a new dictionary to store their information
            current_volunteer_info.append(
                {"Volunteer Name": volunteer_name_input})

            print(f"Hello {volunteer_name_input}!")

            break


# @! Handling the COIN TYPE INPUT

#! Collection and verification of data type

while True:
    try:
        # * collecting the coin type name input
        coin_type_input = float(input("Input a coin type: "))

    # * checking if the coin type input is not a number
    except ValueError:
        print("Please type in a number")
        print()

    else:
        print("Coin type collected")
        print()
        break

# * checking if "coin_type_input" is found in "coins_information"
for coin_info in coins_information:
    coin_type = (coin_info["Coin Type (£)"])

    if coin_type_input == coin_type:
        print("Coin type valid")
        print()
        print(coin_info)
        break
else:
    print("invalid")
