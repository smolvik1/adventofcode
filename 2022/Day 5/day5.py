import os
import re

input = os.path.join(os.path.dirname(__file__), "input.txt")

total_stacks = int((len(open(input, "r").readline()) - 4) / 4 + 1)
logistics = []
instructions = []
crates = [""] * total_stacks


def command_transform(lst, m, f_stack, t_stack, maintain_order=False):
    crates = lst[f_stack][-m:]  # crates to be moved (e.g ZN)
    lst[f_stack] = lst[f_stack][:-m]
    if maintain_order:
        lst[t_stack] = lst[t_stack] + crates  # add crates, but keep order
    else:
        lst[t_stack] = lst[t_stack] + crates[::-1]  # add crates, but reverse order

    return lst


for line in open(input, "r").read().splitlines():
    if (len(line) != 0) and ("move" not in line) and (" 1" not in line):
        logistics.append(line)
    if "move" in line:
        instructions.append(line)

for y in reversed(range(0, int(len(logistics)))):  # loop from bottom to top
    for stack in range(0, total_stacks):
        x = 1 + stack * 4
        letter = logistics[y][x]
        if letter != " ":
            crates[stack] = crates[stack] + letter

crates_2 = crates.copy()

for instruction in instructions:
    # print(crates)
    instruction_list = re.findall(r"\b\d+\b", instruction)  # put numbers into a list
    instruction_list = [int(i) for i in instruction_list]  # convert to ints
    # print(instruction_list)
    crates = command_transform(
        crates, instruction_list[0], instruction_list[1] - 1, instruction_list[2] - 1
    )

    crates_2 = command_transform(
        crates_2,
        instruction_list[0],
        instruction_list[1] - 1,
        instruction_list[2] - 1,
        maintain_order=True,
    )

print("Answer to part 1: " + "".join([item[-1] for item in crates]))
print("Answer to part 2: " + "".join([item[-1] for item in crates_2]))
