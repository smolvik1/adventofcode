import os
input = os.path.join(os.path.dirname(__file__),'input.txt')

bags = open(input, 'r').read().splitlines()
errors = []

def value(letter):
    if letter.isupper():
        value = ord(letter) - 38
    elif letter.islower():
        value = ord(letter) - 96
    return value

def valueError(comp1, comp2):
    itemError = []
    itemErrorValue = 0

    for item in comp1:
        if (item in comp2) and (item not in itemError):
            itemError.append(item)
            itemErrorValue += value(item)
    return itemErrorValue

for i, bag in enumerate(bags):
    comp_items = int(len(bag)/2)  # Items in each compartment
    bags[i] = [bag[0:comp_items], bag[comp_items:]]  # Split the bag into two compartments
    errors.append(valueError(bags[i][0], bags[i][1]))

print('Solution to part 1: ' + str(sum(errors)))

def badgeFinder(bag1, bag2, bag3):
    badge = ''
    badgeValue = 0
    for item in bag1:
        if (item in bag2) and (item in bag3):
            badge = item
            badgeValue = value(badge)
    return badgeValue

badgeValues = []
for group in range(0, int(len(bags)/3)):
    groupbags = bags[(3*group):(3*group)+3]
    badgeValue = badgeFinder(''.join(groupbags[0]), ''.join(groupbags[1]), ''.join(groupbags[2]))
    badgeValues.append(badgeValue)

print('Solution to part 2: ' + str(sum(badgeValues)))