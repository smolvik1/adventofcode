
import numpy as np
import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

seats = open(inputCsv,'r').read().split('\n')

plan = []

for row in seats:
    l = list(row)
    plan.append(l)

seatplan = np.array(plan)
row_length = len(seatplan[1])
new_seatplan = np.where(seatplan == 'L', 'K', seatplan)
iteration = 0

while (new_seatplan==seatplan).all() == False:
    seatplan = new_seatplan.copy()
    #print('Iteration:', iteration)

    # Check corners
    corner = seatplan[0:2,0:2]
    if '#' not in corner and seatplan[0,0] !='.':
        new_seatplan[0,0] = '#'    
    corner = seatplan[0:2,row_length-2:row_length]
    if '#' not in corner and seatplan[0,row_length-1] !='.':
        new_seatplan[0,row_length-1] = '#'
    corner = seatplan[len(seatplan)-2:len(seatplan), 0:2]
    if '#' not in corner and seatplan[len(seatplan)-1,0] != '.':
        new_seatplan[len(seatplan)-1,0] = '#'
    corner = seatplan[len(seatplan)-2:len(seatplan),row_length-2:row_length]
    if '#' not in corner and seatplan[len(seatplan)-1,row_length-1] != '.':
        new_seatplan[len(seatplan)-1,row_length-1] = '#'

    # Check first row
    for i in range(0, row_length-1):
        arr = seatplan[0:2,i:i+3]
        focus = arr[0,1]
        occupied = np.count_nonzero(arr == '#')
        if '#' not in arr and focus !='.':
            new_seatplan[0,i+1] = '#'
        elif focus == '#' and occupied > 4:
            new_seatplan[0,i+1] = 'L'

    # Check last row
    for i in range(0, row_length-1):
        arr = seatplan[len(seatplan)-2:len(seatplan),i:i+3]
        focus = arr[1,1]
        occupied = np.count_nonzero(arr == '#')
        if '#' not in arr and focus !='.':
            new_seatplan[len(seatplan)-1,i+1] = '#'
        elif focus == '#' and occupied > 4:
            new_seatplan[len(seatplan)-1,i+1] = 'L'

    # Check first column
    for i in range(0, len(seatplan)-1):
        arr = seatplan[i:i+3,0:2]
        focus = arr[1,0]
        occupied = np.count_nonzero(arr == '#')
        if '#' not in arr and focus !='.':
            new_seatplan[i+1,0] = '#'
        elif focus == '#' and occupied > 4:
            new_seatplan[i+1,0] = 'L'

    # Check last column
    for i in range(0, len(seatplan)-1):
        arr = seatplan[i:i+3,row_length-2:row_length]
        focus = arr[1,1]
        occupied = np.count_nonzero(arr == '#')
        if '#' not in arr and focus !='.':
            new_seatplan[i+1,row_length-1] = '#'
        elif focus == '#' and occupied > 4:
            new_seatplan[i+1,row_length-1] = 'L'

    # Check the rest
    for row in range(0, len(seatplan)-1):
        for seat in range(0, row_length-1):
            arr = seatplan[row:row+3, seat:seat+3]
            focus = arr[1,1]
            occupied = np.count_nonzero(arr == '#')
            if '#' not in arr and focus !='.':
                new_seatplan[row+1, seat+1] = '#'
            elif focus == '#' and occupied > 4:
                new_seatplan[row+1, seat+1] = 'L'

    iteration += 1

occupied = np.count_nonzero(new_seatplan == '#')
print('Occupied seats:', occupied)