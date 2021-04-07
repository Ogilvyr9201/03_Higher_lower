# import random
import random


# Functions go here
# Ultimate number checker works for 4 situations!!!!!
def num_check(question, error, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low is not None and high is not None:
                if low < response < high:
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

if played_before == "no":
    instructions()
    print()

# Ask user how many rounds the want to play
rounds = check_rounds()
