import pandas as pd
import math
import os

inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')
df = pd.read_csv(inputCsv)

xPatLength = len(df['map'][0])
yPatLength = len(df)

xMovePat = 1
yMovePat = 2
xScaleFactor = math.ceil(yPatLength/xPatLength*xMovePat/yMovePat)

df['map'] = df['map']*xScaleFactor  # Expanding the "map" in x-direction

x = 0  # start x-coordinate
y = 0  # start y-coordinate
treeCount = 0  # start tree count

while y < yPatLength:
    dfVal = df.iloc[y]['map'][x]  # returns # or .
    
    if dfVal == '#':
        treeCount = treeCount + 1

    y = y + yMovePat
    x = x + xMovePat

print('Solution to part #1: ', treeCount, 'trees will be hit by traversing ', xMovePat, 'to the left and ', yMovePat,' vertically')

#slopes = pd.DataFrame([[1, 1], [3, 1], [5, 1], [7,1], [1,2]])