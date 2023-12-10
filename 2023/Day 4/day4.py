import os
import re

input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r", encoding="utf-8") as f:
    data = f.read().splitlines()


def calculate_winnings(win_list: list, user_list: list) -> int:
    """Function to calculate winnings"""
    matching_numbers = sum(number in user_list for number in win_list)
    if matching_numbers > 0:
        pts = 2 ** (matching_numbers - 1)
    else:
        pts = 0

    return pts


def calculate_cards_won(win_list: list, user_list: list, cn: int) -> list[int]:
    """Function to calculate cards won"""
    matching_numbers = sum(number in user_list for number in win_list)

    if matching_numbers > 0:
        cards_w = list(range(cn + 1, (cn + 1) + matching_numbers, 1))
    else:
        cards_w = None

    return cards_w


winnings_list = []
cards = {}
copies = {}


def update_copy(copies_dict: dict, cn: int, nmbr: int) -> None:
    """Update the occurrence of a card"""
    if cn not in copies_dict:
        copies_dict[cn] = {"copies": nmbr}
    else:
        copies_dict[cn]["copies"] += nmbr


def update_copies(copies_dict: dict, copies_w: list) -> None:
    """Update cards copies won"""
    if copies_w is not None:
        for cn in copies_w:
            update_copy(copies_dict=copies_dict, cn=cn, nmbr=1)


for card in data:
    card_number = int(re.findall(r"Card\s*(\d+):", card)[0])

    win_numbers_str = re.findall(r"Card\s*\d+:\s*([\d\s*]+)\s*\|", card)[0]
    win_numbers = [int(number) for number in win_numbers_str.split()]

    my_numbers_str = re.findall(r"\|\s*([\d\s]+)", card)[0]
    my_numbers = [int(number) for number in my_numbers_str.split()]

    points = calculate_winnings(win_numbers, my_numbers)
    winnings_list.append(points)

    cards_won = calculate_cards_won(win_numbers, my_numbers, card_number)

    cards.update(
        {
            card_number: {
                "win_numbers": win_numbers,
                "my_numbers": my_numbers,
                "cards_won": cards_won,
            }
        }
    )
    update_copies(copies_dict=copies, copies_w=cards_won)

print(f"Solution part 1: {sum(winnings_list)}")

for card_number, copy_info in copies.items():
    copy_number = copy_info["copies"]
    cards_won = cards[card_number]["cards_won"]

    if cards_won is not None:
        new_copies_won = cards_won * copy_number
        update_copies(copies, new_copies_won)


CARDS_COUNT = len(cards)


for value in copies.values():
    CARDS_COUNT += value["copies"]

print(f'Solution part 2: {CARDS_COUNT}')
