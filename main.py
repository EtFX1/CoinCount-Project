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


# @! Handling the BAG WEIGHT INPUT

#! Calculating how many coins to be added or removed to correct an inaccurate bag weight

bag_weight_variables = {
    "Bags Counted": 0,
    "Bags Value Counter": 0,
    "Incorrect Weight Inputs": 0,
    "Bags Counted Correctly": 0
}


def handleBagWeightInput(bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables):

    bags_counted = bag_weight_variables["Bags Counted"]
    bags_value_counter = bag_weight_variables["Bags Value Counter"]
    bags_counted_correctly = bag_weight_variables["Bags Counted Correctly"]
    incorrect_weight_inputs = bag_weight_variables["Incorrect Weight Inputs"]

    user_trying_again = 0

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
            user_trying_again += 1

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
            user_trying_again += 1

            print("Type in the correct bag weight")
            print()
            continue

        # * Comes here if has entered the correct bag weight

        if bag_weight_input == bag_weight:
            bags_counted += 1
            bags_counted_correctly += 1
            bags_value_counter += bag_value
        if user_trying_again >= 1:
            bags_counted_correctly = 0

        print("You have entered the correct bag weight")

        # Update the values in the bag_weight_variables dictionary (to ensure they wont be set back to 0)
        bag_weight_variables["Bags Counted"] = bags_counted
        bag_weight_variables["Bags Value Counter"] = bags_value_counter
        bag_weight_variables["Incorrect Weight Inputs"] = incorrect_weight_inputs
        print(f"Incorrect Weight Inputs: {incorrect_weight_inputs}")
        bag_weight_variables["Bags Counted Correctly"] = bags_counted_correctly

        # * Append the number of bags counted correctly to current_volunteer_info
        current_volunteer_info = appendBagsCountedCorrectly(
            current_volunteer_info, bags_counted_correctly)

        # * Append the total number of bags counted to current_volunteer_info
        current_volunteer_info = appendNumberOfBagsCounted(
            current_volunteer_info, bags_counted)

        print()
        break

    # * returns the counter variables for use outside the function
    return bags_value_counter, incorrect_weight_inputs, bags_counted_correctly, bags_counted


# * Calling the handleBagWeightInput function and capturing the return variables
bags_value_counter, bags_counted_incorrectly, bags_counted_correctly, bags_counted = handleBagWeightInput(
    bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables)


print(current_volunteer_info)
print()


# @! Asking the user if they want to weigh another bag
while True:
    user_response = input("Do you want to weigh another bag?: ").title()

    if user_response == "Yes":
        print()
        handleCoinTypeInput()

        # * Calling the handleBagWeightInput function and capturing the return variables

        bags_value_counter, bags_counted_incorrectly, bags_counted_correctly, bags_counted = handleBagWeightInput(
            bag_weight, coin_type, coin_weight, bag_value, current_volunteer_info, bag_weight_variables)

        print(current_volunteer_info)

    if user_response == "No":
        print("Moving on")
        break
    else:
        print("Please type in 'Yes' or 'No'")
        continue

print("")
