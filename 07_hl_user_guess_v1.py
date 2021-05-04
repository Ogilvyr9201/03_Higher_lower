# imports
import random

# Functions


# Number checker
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


# main routine
# lists
already_guessed = []


# Looped for testing
guess = -1

loop = ""
while loop == "":

    # gets comp choice for guessing between 1 - 100 for testing
    comp_choice = random.randint(1, 100)

    # Loop until user gets correct
    while guess != comp_choice:
        # gets user guess (between 1-100 for testing would be low and high boundarys)
        guess = num_check("Guess a number between 1 and 100: ", "<error> please choose an interger", 1, 100)
        print()

        # Compares guess
        # if user guess is the same as what they have guessed before
        if guess in already_guessed:
            print("You have already Guessed this number ")
            print("You still have __ guesses left")
            print()
            continue

        # adds guess to list of already guessed
        already_guessed.append(guess)

        if guess < comp_choice:
            print("To Low try again ")
            print()
            continue
        elif guess > comp_choice:
            print("To High try again ")
            print()
            continue
        elif guess == comp_choice:
            continue

    print("Congratulations")
    print()
