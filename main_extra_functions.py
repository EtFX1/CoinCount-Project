from volunteer_info_utils.handle_volunteer_info import handleVolunteerInfo

from file_handlers.update_coin_count import updateCoinCount

from file_handlers.read_from_coin_count import readFromCoinCount


# * data structure to hold all volunteer's information, which is stored in readFromCoinCount()


volunteer_list = readFromCoinCount()
print(len(volunteer_list))


def addVolunteer():

    if len(volunteer_list) == 6:
        print("Volunteer list is full. (Type 'EXIT' to exit the application)")
    else:
        handleVolunteerInfo(volunteer_list)


def deleteVolunteerInfo():

    volunteer_list_copy = volunteer_list[:]

    while True:
        response = input(
            "Which volunteer's information would you like to delete?: ").title()

        for volunteer_info in volunteer_list_copy:
            volunteer_name = volunteer_info["Volunteer Name"]

            if response == volunteer_name:
                volunteer_list.remove(volunteer_info)
                print()
                updateCoinCount(volunteer_list)
                break

        if response != volunteer_name:
            print("Please type in a name that is in the list")
            print()
            continue

        return volunteer_list
