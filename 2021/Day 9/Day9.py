import os
inputTxt = os.path.join(os.path.dirname(__file__),'inputSample.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
hmap = data.split('\n')

def addBorder(inList, borderStr):
    outList = list(map(lambda x: borderStr+x+borderStr, inList))
    xlen = len(outList[0])
    outList.insert(0, borderStr*xlen)
    outList.append(borderStr*xlen)

    return outList

# Part 1 and Part 2
hmap = addBorder(hmap, '9')  # map now has 9 borders all around
#hmap = list(map(int, hmap))  # convert to integers
lowPoints = []
basins = []

for j in range(1, len(hmap)-1):
    for i in range(1, len(hmap[0])-1):
        val = int(hmap[j][i])
        left = int(hmap[j][i-1])
        right = int(hmap[j][i+1])
        up = int(hmap[j-1][i])
        down = int(hmap[j+1][i])

        if all(adjacent > val for adjacent in [left, right, up, down]):
            lowPoints.append(val)

riskLevel = list(map(lambda x: x+1, lowPoints))
print(sum(riskLevel))




