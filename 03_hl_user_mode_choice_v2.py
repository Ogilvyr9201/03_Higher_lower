# version 2 actually works
def check_mode(question):
    while True:
        response = input(question)

        mode_error = "<error> Please Type 1 or 2"

        if response != "":
            try:
                response = int(response)

                if 1 <= response <= 2:
                    return response
                else:
                    print(mode_error)
                    print()

            except ValueError:
                print(mode_error)
                print()

# Main routine
# looped for testing


loop = ""
while loop == "":
    mode_choice = check_mode("Would you like to play Mode #1 or Mode #2: ")
    if mode_choice == 1:
        print("Mode #1: 1-100: ")
        print()
    elif mode_choice == 2:
        print("Mode #2: User choice")
        print()
