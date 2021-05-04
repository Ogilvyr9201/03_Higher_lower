# imports
import math


# Functions


def num_check(question, error, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# Main routine
# loope for testing

for item in range(0, 4):
    # mode checker
    mode_choice = num_check("Would you like to play Mode #1 or Mode #2: ", "<error> please choose 1 or 2", 1, 2)
    print()

    # Mode heading and high and low boudarys
    if mode_choice == 1:
        mode_heading = "Mode #1: 1-100: "
        print(mode_heading)
        low_boundary = 1
        high_boundary = 100

    elif mode_choice == 2:
        mode_heading = "Mode #2: User choice"
        print(mode_heading)
        low_boundary = num_check("What is the low boundary? ", "<error> please eneter a number above 0", 0, None)
        print()
        high_boundary = num_check("What is the high boundary? ", "<error> please enter a number above {}".format(low_boundary), low_boundary, None)
    print()

    # Calculate number of guesses
    range = high_boundary - low_boundary + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
