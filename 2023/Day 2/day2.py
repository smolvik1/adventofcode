import os
import re

input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

BLUE = 14
RED = 12
GREEN = 13

possible_games = []
power_games = []

for game in data:
    game_number = int(re.findall(r"Game (\d+)", game)[0])

    # Returns list of string numbers with occurrences of digit
    # followed by space and respective colors
    blue_numbers = re.findall(r"(\d+)\s+blue", game)
    red_numbers = re.findall(r"(\d+)\s+red", game)
    green_numbers = re.findall(r"(\d+)\s+green", game)

    # Convert the list of strings to integers and sum them up
    max_of_blue = max(map(int, blue_numbers))
    max_of_red = max(map(int, red_numbers))
    max_of_green = max(map(int, green_numbers))

    possible_game = (
        (max_of_blue <= BLUE) and (max_of_red <= RED) and (max_of_green <= GREEN)
    )

    if possible_game:
        possible_games.append(game_number)

    power_game = max_of_blue * max_of_red * max_of_green
    power_games.append(power_game)

print(f'Solution part 1: {sum(possible_games)}')

print(f'Solution part 2: {sum(power_games)}')
