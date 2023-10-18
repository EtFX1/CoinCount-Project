""" Loads up the coinCount.txt file"""
from loadCoinCount import loadCoinCount

print("Print a welcome message later")
print()

print(loadCoinCount())
print()


# * stores all of the volunteers' information
# todo: store in a separate module
volunteer_list = [
]

# * stores the current volunteer's information ("Volunteer Name", "Total Bags Weighed", "Number of bags counter correctly")
current_volunteer_info = {}

# * stores the information for each type of coin
coin_info_list = [
    {
        "Coin Type (£)": 0.01,
        "Bag Value (£)": 1,
        "Coin Weight (g)": 3.56
    },
    {
        "Coin Type (£)": 0.02,
        "Bag Value (£)": 1,
        "Coin Weight (g)": 7.12
    },
    {
        "Coin Type (£)": 0.05,
        "Bag Value (£)": 5,
        "Coin Weight (g)": 2.35
    },
    {
        "Coin Type (£)": 0.10,
        "Bag Value (£)": 5,
        "Coin Weight (g)": 6.50
    },
    {
        "Coin Type (£)": 0.20,
        "Bag Value (£)": 10,
        "Coin Weight (g)": 5.00
    },
    {
        "Coin Type (£)": 0.50,
        "Bag Value (£)": 10,
        "Coin Weight (g)": 8.00
    },
    {
        "Coin Type (£)": 1,
        "Bag Value (£)": 20,
        "Coin Weight (g)": 8.75
    },
    {
        "Coin Type (£)": 2,
        "Bag Value (£)": 20,
        "Coin Weight (g)": 12
    }
]

#!Initialising counter variables to 0

# * stores the running total of the VALUE of bags weighed

bags_value_counter = 0

# * stores the running total of the NUMBER of bags weighed
bags_weighed_counter = 0

# * stores the running total of the NUMBER of bags weighed INCORRECTLY
bags_weighed_incorrectly = 0

# * stores the running total of the NUMBER of bags Counted CORRECTLY
bags_weighed_correctly = 0


# @! Handling the VOLUNTEER'S NAME

#! Collection of volunteer name input
while True:

    # * collecting the volunteer’s name input
    volunteer_name_input = input("Input volunteer name: ").title()

    #! Collection of volunteer name input's data type

    # * verifying that the user types in letters not numbers
    if not volunteer_name_input.isalpha():
        print("Please type in an actual name, with letters!")
        print()
        continue
    print("Name accepted.")
    print()
    break

#! Appending the volunteer's name to current_volunteer_information
# * checking if volunteer list is empty
# ? ("[] is a falsy value, so not turns [] to true)
if not volunteer_list:

    # * creating a dictionary to store information for a new user
    current_volunteer_info.update({"Volunteer Name": volunteer_name_input})
    print(f"Hello {volunteer_name_input}!")
    print()

# * if volunteer_list is not empty
else:

    #
    # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
    for volunteer_info in volunteer_list:

        # * extracting the volunteer's name key-value from each dictionary
        volunteer_name = volunteer_info["Volunteer Name"]

        # ? checking if the previously stored volunteer name matches the current volunteer name input
        if volunteer_name == volunteer_name_input:

            # * greeting the user and showing them their previously stored data
            print(f"Welcome back {volunteer_name}! Here is your previous data")
            current_volunteer_info = volunteer_info
            break

        # ? runs if "volunteer_name_input" is NOT found in volunteer
        else:

            # * creating a dictionary to store information for a new user
            current_volunteer_info["Volunteer Name"] = volunteer_name_input

print(current_volunteer_info)
print()

# @! Handling the COIN TYPE INPUT

#! Collection of coin type input

while True:
    try:
        # * collecting the coin type name input
        coin_type_input = float(input("Input a coin type: "))

    #! verification of coin type input data type

    # * checking if the coin type input is not a number
    except ValueError:
        print("Please type in a number")
        print()
        continue

    # * iterating over the dictionaries in "coins_info_list"
    for coin_info in coin_info_list:

        # * extracting and storing the coin type, bag value and coin Weight
        coin_type = coin_info["Coin Type (£)"]
        bag_value = coin_info["Bag Value (£)"]
        coin_weight = coin_info["Coin Weight (g)"]

        # * checking if "coin_type_input" is found in "coin_info_list"
        if coin_type_input == coin_type:
            print("Coin type valid")
            print()
            print("Information about the coin you picked:")
            print(coin_info)
            break

    # * checking if the coin type is not found in "coins_info_list"
    else:
        print("Coin type is invalid. Please try again")
        print()
        continue
    break

print()

# @! Handling the BAG WEIGHT INPUT


#! Collection and verification of data type

while True:
    try:
        # * collecting the bag weight name input
        bag_weight_input = float(
            input(f"Input the bag weight for £{coin_type}: "))
        bags_weighed_counter += 1

    # * checking if the bag weight input is not a number
    except ValueError:
        print("Please type in a number")
        print()

    # * if the input is valid (if its a number, then print confirmation message)
    else:
        print("Bag Weight collected")
        print()
        break

#! Appending the total number of bags weighed to current_volunteer_info

# * checking if "Total Bags Weighed" key is in "current_volunteer_info" (means that it has been previously stored)
if "Total Bags Weighed" in current_volunteer_info:

    # ? we update the old "Total Bags Weighed" key value
    # * assigning the "bags_weighed_counter" value to the "Total Bags Weighed"
    current_volunteer_info["Total Bags Weighed"] = bags_weighed_counter
    print("updated")

# * checking if "Total Bags Weighed" key is not in "current_volunteer_info" (means that it has been previously stored)
else:

    # ? we create a "Total Bags Weighed" key value
    current_volunteer_info.update({"Total Bags Weighed": bags_weighed_counter})

print(current_volunteer_info)
print()


#! Calculating the correct bag weight
number_of_coins_in_the_bag = bag_value / coin_type
bag_weight = (number_of_coins_in_the_bag) * coin_weight

print(bag_weight)

#! Calculating how many coins to be added or removed to correct an inaccurate bag weight

# * checking if the user input a bag weight that's too large
if bag_weight_input > bag_weight:

    # * calculation of the coins to be added
    surplus_bag_weight = (bag_weight_input - bag_weight)
    coins_to_remove = surplus_bag_weight / coin_weight

    print(f"{surplus_bag_weight}g")

    print(f"You should remove {round(coins_to_remove)} coins (approx)")
    bags_weighed_incorrectly += 1

# * checking if the user input a bag weight that's too small

elif bag_weight_input < bag_weight:

    # * calculation of the coins to be to be removed

    deficit_bag_weight = (bag_weight - bag_weight_input)
    coins_to_add = deficit_bag_weight / coin_weight

    print(f"{deficit_bag_weight}g")
    print(f"You should add {round(coins_to_add)} coins (approx)")
    bags_weighed_incorrectly += 1

# * if the user has a correct bag weight
else:
    bags_weighed_correctly += 1
    print("You have entered the correct bag weight")
    print()
#! Appending the bag weight input to current_volunteer_info

# * checking if "Bags Counted Correctly" key is in "current_volunteer_info" (means that it has been previously stored)
if "Bags Counted Correctly" in current_volunteer_info:

    # ? we update the old "Bags Counted Correctly" key value
    # * assigning the "bags_weighed_counter" value to the "Total Bags Weighed"
    current_volunteer_info["Bags Counted Correctly"] = bags_weighed_correctly

# * checking if "Bags Counted Correctly" key is not in "current_volunteer_info" (means that it has been previously stored)
else:

    # ? we create a "Bags Counted Correctly" key value
    current_volunteer_info.update(
        {"Bags Counted Correctly": bags_weighed_correctly})

print(current_volunteer_info)
print()
