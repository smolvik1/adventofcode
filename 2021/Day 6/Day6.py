import os
import numpy as np

inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')
fishes = np.loadtxt(inputTxt, delimiter=',')

def numberOfFish(fishes, days):
    min1 = lambda x: (x-1) if (x > 0) else 6
    v_min1 = np.vectorize(min1)

    for day in range(0, days):
        newFish = np.count_nonzero(fishes==0)  # Fishes to be born
        fishes = v_min1(fishes)
        if newFish > 0:
            fishes = np.append(fishes, [8]*newFish, axis=0)  # Add newborn fish
        #print('Day '+str(day+1)+": "+str(fishes.size)+" fish")
    
    return fishes.size

# Part 1
print(numberOfFish(fishes, 80))