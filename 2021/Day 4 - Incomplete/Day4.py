import os
inputTxt = os.path.join(os.path.dirname(__file__),'inputSample.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
data = data.split('\n')

drawList = data[0]
bingoBoards = []
bingoBoard = []

for i, x in enumerate(data[2:]):
    if x != '':
        bingoBoard.append(x)
    else:
        bingoBoards.append(bingoBoard)
        bingoBoard = []
bingoBoards.append(bingoBoard)

bingoBoards = [[row.lstrip() for row in bingoBoard] for bingoBoard in bingoBoards]


bingoStatus = [list(map(lambda x: '0 0 0 0 0', bingoBoard)) for bingoBoard in bingoBoards]

print(bingoBoards[0])
def checkBingoBoard(bingoBoard, number=-1):
    for i, x in enumerate(bingoBoard):
        row = x.split(' ')
        print(row)

checkBingoBoard(bingoBoards[0])