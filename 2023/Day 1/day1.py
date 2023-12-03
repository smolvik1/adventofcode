import os

input_file = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_file, "r") as f:
    data = f.read()

data = data.split("\n")


valid_str_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_spelled_numbers_with_numbers(word: str) -> str:
    i = 0
    new_word = ""
    while i < len(word):
        search_area = word[i : len(word)]

        for key, replacement in valid_str_digits.items():
            if search_area.startswith(key):
                new_word = new_word + replacement
                break

        if not search_area.startswith(tuple(valid_str_digits.keys())):
            new_word = new_word + word[i]

        i += 1

    return new_word


data = [replace_spelled_numbers_with_numbers(word) for word in data]


calibration = 0

for row in data:
    digit_str = "".join(str(letter) for letter in row if letter.isdigit())
    relevant_digit = int(digit_str[0] + digit_str[-1])
    calibration += relevant_digit

print(calibration)
