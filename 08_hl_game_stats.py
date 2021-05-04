# from RPS

game_summary = []

rounds_played = 5
rounds_lost = 0
rounds_won = 0

for item in range(0, 5):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "won":
        rounds_won += 1

    game_summary.append("Round #{}: {}".format(rounds_played + 1, result))

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()
