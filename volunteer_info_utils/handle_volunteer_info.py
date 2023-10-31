"""Loads CoinCount.txt"""

from pprint import pprint

from collections import OrderedDict

from file_handlers.load_coin_count import loadCoinCount

from file_handlers.update_coin_count import updateCoinCount

from volunteer_info_utils.update_info import appendVolunteerName, appendBagsCountedCorrectly, appendNumberOfBagsCounted, appendVolunteerAccuracy, appendCurrentVolunteerInfo

from volunteer_info_utils.extra_functions import viewBagsChecked, sortBy

from stored_data.coin_info_list import coins_data


def handleVolunteerInfo(volunteer_list):

    print()

    print("Previously Stored Data:")
    print()
    # * text file that stores all the user's information
    loadCoinCount()

    # print(volunteer_list)

    # * stores the current volunteer's information
    current_volunteer_info = OrderedDict({})

    # @! Handling the VOLUNTEER'S NAME

    def handleNameInput():
        #! Collection of volunteer name input
        while True:

            # * collecting the volunteer’s name input
            # todo: ignore the spaces the user types
            user_input = input(
                "Input volunteer name (first names only): ").title().strip()

            # * verifying that the user types in letters not numbers
            if not user_input.isalpha():
                print()
                print("Name invalid. Try:")
                print("Typing in a name with letters | Typing in only a first name")
                print()
                continue
            else:
                print("Name accepted.")
                print()
                break

        # * calling function that appends volunteer name to current_volunteer_info
        appendVolunteerName(
            current_volunteer_info, volunteer_list, user_input)

        return user_input

    #! calling handleNameInput()
    volunteer_name_input = handleNameInput()

    # print(current_volunteer_info)

    # @! Handling the COIN TYPE INPUT

    def handleCoinTypeInput():

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
                the_type = coin_data["Coin Type (£)"]
                the_value = coin_data["Bag Value (£)"]
                the_weight = coin_data["Coin Weight (g)"]

                # * checking if "coin_type_input" is found in "coin_info_list"
                if coin_type_input == the_type:
                    print("Coin type valid")
                    print()

                    print(
                        f"Information about the coin you picked (£{(the_type)}):")
                    print()

                    pprint(coin_data, width=1)
                    print()

                    break

            # * checking if the coin type is not found in "coins_info_list"
            else:
                print("Coin type is invalid. Please try again")
                print()
                continue

            # ? returns these variables for use outside the function
            return the_type, the_value, the_weight

    # ? redefining and storing the returned variables so that they can be globally accessed in the program [converting local to global variables]
    coin_type, bag_value, coin_weight = handleCoinTypeInput()

    # @! Handling the BAG WEIGHT INPUT

    # * Initialising counter variables to 0 (in a dictionary)

    bag_weight_variables = {
        "Number of Bags Counted": 0,
        "Bags Value Counter": 0,
        "Bags Counted Correctly": 0
    }

    #! Calculating how many coins to be added or removed to correct an inaccurate bag weight

    def handleBagWeightInput(coin_type, bag_value, coin_weight):

        # @! Calculating the correct bag weight

        number_of_coins_in_the_bag = bag_value / coin_type
        bag_weight = (number_of_coins_in_the_bag) * coin_weight

        # @! Collecting and verifying bag weight input

        # * storing the key-values from the "bag_weight_variables" dictionary in variables for easier access

        bags_counted = bag_weight_variables["Number of Bags Counted"]
        bags_value_counter = bag_weight_variables["Bags Value Counter"]
        bags_counted_correctly = bag_weight_variables["Bags Counted Correctly"]

        incorrect_weight_inputs = 0

        # * Collecting bag weight input
        while True:

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
                print("Bag Weighed Incorrectly 😬")
                print()

                print(f"However, you are {surplus_bag_weight}g over the correct bag weight. You should remove {
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
                print("Bag Weighed Incorrectly 😬")
                print()

                print(f"However, you are {deficit_bag_weight}g under the correct bag weight. You should add {
                    round(coins_to_add, 1)} more £{coin_type} coins (approx)")

                print("Type in the correct bag weight")
                print()
                continue

            # * checks if the user has made any errors
            if incorrect_weight_inputs >= 1:

                # * Appending the "bags_counted_correctly" variable to "current_volunteer_info" dictionary
                appendBagsCountedCorrectly(
                    current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly)

            # * Comes here if has entered the correct bag weight
            else:
                bags_counted_correctly += 1

                # * Updating the "Bags Counted Correctly" key in the "bag_weight_variables" dictionary
                # ? (to ensure it wont be set back to 0) when the function is called again

                bag_weight_variables["Bags Counted Correctly"] = bags_counted_correctly

                # * Appending the "bags_counted_correctly" variable to "current_volunteer_info" dictionary
                appendBagsCountedCorrectly(
                    current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly)

            # * Updating the "Number of Bags Counted" key in the "bag_weight_variables" dictionary
            bags_counted += 1
            bag_weight_variables["Number of Bags Counted"] = bags_counted

            # * Appending the "bags_counted" variable to "current_volunteer_info" dictionary
            appendNumberOfBagsCounted(
                current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted)

            # * Updating the "Bags Value Counter" key in the "bag_weight_variables" dictionary
            bags_value_counter += bag_value

            bag_weight_variables["Bags Value Counter"] = bags_value_counter

            print("You have entered the correct bag weight")
            print()

            break

        # ? returns these variables for use outside the function
        return bags_value_counter, bags_counted_correctly, bags_counted

    # ? redefining and storing the returned variables so that they can be globally accessed in the program [converting local to global variables]
    bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
        coin_type, bag_value, coin_weight)

    # *  Calling function that Asks the user if they want to see the number of bags checked (and their total value)
    viewBagsChecked(bags_value_counter, bags_counted)

    # pprint(current_volunteer_info, indent=1)

    # @! Asking the user if they want to weigh another bag

    def weighAnotherBag(bags_value_counter, bags_counted, bags_counted_correctly):

        # print()

        while True:
            #! Collecting user input

            user_response = input(
                "Do you want to weigh another bag? (Type a 'Yes' or 'No'): ").title().strip()

            #! Collecting user input for coin type and bag weight again if the user wants to weigh another bag

            if user_response == "Yes":
                print()
                coin_type, bag_value, coin_weight = handleCoinTypeInput()

                # ? [ passing the new variables for coin_type, bag_value, coin_weight explicitly to handleBagWeightInput(), because by default functions access and modify global variables, and the variables above aren't changed globally]
                bags_value_counter, bags_counted_correctly, bags_counted = handleBagWeightInput(
                    coin_type, bag_value, coin_weight)

                # *  Calling function that Asks the user if they want to see the number of bags checked (and their total value)
                viewBagsChecked(bags_value_counter, bags_counted)
                continue

            #! Exiting loop if user doesn't want to weigh another bag
            elif user_response == "No":
                print("Moving on")
                print()
                break
            else:
                print("Please type in 'Yes' or 'No'")
                print()
                continue

        return bags_value_counter, bags_counted, bags_counted_correctly

    # ? storing the return values in variables, so that they can be accessible in every function within the program
    bags_value_counter, bags_counted, bags_counted_correctly = weighAnotherBag(
        bags_value_counter, bags_counted, bags_counted_correctly)

    print("next function")

    # @! Handling user accuracy

    def handleUserAccuracy():

        # @! Calculating the user accuracy

        # todo: bug: when the user gets it wrong the first time, and right the second time, volunteer accuracy = 0% instead of 50%

        volunteer_accuracy = round(bags_counted_correctly / bags_counted * 100)

        #! Appending the "Volunteer Accuracy (%)" key to the "current_volunteer_info" dictionary
        appendVolunteerAccuracy(
            current_volunteer_info, volunteer_name_input, volunteer_list, volunteer_accuracy)

        #! Updating the volunteer list with the newest volunteer, to get it ready for sorting
        appendCurrentVolunteerInfo(volunteer_name_input,
                                   volunteer_list, current_volunteer_info)

        #! Sorting the volunteer list in descending order

        # * the key is the "sortBy" function, which specifies that the criteria to sort out the list is with the "Volunteer Accuracy (%) key"

        volunteer_list.sort(key=sortBy, reverse=True)

        return volunteer_accuracy

    handleUserAccuracy()

    # print("Final Volunteer List:")
    # pprint(volunteer_list, indent=4)

    updateCoinCount(volunteer_list)

    return volunteer_list
