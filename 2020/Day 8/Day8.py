import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

with open(inputCsv, 'r') as f:
    data = f.read().replace('+', '')
data = data.split('\n')

def testCheck(data):
    row = 0
    accumulator = 0
    converged = False
    rowsVisited=[]

    while not converged:
        cmd, val = data[row].split(' ')

        if row in rowsVisited:
            converged = False
            break
        elif row == (len(data)-1):
            rowsVisited.append(row)
            converged = True
            if (cmd=='acc'):
                accumulator += int(val)
            break
        else:
            rowsVisited.append(row)       

        if (cmd=='acc'):
            accumulator += int(val)
            row += 1  # continue to next row

        if (cmd=='jmp'):
            row += int(val)  # jump the specified number of rows

        if (cmd=='nop'):
            row += 1  # continue to next row
    
    return accumulator, converged
        
accumulator, converged = testCheck(data)

print('Answer to part #1: ', accumulator)

for row in list(range(0,len(data)-1)):
    data2 = data.copy()
    cmd0, val0 = data2[row].split(' ')
    
    if (cmd0 == 'jmp'):
        data2[row] = 'nop'+' '+val0
    elif (cmd0 == 'nop'):
        data2[row] = 'jmp'+' '+val0

    accumulator, converged = testCheck(data2)

    if converged:
        print('Answer to part #2:', accumulator)
        break
    
