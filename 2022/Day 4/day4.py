import os
input = os.path.join(os.path.dirname(__file__),'input.txt')

groups = []
overlaps = []

def overlap(assignment1, assignment2):
    f1, t1 = [int(x) for x in assignment1.split('-')]
    f2, t2 = [int(x) for x in assignment2.split('-')]

    if ((f1 <= f2) and (t1 >= t2)) or ((f2 <= f1) and (t2 >= t1)):  # Full overlap
        return 1
    elif (t1 < f2) or (f1 > t2):  # No overlap
        return 0
    else:
        return 0.5  # Partly overlap

for line in open(input, 'r').read().splitlines():
    groups.append(line.split(','))

for group in groups:
    overlaps.append(overlap(group[0], group[1]))

print('Answer to part 1: ' + str(overlaps.count(1)))  # Groups with full overlap
print('Answer to part 2: ' + str(sum(map(lambda x: x >= 0.5, overlaps))))  # Groups with partly overlap
