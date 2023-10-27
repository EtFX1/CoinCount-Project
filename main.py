from handlers import handlers
from pprint import pprint
from collections import OrderedDict

print("jazz")

volunteer_list, current_volunteer_info = handlers()


def displayFinalList():

    current_volunteer_info = OrderedDict()

    while True:

        user_response = input(
            "Do you want see the final volunteer list sorted by accuracy in descending order? (Type a 'Yes' or 'No'): ").title().strip()

        #! checks if the user wants to see the final volunteer list or not
        if user_response == "Yes":
            print()
            return pprint(volunteer_list, indent=1)

        #! updating the coinCount.txt file if the user no longer wants to add any more volunteers
        elif user_response == "No":
            volunteer_list.append(current_volunteer_info)
            print("Thank you for using the coin counter app!")

            break

        else:
            print("Please type in 'Yes' or 'No'")
            print()
            continue

    # * Updating "CoinCount.txt" file
    return volunteer_list, current_volunteer_info


def addAnotherVolunteer():

    while True:
        user_response4 = input(
            "Do you want to add another volunteer? (Type a 'Yes' or 'No'): ").title().strip()
        if user_response4 == "Yes":
            handlers()
        elif user_response4 == "No":
            displayFinalList()
        else:
            print("Please type in 'Yes' or 'No'")
            continue


if __name__ == "__main__":
    addAnotherVolunteer()

displayFinalList()


"""
first volunteer gets added
volunteer data gets stored in CoinCount.txt
asks if they want to add another volunteer
if they do:
    another volunteer gets added
    volunteer data gets stored in CoinCount.txt
if they don't:
    list displays 
    volunteer data gets stored in CoinCount.txt


steps:
handling the writing of one volunteer to coin count

handling the writing of >= 2 volunteers to coin count (or adding another volunteer to coin count)

handling updating an already existing volunteer
"""

# @! Asking the user


# todo: fix bug that doesn't allow the name to be shown when the same user comes back
# todo: perfect statements
# todo: add an exit function
# todo: add an option to clear volunteer list
