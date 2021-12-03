import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputCsv, 'r') as f:
    data = f.read()
data = data.split('\n')
data = list(map(int, data))

# Part 1
trend = []

for i, x in enumerate(data):
    if i == 0: # Pass the first index
        trend.append('N/A')
    else:
        prev = data[i-1]
        if x > prev:
            trend.append('Increasing')
        else:
            trend.append('Decreasing')
        
print(trend.count('Increasing'))

# Part 2
sumArr = [sum(data[0:3])]
trend = ['N/A']

for i in range(1, len(data)-2, 1):
    sumPrev = sumArr[i-1]
    sumCurr = sum(data[i:i+3])

    if (sumCurr > sumPrev):
        trend.append('increased')
    elif (sumCurr == sumPrev):
        trend.append('no change')
    else:
        trend.append('decreased')

    sumArr.append(sumCurr)
   
print(trend.count('increased'))

