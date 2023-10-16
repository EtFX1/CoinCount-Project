""" Loads up the coinCount.txt file"""
from loadCoinCount import loadCoinCount

print(loadCoinCount())

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
