import os
import pandas as pd
import math

inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')
df = pd.read_csv(inputCsv)

def seatIdCalc(seatCodeStr):
    maxRows = 128
    row = list(range(0,maxRows))

    for char in seatCodeStr[0:7]:
        if char == 'F':
            row = row[0:math.floor(len(row)/2)]
        elif char == 'B':
            row = row[math.floor(len(row)/2):]
    row = row[0]

    maxSeats = 8
    seat = list(range(0,maxSeats))

    for char in seatCodeStr[7:]:
        if char == 'L':
            seat = seat[0:math.floor(len(seat)/2)]
        elif char == 'R':
            seat = seat[math.floor(len(seat)/2):]

    seat = seat[0]

    seatId = row*8+seat

    return seatId

df['SeatId'] = df['SeatCode'].apply(seatIdCalc)
df = df.sort_values(by='SeatId', ascending=True)
minSeatId = min(df['SeatId'])
maxSeatId = max(df['SeatId'])

print('Solution part 1: ', maxSeatId)

seats = range(minSeatId, maxSeatId, 1)

for seat in seats:
    if seat not in df['SeatId'].values:
        print('Solution part 2: ',seat)

