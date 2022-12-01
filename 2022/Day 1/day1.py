import os
import pandas as pd

inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')

with open(inputTxt, 'r') as f:
    data = f.read()
data = data.split('\n')

elfNumList = []
elfNum = 1

for i, calories in enumerate(data):
    if calories=='':
        elfNum += 1
        data[i] = -1  # Replace '' with -1    
    elfNumList.append(elfNum)

zipList = list(zip(data, elfNumList))

df = pd.DataFrame(zipList, columns=['Calories', 'Elf'])
df['Calories'] = df['Calories'].astype(int)
df = df[df['Calories'] != -1].reindex()  # Remove rows with -1

df_grouped = df.groupby('Elf').sum()
maxCal = df_grouped['Calories'].max()
print('Solution to part #1 is: '+str(maxCal)+' calories')  # Solution part #1

top3Cal = df_grouped.nlargest(3, columns=['Calories']).sum()[0]

print('Solution to part #2 is: '+str(top3Cal)+' calories')  # Solution part #2



