import os
import numpy as np

inputTxt = os.path.join(os.path.dirname(__file__),'input.txt')
pos = np.loadtxt(inputTxt, delimiter=',')

# Part 1
target = round(np.median(pos))
fuelConsumption = lambda x: abs(x-target)
v_fuel = np.vectorize(fuelConsumption)

fuelSpent = v_fuel(pos)
print(sum(fuelSpent))

# Part 2
targetGuess = round(np.average(pos))

for target in [targetGuess-1, targetGuess, targetGuess+1]:
    fuelConsumption = lambda x: 0.5*abs(x-target)**2 + 0.5*abs(x-target)
    v_fuel = np.vectorize(fuelConsumption)

    fuelSpent = v_fuel(pos)
    print("Target: "+str(target)+". Fuel spent: "+str(sum(fuelSpent)))
