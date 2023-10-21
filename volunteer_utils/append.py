# todo: store each in its own separate module
def appendVolunteerName(current_volunteer_info, volunteer_list, volunteer_name_input):
    # * checking if volunteer list is empty
    # ? ("[] is a falsy value, so not turns [] to true)
    if not volunteer_list:

        # * creating a dictionary to store information for a new user
        current_volunteer_info.update({"Volunteer Name": volunteer_name_input})
        print(f"Hello {volunteer_name_input}!")
        print()

    # * if volunteer_list is not empty
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
                    f"Welcome back {volunteer_name}! Here is your previous data")
                current_volunteer_info = volunteer_info
                break

            # ? runs if "volunteer_name_input" is NOT found in volunteer
            else:

                # * creating a dictionary to store information for a new user
                current_volunteer_info["Volunteer Name"] = volunteer_name_input

    return (current_volunteer_info)


def appendBagsCountedCorrectly(current_volunteer_info, bags_counted_correctly):

    # * checking if "Bags Counted Correctly" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Bags Counted Correctly" in current_volunteer_info:

        # ? we update the old "Bags Counted Correctly" key value
        # * assigning the "bags_counted" value to the "Total Bags Weighed"
        current_volunteer_info["Bags Counted Correctly"] = bags_counted_correctly

    # * checking if "Bags Counted Correctly" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # ? we create a "Bags Counted Correctly" key value
        current_volunteer_info.update(
            {"Bags Counted Correctly": bags_counted_correctly})

    return current_volunteer_info


def appendNumberOfBagsCounted(current_volunteer_info, bags_counted):

    # * checking if "Total Bags Weighed" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Number of Bags Counted" in current_volunteer_info:

        # ? we update the old "Total Bags Weighed" key value
        # * assigning the "bags_counted" value to the "Total Bags Weighed"
        current_volunteer_info["Number of Bags Counted"] = bags_counted
        print("updated")

    # * checking if "Total Bags Weighed" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # ? we create a "Total Bags Weighed" key value
        current_volunteer_info.update(
            {"Number of Bags Counted": bags_counted})

    # print(current_volunteer_info)
    print()

    return current_volunteer_info
