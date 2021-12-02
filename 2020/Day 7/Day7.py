import os
import pandas as pd
import numpy as np
import string

inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

with open(inputCsv, 'r') as f:
    data = f.read()#.replace('no', '0')
data = data.split('\n')


for i in data:
    firstBagEnd = i.find('contain')-6
    firstBagName = i[0:firstBagEnd]

    bagNumberAllowedList = [int(s) for s in i.split() if s.isdigit()]
    bagsInFirstBag = len(bagNumberAllowedList)

    searchStart = len(firstBagName)
    for j in range(0,bagsInFirstBag-1):
        jBagStart1 = i.find(',', start=searchStart)
        jBagEnd1 = i.find(' ', start=searchStart)
        jBagName1 = i[(jBagStart1+3):jBagEnd1]

        print(jBagName1)

    #for bagNameNumber in bagNameCount-1:
    #    bag[bagNameNumber+1] = 
        

    print(bagNumberAllowedList, bagsInFirstBag)



