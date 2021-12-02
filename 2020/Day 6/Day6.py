import os
import pandas as pd
import string

inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')
#a_file = open(inputCsv)
#file_contents = a_file.read()

with open(inputCsv, 'r') as f:
    data = f.read().replace('\n', ',').replace(',,', '\n').replace(' ', ', ').replace(', ', ',')
data = data.split('\n')

cnt = 0

for i in data:
    txt = i.replace(',', '')
    cnt +=(len(set(txt)))

print('Solution to part 1: ',cnt)

alphabet = list(string.ascii_lowercase)

cnt = 0

data2 = ['abc', 'a,b,c', 'ab,ac', 'a,a,a,a', 'b']

for i in data:
    persons = i.count(',')+1

    for letter in alphabet:
        letterOccurrence = i.count(letter)

        if letterOccurrence == persons:
            cnt += 1

print('Solution to part 2: ',cnt)

