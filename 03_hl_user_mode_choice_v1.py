def mode_check(question):
    valid = False
    while not valid:
        response == input(question)
        mode_error = "<error> Pick '1' or '2' "

        if response != "":
            try:
                response = int(resposne)

                if response == 1:
                    response = 1

                elif response == 2:
                    response = 2

                else:
                    print(mode_error)
                    print()

            except ValueError:
                print(mode_error)
        else:
            return response


# Main routine
# looped for testing
loop = ""
while loop == "":
    mode_choice = mode_check("Do you want to play Mode #1 or Mode #2 ? ")
    if mode_choice == 1:
        print("Mode #1: 1-100: ")
        print()
    else:
        print("Mode #2: User choice")
        print()