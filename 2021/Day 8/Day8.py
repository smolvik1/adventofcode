import os
inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
data = data.split('\n')

# Part 1
sol = data
for i, x in enumerate(sol):
    sol[i] = x.split('| ', 1)[1]

cnt = []  
for line in sol:
    lineList = list(line.split(' ', 3))
    lineList = list(filter(lambda x: (len(x) in [2, 3, 4, 7]), lineList ))
    cnt.append(len(lineList))

print(sum(cnt))