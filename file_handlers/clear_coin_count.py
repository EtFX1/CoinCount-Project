"""Clears the contents of coinCount.txt with user's permission"""
#! Function to delete the contents of coinCount.txt


def clearCoinCount(volunteer_list):
    while True:
        response = input(
            "Are you sure you want to clear the volunteer list? (Type a 'Yes' or 'No'): ").strip().title()

        # * deletes the data in CoinCount.txt if the user confirms it
        if response == "Yes":
            with open("stored_data/CoinCount.txt", "r+", encoding="utf-8") as file_handler:
                volunteer_list.clear()
                file_handler.truncate(0)
                print()
                print("Coin Count Cleared")
                break

        # * goes back to the options if the user doesn't want to delete the data in coin count.txt
        elif response == "No":
            print()
            break
        else:
            print("Please type in a 'Yes' or 'No'")
            print()
            continue

    return
