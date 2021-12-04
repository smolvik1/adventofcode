import os
inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
data = data.split('\n')

# Part 1
gammaBin, epsilonBin = '', ''

for x in range(0, len(data[0])):
    zeroCount, oneCount = 0, 0

    for y in range(0, len(data)):
        val = int(data[y][x])
        if val == 0:
            zeroCount += 1
        else:
            oneCount +=1
    
    if (oneCount > zeroCount):
        gammaBin += '1'
        epsilonBin += '0'
    else:
        gammaBin += '0'
        epsilonBin += '1'

gamma = int(gammaBin, 2)
epsilon = int(epsilonBin, 2)

print(gamma * epsilon)

#Part 2
dataSearch = data

def listWithLetterInPos(dataList, mostCommon=True):
    searchList = dataList
    for x in range(0, len(searchList[0])):
        zeroCount, oneCount = 0, 0

        for y in range(0, len(searchList)):
            val = searchList[y][x]
            if val == '0':
                zeroCount += 1
            else:
                oneCount +=1

        if mostCommon:
            if (oneCount >= zeroCount):
                bitVal = '1'
            else:
                bitVal = '0'
        else:
            if (oneCount >= zeroCount):
                bitVal = '0'
            else:
                bitVal = '1'
        
        if len(searchList) > 1:
            searchList = list(filter(lambda str: str[x] == bitVal, searchList))

    bitStr = searchList[0]
    return int(bitStr, 2)

o2 = listWithLetterInPos(data)
co2 = listWithLetterInPos(data, mostCommon=False)

print(o2*co2)