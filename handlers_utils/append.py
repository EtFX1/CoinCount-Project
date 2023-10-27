from pprint import pprint
from collections import OrderedDict
# todo: store each in its own separate module


def appendVolunteerName(current_volunteer_info, volunteer_list, volunteer_name_input):
    # * checking if volunteer list is empty
    # ? ("[] is a falsy value, so not turns [] to true)
    if not volunteer_list:

        # * creating a dictionary to store information for a new user
        current_volunteer_info.update({"Volunteer Name": volunteer_name_input})
        print(f"Hello {volunteer_name_input}!")
        print()

    #!Updating the user's data in "current_volunteer_info" and "volunteer_info" if the data has been previously stored
    else:

        #
        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * extracting the volunteer's name key-value from each dictionary
            volunteer_name = volunteer_info["Volunteer Name"]

            # ? checking if the previously stored volunteer name matches the current volunteer name input
            if volunteer_name == volunteer_name_input:

                # * greeting the user and showing them their previously stored data
                print(
                    f"Welcome back {volunteer_name}! Here is your previous data:")
                print()

                # * updating current volunteer's name with the value of "Volunteer Name"
                current_volunteer_info["Volunteer Name"] = volunteer_name

                # * setting the "volunteer_info" in "current_volunteer_info"
                current_volunteer_info = volunteer_info
                # pprint(OrderedDict(current_volunteer_info), indent=1)
                print()

                break
            # ? comes here if "volunteer_name_input" is NOT found in volunteer
            else:

                # * creating a dictionary to store information for a new user
                current_volunteer_info["Volunteer Name"] = volunteer_name_input

    return (current_volunteer_info)


# todo (in future): write a function to handle all of these
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


def appendVolunteerAccuracy(current_volunteer_info, volunteer_name_input, volunteer_list, volunteer_accuracy):

    #!Creating new user data in "current_volunteer_info" if no data about that user has been previously stored

    # ? checking if "Volunteer Accuracy (%)" key is in "current_volunteer_info" (means that it has been previously stored)

    if "Volunteer Accuracy (%)" in current_volunteer_info:

        # * updating current_volunteer_info
        current_volunteer_info["Number of Bags Counted"] = volunteer_accuracy

        # * we update the old "Volunteer Accuracy (%)" key value in "volunteer_info"

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Accuracy (%)" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Number of Bags Counted" key to the "volunteer_accuracy" variable
                volunteer_info["Number of Bags Counted"] = volunteer_accuracy
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


#! Updating the final volunteer list
# todo add comments

def updateVolunteerList(volunteer_name_input, volunteer_list, current_volunteer_info):

    # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
    for volunteer_info in volunteer_list:

        # * extracting the volunteer's name key-value from each dictionary
        volunteer_name = volunteer_info["Volunteer Name"]

        #! Updates the user's info if their name is found
        if volunteer_name == volunteer_name_input:
            print(volunteer_info)
            print("new volunteer info")
            volunteer_info.update(current_volunteer_info)
        #! comes here if its a new user and just adds new info entirely
        else:
            # * Adding the current_volunteer_info to the final volunteer list
            volunteer_list.append(current_volunteer_info)
