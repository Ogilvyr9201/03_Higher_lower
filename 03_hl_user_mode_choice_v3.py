# version 2 actually works

# checkes users enter an integer between two endpoints.
def num_checker(question, low_num, high_num):
    while True:

        error = "<error> Please type an interger between {} or {}" \
         .format(low_num, high_num)

        try:
            response = int(input(question))

            # Checks if user puts in the right input
            if low_num <= response <= high_num:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# Main routine
# looped for testing


loop = ""
while loop == "":
    mode_choice = num_checker("Would you like to play Mode\
 #1 or Mode #2: ", 1, 2)

    if mode_choice == 1:
        print("Mode #1: 1-100: ")
        print()
    elif mode_choice == 2:
        print("Mode #2: User choice")
        print()
