# import
import random
import math


# Functions go here
# Ultimate number checker works for 4 situations!!!!!
# checks for intgers.  Optinally checks an integer is above a minimum / below a maximum
def num_check(question, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()

            if response == exit_code:
                return response
            else:
                response = int(response)

            # Checks between two integers (includes endpoints)
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            # Checks for a number more than a minimum (no max)
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

        elif response == "egg":
            response = "egg"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Prints instructions if necessary, returns <blank>
def instructions():
    statement_generator("Instuctions", "*", "-")
    print()
    print(
        "In this game your goal is too guess the\n"
        "randomly generated number between 1-100\n"
        "or between a high and low or your choice\n"
        "\n"
        "There are 2 modes:\n"
        "\n"
        "Mode 1: 1-100\n"
        "Mode 2: User choice\n"
        "\n"
        "You can Either choose to play continuesly\n"
        "by pressing <enter> or play a certain #\n"
        "of rounds. You can say xxx to exit game\n"
        "at anytime while guessing."
    )
    return""


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

    top_right_decoration = " " * len(satement) + top_right

    print(top_right)
    print(statement_generator)
    print()


# Easter Egg - Credit Toby Ayers 
# couldnt have done it without him
def easter_egg():
    pico_again = "yes"
    valid = False
    while not valid:
        print()
        print()
        print("           *")
        pico = input("    Pico-8    ")
        print()
        print()
        pico_choice = random.randint(1, 10)

        while pico_again == "yes":

            pico_guess = num_check("choose a number between 1 and 10 ", "oops")

            if pico_guess > pico_choice:
                print()
                print("wrong")
                continue
            elif pico_guess < pico_choice:
                print()
                print("wrong")
                continue
            elif pico_guess == pico_choice:
                print()
                print("congratulations")
                break
        pico_again = yes_no("do you want to play again? ")

        if pico_again == "no":
            pico_again = "no"
            break
        elif pico_again == "yes":
            pico_again = "yes"
            continue

# Main Routine


choose_instruction = "Choose a number between 1 and 100"

# Welcome
statement_generator("Welcome to the Higher Lower Game", "!", "=")


# Ask user if they have played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

elif played_before == "egg":
    easter_egg()
print()

game_repeat = ""
while game_repeat == "":
    # Ask user what mode they want to play
    mode_choice = num_check("Would you like to play Mode #1 or Mode #2: ", "<error> please choose 1 or 2", 1, 2)

    # Mode heading and high and low num difining
    if mode_choice == 1:
        mode_heading = "Mode #1: 1-100: "
        # Sets high amd low boundarys automaticaly
        low_boundary = 1
        high_boundary = 100

    elif mode_choice == 2:
        mode_heading = "Mode #2: User choice"
        # Asks user for low and high boundarys
        low_boundary = num_check("What is the low boundary? ", "<error> please enter a number above 0", 0, None)
        high_boundary = num_check("What is the high boundary? ", "<error> please enter a number above {}".format(low_boundary), low_boundary, None)

    print()
    statement_generator(mode_heading, "-", "*")
    print()

    # 0n reapeats sets all varibles from last game back too 0
    rounds_played = 0
    rounds_won = 0
    rounds_lost = 0

    # Games result list (filled when you win or lose)
    game_summary = []

    # Ask user how many rounds the want to play and sets rounds played to 0
    round_error = "Please type either <enter> or an integer that is more the 0"

    rounds = num_check("How many rounds: ", round_error, exit_code="")
    rounds_played = 0

    end_game = "no"
    while end_game == "no":

        # rounds heading
        if rounds == "":
            round_heading = "Continuous Mode Round: Round {}".format(rounds_played + 1)

        else:
            round_heading = "Round {} of {}".format(rounds_played + 1, rounds)
            # End game if Rounds played is smae as number of rounds
            if rounds == rounds_played + 1:
                end_game = "yes"

        print()
        statement_generator(round_heading, "|", "~")
        print()

        # Generate computer choice
        comp_choice = random.randint(low_boundary, high_boundary)

        # Calculate number of guesses depnding on the range of numbers
        num_range = high_boundary - low_boundary + 1
        max_raw = math.log2(num_range)
        max_upped = math.ceil(max_raw)
        max_guesses = max_upped + 1
        statement_generator("Max Guesses: {}".format(max_guesses), "?", "-")
        print()

        # defines guess and number of guesses so loop can continue
        guess = -1
        num_guess = 0

        # already guessed list (filled when you guess)
        already_guessed = []

        # looped untill user guesses corectly
        while guess != comp_choice:

            # Gets user guess
            guess_instruction = "Guess a number between {} and {}: ".format(low_boundary, high_boundary)
            guess_error = "<error> please choose an interger between {} and {}".format(low_boundary, high_boundary)

            guess = num_check(guess_instruction, guess_error, low_boundary, high_boundary, "xxx")
            print()

            # Exits game if exit code typed
            if guess == "xxx":
                end_game = "yes"
                result = "quit"
                break

            # if user guess is the same as what they have guessed before
            if guess in already_guessed:
                print("You have already Guessed this number ")
                print("You still have {} guesses left".format(guesses_left))
                print()
                continue

            # adds guess to list of already guessed
            already_guessed.append(guess)

            # Compare guess with computer choice
            if guess != comp_choice:
                if guess < comp_choice:
                    statement_generator("To Low try again", "<", "=")
                    print()
                elif guess > comp_choice:
                    statement_generator("To High try again", ">", "=")
                    print()

                # Adds users guesses
                num_guess += 1
            elif guess == comp_choice:
                statement_generator("Congratulations! You got it Right", "!", "-")
                print()
                # Adds too rounds won
                rounds_won += 1
                # Adds users guesses
                num_guess += 1
                # Defines Result
                result = "won"
                break

            # checks how many guesses are left
            guesses_left = max_guesses - num_guess
            if num_guess != max_guesses:
                print("You have {} Guesses left".format(guesses_left))
                print()
            else:
                statement_generator("You Lose", "?", "*")
                # Adds to rounds lost
                rounds_lost += 1
                print()
                # Defines Result
                result = "lost"
                # Outputs the number
                print("The Number was {}!".format(comp_choice))
                print()
                break

        # Adds Game result to a list for history
        game_summary.append("Round #{}: {}".format(rounds_played + 1, result))

        # Every round adds how many rounds played
        rounds_played += 1

    # Calculate Game Stats
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100

    # Displays game stats with % values to the nearest whole number
    statement_generator("Game stats", "*", "=")
    print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
    print()

    # Asks user if they want to see there history
    show_history = yes_no("Would you like to see game history? ")
    print()

    # displays history if user says yes
    if show_history == "yes":
        statement_generator("Game History", "*", "=")
        for game in game_summary:
            print(game)

    # final message output
    print()
    statement_generator("Thanks for Playing", "!", "=")

    # To play again
    play_again = yes_no("Do you want to reapeat? ")
    if play_again == "yes":
        game_repeat = ""
    else:
        game_repeat = " "
