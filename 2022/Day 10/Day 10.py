import os
from itertools import accumulate

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

signals = []
for cycle, register_value in enumerate(register_values):
    signals.append(cycle*register_values[cycle-1])

print('Solution to part 1: '+ str(sum([signals[20], signals[60], signals[100], signals[140], signals[180], signals[220]])))

