import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

with open(inputCsv, 'r') as f:
    data = f.read().replace('+', '')
data = data.split('\n')

for i in range(0,len(data)):
    data[i] = int(data[i])

def validCheck(number, subsetData):
    validNumbers=[]
    for nmbr in subsetData:
        for nmbr2 in subsetData:
            if nmbr != nmbr2:
                validNumber = nmbr+nmbr2
                validNumbers.append(validNumber)

    if number in validNumbers:
        valid = True
    else:
        valid = False

    return valid, validNumbers

preamble = 25
row = preamble
valid = True


while valid:
    number = data[row]
    subsetData = data[(row-preamble):row]
    valid, validNumbers = validCheck(number, subsetData)
    
    if not valid:
        firstInvalid = number
        print('The first invalid number is ', firstInvalid)
        break

    row += 1


##########
# Part 2 #
##########
def contiguousSumList(number, data):
    contiguousList = []
    for i in range(0, len(data)):
        for j in range(i, len(data)):
            sumTotal = sum(data[i:j])
            if (sumTotal == number) & (len(data[i:j]) >= 2):
                minValue = min(data[i:j])
                maxValue = max(data[i:j])
                sol = minValue + maxValue
                contiguousList = data[i:j]
            
    return sol, contiguousList

sol, smpl = contiguousSumList(firstInvalid, data)
print('Answer to part #2: ', sol)

