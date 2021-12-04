import os
inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
data = data.split('\n')

# Task 1
y, x = 0, 0

for i, dirStr in enumerate(data):
    direction, value = dirStr.split(' ', 1)
    value = int(value)

    if direction == 'up':
        y += -value
    elif direction == 'down':
        y += value
    else:
        x += value

print(x, y, x*y)

# Task 2
y, x, aim = 0, 0, 0

for i, dirStr in enumerate(data):
    direction, value = dirStr.split(' ', 1)
    value = int(value)

    if direction == 'up':
        aim += -value
    elif direction == 'down':
        aim += value
    else:
        x += value
        y += aim*value
    
print(x, y, x*y)
