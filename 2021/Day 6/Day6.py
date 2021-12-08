import os
import numpy as np

inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')
fishes = np.loadtxt(inputTxt, delimiter=',')

def numberOfFish(fishes, days):
    if not isinstance(fishes, np.ndarray):
        fishes = np.array([fishes])

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


# Part 2

# Calculate a master list how many fish spawn based on start condition
noDays = 256
fishMaster = [list(range(0,9)), []]
for fish in fishMaster[0]:
    print('Calculating fish #: '+str(fish))
    fishMaster[1].append(numberOfFish(fish, noDays))

func = lambda x: fishMaster[1][int(x)]
v_func = np.vectorize(func)

test = v_func(fishes)

print(sum(test))

