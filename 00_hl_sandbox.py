# number checker goes here...
def num_check(question, low=None, high=None):
    error = "please enter a valid response"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    continue

            else:
                return response

        except ValueError:
            print(error)


# main routine
num_rounds = num_check("Rounds? ", 0)
guess = num_check("Guess: ", 0, 10)

fav_num = num_check("Favourite? ")

print("Rounds chosen: ", num_rounds)
print("Guess: ", guess)
print("Favourite: ", fav_num)
