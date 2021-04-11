# import
import random
import math


# Functions go here
# Ultimate number checker works for 4 situations!!!!!
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


# A number checker that allows enter as a response Imported From RPS
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more the 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


# Checks for yes or no responses Imported From LU
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Instructions are here
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules go here")
    print()
    return""


# Main Routine
rounds_played = 0
choose_instruction = "Choose a number between 1 and 100"


# Ask user if they have played before
played_before = yes_no("Have you played this game before? ")
print()

if played_before == "no":
    instructions()

print()
# Ask user what mode they want to play
mode_choice = num_check("Would you like to play Mode #1 or Mode #2: ", "<error> please choose 1 or 2", 1, 2)

# Mode heading and high and low num difining
if mode_choice == 1:
    mode_heading = "Mode #1: 1-100: "
    print(mode_heading)
    low_boundary = 1
    high_boundary = 100

elif mode_choice == 2:
    mode_heading = "Mode #2: User choice"
    print(mode_heading)
    low_boundary = num_check("What is the low boundary? ", "<error> please Eneter a number above 0", 0, None)

    print()
    high_boundary = num_check("What is the high boundary? ", "<error> please enter a number above {}".format(low_boundary), low_boundary, None)

# Ask user how many rounds the want to play
rounds = check_rounds()

end_game = ""
while end_game == "":

    # rounds heading
    print()
    if rounds == "":
        round_heading = "Continuous Mode Round: Round {}".format(rounds_played + 1)

    else:
        round_heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(round_heading)

    # Generate computer choice
    comp_choice = random.randint(low_boundary, high_boundary)
    print(comp_choice)
    print()

    # Calculate number of guesses
    range = high_boundary - low_boundary + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))
    print()

    end_game = yes_no("Do you want to reapeat? ")
    if end_game == "yes":
        end_game = ""
        continue
    else:
        break
