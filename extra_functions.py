
# from coin_count_handlers.update_coin_count import updateCoinCount


#! Function to give the user to the option to see the number of bags checked so far


def viewBagsChecked(bags_value_counter, bags_counted):
    # @! Ask the user if they want to see the number of bags checked (and their total value)
    while True:
        user_response2 = input(
            "Do you want see the number of bags checked so far and their total value (Type a 'Yes' or 'No')?: ").title().strip()

        if user_response2 == "Yes":
            print()
            print(f"Number of bags checked: {
                bags_counted} | Total Value: £{bags_value_counter}")
        elif user_response2 == "No":
            print("Moving on")
        else:
            print("Please type in 'Yes' or 'No'")
            continue

        return bags_counted, bags_value_counter


#! function to specify the criteria with which to sort the list
def sortBy(dictionary):

    # * the criteria we want to sort with is "Volunteer Accuracy"
    return dictionary["Volunteer Accuracy (%)"]

# @! Ask the user if they want to see the final list of volunteers
