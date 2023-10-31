""" Functions that update data structures with volunteer's information"""

from pprint import pprint

# @! Function to update the "Volunteer Name" key-value


def appendVolunteerName(current_volunteer_info, volunteer_list, volunteer_name_input):

    # ! code that runs if volunteer list is empty
    # ? ("[] is a falsy value, so not turns [] to true)
    if not volunteer_list:
        print()

        # * creating a dictionary to store information for a new user
        current_volunteer_info.update({"Volunteer Name": volunteer_name_input})
        print(f"Hello {volunteer_name_input}!")
        print()

    #!Updating the user's data in "current_volunteer_info" and "volunteer_info" if the data has been previously stored
    else:

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for i, volunteer_info in enumerate(volunteer_list, 1):
            volunteer_count = i

            # * extracting the volunteer's name key-value from each dictionary
            volunteer_name = volunteer_info["Volunteer Name"]

            # ? checking if the previously stored volunteer name matches the current volunteer name input
            if volunteer_name == volunteer_name_input:

                # * greeting the user and showing them their previously stored data
                print(
                    f"Welcome back {volunteer_name}! You are volunteer {volunteer_count}. Here is your previous data:")
                print()
                pprint(volunteer_info, indent=1)

                # * updating current volunteer's name with the value of "Volunteer Name"
                current_volunteer_info["Volunteer Name"] = volunteer_name

                # * setting the "volunteer_info" in "current_volunteer_info"
                current_volunteer_info = volunteer_info
                print()

                break

        else:
            print(f"Hello {volunteer_name_input}! You are volunteer {
                  volunteer_count + 1}")
            print()

            # * creating a dictionary to store the new user's name
            current_volunteer_info.update(
                {"Volunteer Name": volunteer_name_input})

    return current_volunteer_info


# @! Function to update the "Bags Counted Correctly" key-value
def appendBagsCountedCorrectly(current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly):

    #!Updating the user's data in "current_volunteer_info" and "volunteer_info" if the data has been previously stored

    # ? checking if "Bags Counted Correctly" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Bags Counted Correctly" in current_volunteer_info:

        # * updating current volunteer info with the value of "bags_counted_correctly"
        current_volunteer_info["Bags Counted Correctly"] = bags_counted_correctly

        # * we also update the old "Bags Counted Correctly" key value in "volunteer_info"

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Name" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Bags Counted Correctly" key to the "bags_counted_correctly" variable
                volunteer_info["Bags Counted Correctly"] = bags_counted_correctly
                break

    #!Creating new user data in "current_volunteer_info" if no data about that user has been previously stored

    # ? comes here if "Bags Counted Correctly" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # * we create a "Total Bags Weighed" key value in "current_volunteer_info"
        current_volunteer_info.update(
            {"Bags Counted Correctly": bags_counted_correctly})

    return current_volunteer_info

# @! Function to update the "Number of Bags Counted" key-value


def appendNumberOfBagsCounted(current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted):

    #!Updating the user's data in "current_volunteer_info" and "volunteer_info" if the data has been previously stored

    # ? checking if "Total Bags Weighed" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Number of Bags Counted" in current_volunteer_info:

        # * updating current_volunteer_info
        current_volunteer_info["Number of Bags Counted"] = bags_counted

        # * we also update the old "Number of Bags Counted" key value in "volunteer_info"

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Name" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Number of Bags Counted" key to the "bags_counted" variable
                volunteer_info["Number of Bags Counted"] = bags_counted
                break

    #!Creating new user data in "current_volunteer_info" if no data about that user has been previously stored

    # ? comes here if "Total Bags Weighed" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # * we create a "Total Bags Weighed" key value in "current_volunteer_info"
        current_volunteer_info.update(
            {"Number of Bags Counted": bags_counted})

    # print(current_volunteer_info)
    print()

    return current_volunteer_info

# @! Function to update the "Volunteer Accuracy (%)" key-value


def appendVolunteerAccuracy(current_volunteer_info, volunteer_name_input, volunteer_list, volunteer_accuracy):

    #!Creating new user data in "current_volunteer_info" if no data about that user has been previously stored

    # ? checking if "Volunteer Accuracy (%)" key is in "current_volunteer_info" (means that it has been previously stored)

    if "Volunteer Accuracy (%)" in current_volunteer_info:

        # * updating current_volunteer_info
        current_volunteer_info["Volunteer Accuracy (%)"] = volunteer_accuracy

        # * we update the old "Volunteer Accuracy (%)" key value in "volunteer_info"

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Accuracy (%)" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Number of Bags Counted" key to the "volunteer_accuracy" variable
                volunteer_info["Volunteer Accuracy (%)"] = volunteer_accuracy
                break

    #!Creating new user data in "current_volunteer_info" if no data about that user has been previously stored

    # * checking if "Volunteer Accuracy (%)" key is not in "volunteer_accuracy" (means that it has been previously stored)
    else:

        # * we create a "Volunteer Accuracy (%)" key value
        current_volunteer_info.update(
            {"Volunteer Accuracy (%)": volunteer_accuracy})

    # print(current_volunteer_info)
    print()

    return current_volunteer_info

# @! Function to update the volunteer_info list before CoinCount.txt gets updated


def appendCurrentVolunteerInfo(volunteer_name_input, volunteer_list, current_volunteer_info):
    #! Creates new user data that runs if "volunteer_list" is empty

    if not volunteer_list:

        # * updating the "volunteer_list" with "updated_volunteer_list"s
        volunteer_list.append(current_volunteer_info)

    #!  Comes here if  "volunteer_list" is not empty
    else:

        # ? Creating a copy of "volunteer_list" so that we don't modify the original list as we are iterating over it
        volunteer_list_copy = volunteer_list[:]

        # * iterating over each dictionary in "volunteer_list"
        for volunteer_info in volunteer_list:

            # * storing the "Volunteer Name" key-value in a variable for easier access
            volunteer_name = volunteer_info["Volunteer Name"]

            #! updates a previous user's data

            # ? checking if the previously stored "volunteer_name" matches the current "volunteer_name_input"
            if volunteer_name == volunteer_name_input:

                # * update the "volunteer_info" with the new information (current_volunteer_info) if their name is found
                volunteer_info.update(current_volunteer_info)

            #! code that runs if the volunteer's name was not found in volunteer_list, and their data was not previously stored (new data has be created)
            else:
                volunteer_list.append(current_volunteer_info)
                break

        # volunteer_list = volunteer_list_copy

    return volunteer_list
