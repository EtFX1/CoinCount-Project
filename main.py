"""Loads CoinCount.txt"""
from load.load_coin_count import loadCoinCount

# * stores information about each coin
from stored.coin_info_list import coin_info_list

from volunteer_utils.append import appendVolunteerName

from volunteer_utils.append import appendBagsCountedCorrectly

from volunteer_utils.append import appendNumberOfBagsCounted

print("Print a welcome message later")
print()

# * text file that stores all the user's information
print(loadCoinCount())
print()

# * stores volunteer's information
volunteer_list = []

# * stores the current volunteer's information
current_volunteer_info = {}
# todo: display nicely


# @! Handling the VOLUNTEER'S NAME

#! Collection of volunteer name input
while True:

    # * collecting the volunteer’s name input
    # todo: ignore the spaces the user types
    volunteer_name_input = input("Input volunteer name: ").title()

    # * verifying that the user types in letters not numbers
    if not volunteer_name_input.isalpha():
        print("Please type in an actual name, with letters!")
        print()
        continue
    print("Name accepted.")
    print()
    break


# * calling function that appends volunteer name to current_volunteer_info
print(appendVolunteerName(current_volunteer_info,
      volunteer_list, volunteer_name_input))
print()

# @! Handling the COIN TYPE INPUT

#! Collection of coin type input


def handleCoinTypeInput():
    while True:
        try:
            # * collecting the coin type name input
            coin_type_input = float(input("Input a coin type: £"))

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
                print()
                break

        # * checking if the coin type is not found in "coins_info_list"
        else:
            print("Coin type is invalid. Please try again")
            print()
            continue

        return coin_type, bag_value, coin_weight


coin_type, bag_value, coin_weight = handleCoinTypeInput()


# @! Calculating the correct bag weight
number_of_coins_in_the_bag = bag_value / coin_type
bag_weight = (number_of_coins_in_the_bag) * coin_weight


# @! Calculating the correct bag weight
number_of_coins_in_the_bag = bag_value / coin_type
bag_weight = (number_of_coins_in_the_bag) * coin_weight


# @! Handling the BAG WEIGHT INPUT

#! Calculating how many coins to be added or removed to correct an inaccurate bag weight

# * Initialising counter variables to 0 (in a dictionary)

bag_weight_variables = {
    "Number of Bags Counted": 0,
    "Bags Value Counter": 0,
    "Bags Counted Correctly": 0
}

# ? as parameters we are passing all the values that need to be accessed by the function


def handleBagWeightInput(bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables):

    # * storing the values from the "bag_weight_variables" dictionary in variables for easier access

    bags_counted = bag_weight_variables["Number of Bags Counted"]
    bags_value_counter = bag_weight_variables["Bags Value Counter"]
    bags_counted_correctly = bag_weight_variables["Bags Counted Correctly"]

    incorrect_weight_inputs = 0

    # @! Collect and verify bag weight input
    while True:

        # * Collecting bag weight input
        try:
            bag_weight_input = float(
                input(f"Input the bag weight for £{coin_type} (g): "))

        # * verifying the data type of bag weight input
        except ValueError:
            print("Please type in a number")
            print()
            continue

        # * Input is valid (a number)
        print("Bag Weight Accepted")
        print()

        # * Checking if the user input a bag weight that's too large
        if bag_weight_input > bag_weight:

            # ? calculating number of coins that should be removed
            surplus_bag_weight = bag_weight_input - bag_weight
            coins_to_remove = surplus_bag_weight / coin_weight

            print(f"You are {surplus_bag_weight}g over the limit. You should remove {
                  round(coins_to_remove, 1)} £{coin_type} coins (approx")

            incorrect_weight_inputs += 1

            print("Type in the correct bag weight")
            print()
            continue

        # * Checking if the user input a bag weight that's too small
        if bag_weight_input < bag_weight:

            # ? calculating number of coins that should be added
            deficit_bag_weight = bag_weight - bag_weight_input
            coins_to_add = deficit_bag_weight / coin_weight

            print(f"You are {deficit_bag_weight}g under the limit. You should add {
                  round(coins_to_add, 1)} £{coin_type} coins (approx)")

            incorrect_weight_inputs += 1

            print("Type in the correct bag weight")
            print()
            continue

        # * checks if the user has made any errors
        if incorrect_weight_inputs >= 1:
            bags_counted_correctly = 0

        # * Comes here if has entered the correct bag weight
        else:
            bags_counted_correctly += 1

            # * Updating the "Bags Counted Correctly" key in the "bag_weight_variables" dictionary
            # ? (to ensure it wont be set back to 0) when the function is called again

            bag_weight_variables["Bags Counted Correctly"] = bags_counted_correctly

            # * Appending the "bags_counted_correctly" variable to "current_volunteer_info" dictionary
            current_volunteer_info = appendBagsCountedCorrectly(
                current_volunteer_info, bags_counted_correctly)

        # * Updating the "Number of Bags Counted" key in the "bag_weight_variables" dictionary
        bags_counted += 1
        bag_weight_variables["Number of Bags Counted"] = bags_counted

        # * Appending the "bags_counted" variable to "current_volunteer_info" dictionary
        current_volunteer_info = appendNumberOfBagsCounted(
            current_volunteer_info, bags_counted)

        # * Updating the "Bags Value Counter" key in the "bag_weight_variables" dictionary
        bags_value_counter += bag_value
        bag_weight_variables["Bags Value Counter"] = bags_value_counter

        print("You have entered the correct bag weight")

        break

    # * returns the counter variables for use outside the function
    return bags_value_counter, bags_counted_correctly, bags_counted


# * Calling the handleBagWeightInput function and capturing (utilising) the return variables
bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
    bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables)


print(current_volunteer_info)
# print()


# @! Asking the user if they want to weigh another bag
while True:
    user_response = input("Do you want to weigh another bag?: ").title()

    if user_response == "Yes":
        print()
        coin_type, bag_value, coin_weight = handleCoinTypeInput()
        # * Calling the handleBagWeightInput function and capturing the return variables

        bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
            bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables)

        print(current_volunteer_info)

    elif user_response == "No":
        print("Moving on")
        break
    else:
        print("Please type in 'Yes' or 'No'")
        continue

# @! Update the running total of the bag's values`
