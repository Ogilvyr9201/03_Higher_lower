import random

# Functions


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


# main routine
# Ask user for High and low intergers


low_boundary = num_check("What is the low boundary? ", "<error> \
please Eneter a number above 0", 0, None)
print()

high_boundary = num_check("What is the high boundary? ", "<error> please \
Eneter a number above {}".format(low_boundary), low_boundary, None)
print()

# testing loop generate comp choice 20 times
loop_stop = 0

loop = ""
while loop == "":
    comp_choice = random.randint(low_boundary, high_boundary)
    print(comp_choice)
    loop_stop += 1
    if loop_stop == 20:
        break
