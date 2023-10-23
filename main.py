"""Loads CoinCount.txt"""
from load.load_coin_count import loadCoinCount

from load.update_coin_count import updateCoinCount

from load.read_from_coin_count import readFromCoinCount

# * stores information about each coin
from stored.coin_info_list import coins_data

from volunteer_utils.append import appendVolunteerName

from volunteer_utils.append import appendBagsCountedCorrectly

from volunteer_utils.append import appendNumberOfBagsCounted

from volunteer_utils.append import appendVolunteerAccuracy

print("Welcome to the coin counter!")
print()

print("Previously Stored Data:")
# * text file that stores all the user's information
print(loadCoinCount())
print()

# todo: add the contents of CoinCount.txt to volunteer_list (in one of the functions)

# * stores volunteer's information


volunteer_list = readFromCoinCount()
print(volunteer_list)

# * stores the current volunteer's information
current_volunteer_info = {}
# todo: display nicely

# @! Handling the VOLUNTEER'S NAME


def handleNameInput():
    #! Collection of volunteer name input
    while True:

        # * collecting the volunteer’s name input
        # todo: ignore the spaces the user types
        volunteer_name_input = input("Input volunteer name: ").title().strip()

        # * verifying that the user types in letters not numbers
        if not volunteer_name_input.isalpha():
            print("Please type in an actual name, with letters!")
            print()
            continue
        print("Name accepted.")
        print()
        break

    # * calling function that appends volunteer name to current_volunteer_info
    return (appendVolunteerName(current_volunteer_info,
                                volunteer_list, volunteer_name_input))


#! calling handleNameInput()
volunteer_name_input = handleNameInput()


# @! Handling the COIN TYPE INPUT


def handleCoinTypeInput():
    print()
    #! Collection of coin type input

    while True:
        try:
            # * collecting the coin type name input
            coin_type_input = float(input("Input a coin type: £").strip())

        #! verification of coin type input data type

        # * checking if the coin type input is not a number
        except ValueError:
            print("Please type in a number")
            print()
            continue

        # * iterating over the dictionaries in "coins_info_list"
        for coin_data in coins_data:

            # * extracting and storing the coin type, bag value and coin Weight
            coin_type = coin_data["Coin Type (£)"]
            bag_value = coin_data["Bag Value (£)"]
            coin_weight = coin_data["Coin Weight (g)"]

            # * checking if "coin_type_input" is found in "coin_info_list"
            if coin_type_input == coin_type:
                print("Coin type valid")
                print()
                print("Information about the coin you picked:")
                print(coin_data)
                print()
                break

        # * checking if the coin type is not found in "coins_info_list"
        else:
            print("Coin type is invalid. Please try again")
            print()
            continue

        # ? returns these variables for use outside the function
        return coin_type, bag_value, coin_weight


# ? calling handleCoinTypeInput() [also setting function to the variables on the left so that they can be accessed in other parts of the program]
coin_type, bag_value, coin_weight = handleCoinTypeInput()


# @! Handling the BAG WEIGHT INPUT


# * Initialising counter variables to 0 (in a dictionary)

bag_weight_variables = {
    "Number of Bags Counted": 0,
    "Bags Value Counter": 0,
    "Bags Counted Correctly": 0
}

#! Calculating how many coins to be added or removed to correct an inaccurate bag weight
# ? passing as parameters all the (outside) variables that need to be accessed by the function


def handleBagWeightInput(coin_type, coin_weight, bag_value, current_volunteer_info):

    # @! Calculating the correct bag weight
    # ? passing as parameters all the (outside) variables that need to be accessed by the function

    number_of_coins_in_the_bag = bag_value / coin_type
    bag_weight = (number_of_coins_in_the_bag) * coin_weight
    # ? calling calcBagWeight() [also setting function to the "bag_weight" variable so that it can be accessed in other parts of the program

    # * storing the values from the "bag_weight_variables" dictionary in variables for easier access

    bags_counted = bag_weight_variables["Number of Bags Counted"]
    bags_value_counter = bag_weight_variables["Bags Value Counter"]
    bags_counted_correctly = bag_weight_variables["Bags Counted Correctly"]

    incorrect_weight_inputs = 0

    # @! Collecting and verifying bag weight input
    while True:

        # * Collecting bag weight input
        try:
            bag_weight_input = float(
                input(f"Input the bag weight for a £{coin_type} coin (g): ").strip())

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

            incorrect_weight_inputs += 1

            print(f"You are {surplus_bag_weight}g over the limit. You should remove {
                  round(coins_to_remove, 1)} more £{coin_type} coins (approx")

            print("Type in the correct bag weight")
            print()
            continue

        # * Checking if the user input a bag weight that's too small
        if bag_weight_input < bag_weight:

            # ? calculating number of coins that should be added
            deficit_bag_weight = bag_weight - bag_weight_input
            coins_to_add = deficit_bag_weight / coin_weight

            incorrect_weight_inputs += 1

            print(f"You are {deficit_bag_weight}g under the limit. You should add {
                  round(coins_to_add, 1)} more £{coin_type} coins (approx)")

            print("Type in the correct bag weight")
            print()
            continue

        # * checks if the user has made any errors
        if incorrect_weight_inputs >= 1:
            print(f"Number of bags counted incorrectly: {
                  incorrect_weight_inputs}")

            # * Appending the "bags_counted_correctly" variable to "current_volunteer_info" dictionary
            current_volunteer_info = appendBagsCountedCorrectly(
                current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly)

        # * Comes here if has entered the correct bag weight
        else:
            bags_counted_correctly += 1

            # * Updating the "Bags Counted Correctly" key in the "bag_weight_variables" dictionary
            # ? (to ensure it wont be set back to 0) when the function is called again

            bag_weight_variables["Bags Counted Correctly"] = bags_counted_correctly

            # * Appending the "bags_counted_correctly" variable to "current_volunteer_info" dictionary
            current_volunteer_info = appendBagsCountedCorrectly(
                current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly)

        # * Updating the "Number of Bags Counted" key in the "bag_weight_variables" dictionary
        bags_counted += 1
        bag_weight_variables["Number of Bags Counted"] = bags_counted

        # * Appending the "bags_counted" variable to "current_volunteer_info" dictionary
        current_volunteer_info = appendNumberOfBagsCounted(
            current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted)

        # * Updating the "Bags Value Counter" key in the "bag_weight_variables" dictionary
        bags_value_counter += bag_value

        bag_weight_variables["Bags Value Counter"] = bags_value_counter

        print("You have entered the correct bag weight")

        break

    # ? returns these variables for use outside the function
    return bags_value_counter, bags_counted_correctly, bags_counted


# ? calling handleBagWeight() function [setting function to the values on the left so that they can be accessed in other parts of the program]
bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
    coin_type, coin_weight, bag_value, current_volunteer_info)

print(current_volunteer_info)


# @! Asking the user if they want to weigh another bag

def weighAnotherBag(bags_counted, bags_value_counter):
    while True:
        user_response1 = input(
            "Do you want to weigh another bag? (Type a 'Yes' or 'No'): ").title().strip()

        if user_response1 == "Yes":
            print()
            coin_type, bag_value, coin_weight = handleCoinTypeInput()

            # * Calling the handleBagWeightInput function and capturing the return variables
            bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
                coin_type, coin_weight, bag_value, current_volunteer_info)

        elif user_response1 == "No":
            print("Moving on")
            print()
            break
        else:
            print("Please type in 'Yes' or 'No'")
            continue

    # @! Ask the user if they want to see the number of bags checked
    while True:
        user_response2 = input(
            "Do you want see the number of bags checked so far and their total value (Type a 'Yes' or 'No')?: ").title().strip()

        if user_response2 == "Yes":
            print()
            return (f"Number of bags checked: {
                bags_counted} | Total Value: £{bags_value_counter}")
        elif user_response2 == "No":
            return ("Moving on")
        else:
            print("Please type in 'Yes' or 'No'")
            continue


print(weighAnotherBag(bags_counted, bags_value_counter))


# @! Calculating the user accuracy

def handleUserAccuracy(current_volunteer_info):

    volunteer_accuracy = round(bags_counted_correctly / bags_counted * 100)

    #! Appending the "Volunteer Accuracy (%)" key to the "current_volunteer_info" dictionary
    current_volunteer_info = appendVolunteerAccuracy(
        current_volunteer_info, volunteer_name_input, volunteer_list, volunteer_accuracy)

    # @! Sorting the volunteer list in descending order

    def sortList():
        def sortBy(dictionary):

            return dictionary["Volunteer Accuracy (%)"]

        volunteer_list.sort(key=sortBy, reverse=True)

    print(sortList())


print(handleUserAccuracy(current_volunteer_info))

# @! Ask the user if they want to see the number of bags check


def addAnotherVolunteer():
    while True:
        user_response4 = input(
            "Do you want to add another volunteer? (Type a 'Yes' or 'No'): ").title().strip()
        if user_response4 == "Yes":
            print()
            print(handleNameInput())

            coin_type, bag_value, coin_weight = handleCoinTypeInput()

            bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
                coin_type, coin_weight, bag_value, current_volunteer_info)

            print(weighAnotherBag(bags_counted, bags_value_counter))

            print(handleUserAccuracy(current_volunteer_info))

            return (displayFinalList())

        elif user_response4 == "No":
            return ("Moving on")
        else:
            print("Please type in 'Yes' or 'No'")
            continue


def displayFinalList():
    while True:
        user_response3 = input(
            "Do you want see the final volunteer list sorted by accuracy in descending order? (Type a 'Yes' or 'No'): ").title().strip()
        if user_response3 == "Yes":
            print()

            # @! Adding the current_volunteer_info to the volunteer list

            volunteer_list.append(current_volunteer_info)
            print(volunteer_list)

            # @! Updating Coin count
            return (updateCoinCount(volunteer_list))
        elif user_response3 == "No":
            print("Bye for now!")
            break
        else:
            print("Please type in 'Yes' or 'No'")
            continue

    return (addAnotherVolunteer())


print(displayFinalList())
