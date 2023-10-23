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
                    f"Welcome back {volunteer_name}! Here is your previous data:")
                print()

                # * setting the "volunteer_info" in "current_volunteer_info"
                current_volunteer_info = volunteer_info
                print(current_volunteer_info)

                break
            # ? comes here if "volunteer_name_input" is NOT found in volunteer
            else:

                # * creating a dictionary to store information for a new user
                current_volunteer_info["Volunteer Name"] = volunteer_name_input

    return (current_volunteer_info)


# todo (in future): write a function to handle all of these
def appendBagsCountedCorrectly(current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted_correctly):

    # * checking if "Bags Counted Correctly" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Bags Counted Correctly" in current_volunteer_info:

        # * updating current volunteer info
        current_volunteer_info["Bags Counted Correctly"] = bags_counted_correctly

        # * we update the old "Bags Counted Correctly" key value in "current_volunteer_info" instead of creating a new one

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Name" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Bags Counted Correctly" key to the "bags_counted_correctly" variable
                volunteer_info["Bags Counted Correctly"] = bags_counted_correctly
                break

    # * checking if "Bags Counted Correctly" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # ? we create a "Bags Counted Correctly" key value
        current_volunteer_info.update(
            {"Bags Counted Correctly": bags_counted_correctly})

    return current_volunteer_info


def appendNumberOfBagsCounted(current_volunteer_info, volunteer_name_input, volunteer_list, bags_counted):

    # * checking if "Total Bags Weighed" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Number of Bags Counted" in current_volunteer_info:

        # * updating current_volunteer_info
        current_volunteer_info["Number of Bags Counted"] = bags_counted

        # * we update the old "Number of Bags Counted" key value in "current_volunteer_info" instead of creating a new one

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Name" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Number of Bags Counted" key to the "bags_counted" variable
                volunteer_info["Number of Bags Counted"] = bags_counted
                break

    # * checking if "Total Bags Weighed" key is not in "current_volunteer_info" (means that it has been previously stored)
    else:

        # ? we create a "Total Bags Weighed" key value
        current_volunteer_info.update(
            {"Number of Bags Counted": bags_counted})

    # print(current_volunteer_info)
    print()

    return current_volunteer_info


def appendVolunteerAccuracy(current_volunteer_info, volunteer_name_input, volunteer_list, volunteer_accuracy):

    # * checking if "Volunteer Accuracy (%)" key is in "current_volunteer_info" (means that it has been previously stored)
    if "Volunteer Accuracy (%)" in current_volunteer_info:

        # * updating current_volunteer_info
        current_volunteer_info["Number of Bags Counted"] = volunteer_accuracy

        # * we update the old "Volunteer Accuracy (%)" key value in "current_volunteer_info" instead of creating a new one

        # * iterating over the dictionaries in volunteer_list (that contain previously stored information)
        for volunteer_info in volunteer_list:

            # * grabbing the correct dictionary for the user by checking the "Volunteer Accuracy (%)" key
            if volunteer_info["Volunteer Name"] == volunteer_name_input:

                # * setting the "Number of Bags Counted" key to the "volunteer_accuracy" variable
                volunteer_info["Number of Bags Counted"] = volunteer_accuracy
                break

    # * checking if "Volunteer Accuracy (%)" key is not in "volunteer_accuracy" (means that it has been previously stored)
    else:

        # ? we create a "Volunteer Accuracy (%)" key value
        current_volunteer_info.update(
            {"Volunteer Accuracy (%)": volunteer_accuracy})

    # print(current_volunteer_info)
    print()

    return current_volunteer_info
