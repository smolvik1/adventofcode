import pandas as pd
import os
import re

inputCsv = os.path.join(os.path.dirname(__file__),'input.csv')

a_file = open(inputCsv)
file_contents = a_file.read()

with open(inputCsv, 'r') as f:
    data = f.read().replace('\n', ',').replace(',,', '\n').replace(' ', ', ').replace(', ', ',')
data = data.split('\n')

def validCheck(dictInput):
    validKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if all(validKey in dictInput for validKey in validKeys):
        valid = 1
    else:
        valid = 0
    
    return valid

validPassports = 0

for i in data:
    dictInput = dict(item.split(":") for item in i.split(","))
    validPassports = validPassports + validCheck(dictInput)

print('Valid passports for part 1 is: ',validPassports)


validPassports = 0

def validCheck2(dictInput):
    validKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if all(validKey in dictInput for validKey in validKeys):
        # Added conditions
        byrCond = (1920 <= int(dictInput['byr']) <= 2002)
        iyrCond = (2010 <= int(dictInput['iyr']) <= 2020)
        eyrCond = (2020 <= int(dictInput['eyr']) <= 2030)
        
        hgt = dictInput['hgt']
        hgtUnit = hgt[-2:]  # Gets last two (characters), cm or in
        hgtValue = hgt[:len(hgt)-2]

        if (hgtValue.isnumeric()) & (hgtUnit.isnumeric is not True):
            if (hgtUnit == 'cm') & (150 <= int(hgtValue) <= 193):
                hgtCond = True
            elif (hgtUnit == 'in') & (59 <= int(hgtValue) <= 76):
                hgtCond = True
            else:
                hgtCond = False
        else:
                hgtCond = False
        
        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', dictInput['hcl']):
            if len(dictInput['hcl'])==7:
                hclCond = True
            else:
                hclCond = False
        else:
            hclCond = False
        
        eclCond = dictInput['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        
        pid = dictInput['pid']
        if (len(pid)==9) & pid.isnumeric():
            pidCond = True
        else:
            pidCond = False
        
        if byrCond & iyrCond & eyrCond & hgtCond & hclCond & eclCond & pidCond:
            valid = 1
        else:
            valid = 0
    else:
        valid = 0
    
    return valid

for i in data:
    dictInput = dict(item.split(":") for item in i.split(","))
    validPassports = validPassports + validCheck2(dictInput)

print('Valid passports for part 2 is: ',validPassports)