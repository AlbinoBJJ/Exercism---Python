"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL
    
    elif len(list_one) < len(list_two):
        smaller_size = len(list_one)
        for index in range(len(list_two) - smaller_size + 1):
            if list_one == list_two[index : index + smaller_size]:
                return SUBLIST

    elif len(list_one) > len(list_two):
        smaller_size = len(list_two)
        for index in range(len(list_one) - smaller_size + 1):
            if list_two == list_one[index : index + smaller_size]:
                return SUPERLIST

    return UNEQUAL