"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Constantes globais
EXPECTED_BAKE_TIME = 40
BASE_PREPARATION_LAYER_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes) based on layers.

    This function takes the number of layers and calculates the total
    preparation time by multiplying it by the constant time per layer.
    """
    return number_of_layers * BASE_PREPARATION_LAYER_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the total elapsed time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time spent (preparation + baking).

    This function sums the preparation time (based on layers) and the
    time the lasagna has already spent in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# elapsed_time = int(input('Type de total elpsed time: '))
# lasagna_layers = int(input('Type how many layers the lasagna will have: '))

# remaining_bake_time = bake_time_remaining(elapsed_time)
# preparation_time = preparation_time_in_minutes(lasagna_layers)
# total_time_spent = elapsed_time_in_minutes(lasagna_layers, elapsed_time)

# print(f'The elepsed time is {remaining_bake_time} minutes')
# print(f'The total preparation time is {preparation_time} minutes')
# print(f'The total time spent till now, counting prepare and baking time, is {total_time_spent} minutes')