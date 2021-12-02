import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

with open(inputCsv, 'r') as f:
    data = f.read().replace('+', '')
data = data.split('\n')


def seatBorder(dataSet, borderStr):
    for i in range(len(dataSet)):
        newRow = borderStr + dataSet[i] + borderStr
        dataSet[i] = newRow
    
    xDot = borderStr
    xBorderElements = len(dataSet[0])  # horizontal length + 2  
    xDot = xDot*xBorderElements

    dataSet.insert(0, xDot)
    dataSet.append(xDot)

    return dataSet

def seatChange(y, x, data):
    data2 = seatBorder(data, '.')  # Adds '.' border to the seat map
    x += 1
    y += 1
    row = data2[y][1:-1]
    seatVal = data2[y][x]

    seatValN = data2[y-1][x]
    seatValNE = data2[y-1][x+1]
    seatValE = data2[y][x+1]
    seatValSE = data2[y+1][x+1]
    seatValS = data2[y+1][x]
    seatValSW = data2[y+1][x-1]
    seatValW = data2[y][x-1]
    seatValNW = data2[y-1][x-1]

    adjacentSeats = [seatValN, seatValNE, seatValE, seatValSE, seatValS, seatValSW, seatValW, seatValNW]

    if (seatVal == 'L') & (adjacentSeats.count('L') == 8):
        seatVal = '#'
    elif (seatVal == '#') & (adjacentSeats.count('#') >= 4):
        seatVal = 'L'
    
    return seatVal


for i in range(0, 1):#len(data)-1):
    seatsChanged = 0
    for j in range(0, len(data[i])-1): 

        row = data[i]
        seatValOld = data[i][j] 
        seatValNew = seatChange(i, j, data)
        
        if (seatValNew != seatValOld):
            seatsChanged += 1
            if j == (len(row)-1):
                row = row[0:j] + seatValNew
            else:
                row = row[0:(j-1)] + seatValNew + row[(j+1):]  # Add new seat value

        print(i, j, row)

