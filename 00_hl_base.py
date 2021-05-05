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

        else:
            print("<error> Please say yes or no")
            print()


# Prints instructions if necessary, returns <blank> 
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules go here")
    print()
    return""


# Main Routine
choose_instruction = "Choose a number between 1 and 100"


# Ask user if they have played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print()
# Ask user what mode they want to play
mode_choice = num_check("Would you like to play Mode #1 or Mode #2: ", "<error> please choose 1 or 2", 1, 2)

# Mode heading and high and low num difining
if mode_choice == 1:
    mode_heading = "Mode #1: 1-100: "
    low_boundary = 1
    high_boundary = 100

elif mode_choice == 2:
    mode_heading = "Mode #2: User choice"
    low_boundary = num_check("What is the low boundary? ", "<error> please enter a number above 0", 0, None)

    print()
    high_boundary = num_check("What is the high boundary? ", "<error> please enter a number above {}".format(low_boundary), low_boundary, None)

print()
print(mode_heading)
print()

game_repeat = ""
while game_repeat == "":

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
        print(round_heading)
        print()

        # Generate computer choice
        comp_choice = random.randint(low_boundary, high_boundary)
        print(comp_choice)
        print()

        # Calculate number of guesses depnding on the range of numbers
        num_range = high_boundary - low_boundary + 1
        max_raw = math.log2(num_range)
        max_upped = math.ceil(max_raw)
        max_guesses = max_upped + 1
        print("Max Guesses: {}".format(max_guesses))
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
                rounds_played -= 1
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
                    print("To Low try again ")
                    print()
                elif guess > comp_choice:
                    print("To High try again ")
                    print()
                
                # Adds users guesses
                num_guess += 1
            elif guess == comp_choice:
                print("Congratulations! You got it right!")
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
                print("You lose lmao")
                # Adds to rounds lost
                rounds_lost += 1
                print()
                # Defines Result
                result = "lost"
                break
        
        # Adds Game result to a list for history
        game_summary.append("Round #{}: {}".format(rounds_played + 1, result))

        # Next round
        rounds_played += 1

    # Calculate Game Stats
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100

    # Displays game stats with % values to the nearest whole number
    print("**** Game Statistics ****")
    print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
    print()

    # Asks user if they want to see there history
    show_history = yes_no("would you like to see game history? ")
    print()

    # displays history if user says yes
    if show_history == "yes":
        print("**** Game History ****")
        for game in game_summary:
            print(game)

        print()
        print("Thanks for playing")

    # Doesnt display history if user says no
    elif show_history == "no":
        print("Thanks for Playing")

    print()
    # To play again
    play_again = yes_no("Do you want to reapeat? ")
    if play_again == "yes":
        game_repeat = ""
    else:
        game_repeat = " "
