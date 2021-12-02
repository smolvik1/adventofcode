import os
inputCsv = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputCsv, 'r') as f:
    data = f.read()
data = data.split('\n')
data = list(map(int, data))

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