import os
import re

input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r", encoding="utf-8") as f:
    data = f.read().splitlines()


def calculate_winnings(win_list: list, user_list: list) -> int:
    """Function to calculate winnings"""
    matching_numbers = sum(number in user_list for number in win_list)
    if matching_numbers > 0:
        winnings = 2**(matching_numbers-1)
    else:
        winnings = 0
    return winnings

winnings_list = []

for card in data:
    #card_number = int(re.findall(r"Card (\d+):", card)[0])

    win_numbers_str = re.findall(r"Card\s*\d+:\s*([\d\s*]+)\s*\|", card)[0]
    win_numbers = [int(number) for number in win_numbers_str.split()]

    my_numbers_str = re.findall(r"\|\s*([\d\s]+)", card)[0]
    my_numbers = [int(number) for number in my_numbers_str.split()]

    winnings_list.append(calculate_winnings(win_numbers, my_numbers))


print(sum(winnings_list))
