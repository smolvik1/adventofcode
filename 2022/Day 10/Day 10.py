import os
from itertools import accumulate
import textwrap

input = os.path.join(os.path.dirname(__file__), "input.txt")

instructions = []

for line in open(input, 'r').read().splitlines():
    instructions.append(line)

register_values = []

for i, instruction in enumerate(instructions):
    if i == 0:
        register_values.append(1)
    
    if instruction.split()[0] == 'addx':
        register_values.extend([0, int(instruction.split()[1])])
    
    if instruction.split()[0] == 'noop':
        register_values.extend([0])

register_values = list(accumulate(register_values))

sol1 = sum([i * register_values[i-1] for i in range(20, len(register_values), 40)])
print('Solution to part 1: ' + str(sol1))

screen = ''
width = 40
for i in range(0, len(register_values)-1):
    sprite = register_values[i]
    if (sprite - 1) <= (i % width) and (i % 40) <= (sprite + 1):
        screen += '#'
    else:
        screen += '.'
        
print(textwrap.fill(screen, width))  # EALGULPG
