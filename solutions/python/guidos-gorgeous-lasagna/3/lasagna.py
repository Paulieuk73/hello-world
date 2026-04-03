"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the cake.

    :param number_of_layers: int - number of layers in the lasagne.
    :return: int - Preparation time in minutes

    Function that takes the number of layers in the lasagne as an arguement
    and returns how many long the preparation time will be in minutes
    based on the `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the how many  minutes I have been cooking the lasagne.

    :param number_of_layers: int - The number of layers added to the lasagna.
    :param elapsed_bake_time: int - The number of minutes the lasagna has spent baking in the oven already.
    :return: int - Time spent cooking

    Function that takes the number of layers in the lasagne and number of minutes 
    already spent baking as an arguement and returns the total time spent cooking
    preparation plus cooking.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time


print(EXPECTED_BAKE_TIME)
bake_time_remaining(30)
preparation_time_in_minutes(2)
elapsed_time_in_minutes(2, 20)