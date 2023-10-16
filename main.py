""" Loads up the coinCount.txt file"""
from loadCoinCount import loadCoinCount

print("Print a welcome message later")
print()

print(loadCoinCount())
print()


# * stores all of the volunteers' information
volunteer_list = []

# * stores the information for each type of coin
coin_information = [
    {
        "Coin Type (£)": 2,
        "Bag Value (£)": 20,
        "Coin weight (g)": 12
    },
    {
        "Coin Type (£)": 1,
        "Bag Value (£)": 20,
        "Coin weight (g)": 8.75
    },
    {
        "Coin Type (£)": 0.50,
        "Bag Value (£)": 10,
        "Coin weight (g)": 8.00
    },
    {
        "Coin Type (£)": 0.20,
        "Bag Value (£)": 10,
        "Coin weight (g)": 5.00
    },
    {
        "Coin Type (£)": 0.10,
        "Bag Value (£)": 5,
        "Coin weight (g)": 6.50
    },
    {
        "Coin Type (£)": 0.05,
        "Bag Value (£)": 5,
        "Coin weight (g)": 2.35
    },
    {
        "Coin Type (£)": 0.02,
        "Bag Value (£)": 1,
        "Coin weight (g)": 7.12
    },
    {
        "Coin Type (£)": 0.50,
        "Bag Value (£)": 1,
        "Coin weight (g)": 3.56
    }
]

#!Initialising counter variables to 0

# * stores the running total of the VALUE of bags weighed
bags_value_counter = 0

# * stores the running total of the NUMBER of bags weighed
bags_weighed = 0

# * stores the running total of the NUMBER of bags weighed INCORRECTLY
bags_weighed_incorrectly = 0

# * stores the running total of the NUMBER of bags weighed CORRECTLY
bags_weighed_correctly = 0


# @! Handling the VOLUNTEER'S NAME

while True:

    # * collecting the volunteer’s name input
    volunteer_name_input = input("Input volunteer name: ").title()

    # * verifying that the user types in letters not numbers
    if volunteer_name_input.isdigit():
        print("Please type in an actual name, with letters!")
        continue

    print(f"Name accepted. Hello {volunteer_name_input}!")
    print()
    break

# * checking if volunteer list is empty
# ? ("[] is a falsy value, so not turns it to true)
if not volunteer_list:

    # * appending volunteer_name_input to volunteer list
    volunteer_list.append({"Volunteer Name": volunteer_name_input})
    print(volunteer_list)

# * if volunteer_list is not empty
# ? a list comprehension that iterates over the previous "Volunteer Name" keys in each dictionary in "volunteer_list"

previous_volunteer_names = [dictionary["Volunteer Name"]
                            for dictionary in volunteer_list]
print(previous_volunteer_names)

#! Greeting the user with "Volunteer Name"

# * iterating over each name in previous_volunteer_names
for name in previous_volunteer_names:
    # * check if the volunteer_name_input equal to name (that means the user has stored their name previously)
    if volunteer_name_input == name:
        print(f"Hello again {name}!")
