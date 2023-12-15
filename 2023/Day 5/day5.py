import os

input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r", encoding="utf-8") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

parsed_data = {}
rng = []

seeds = list(map(int, data[0].split(": ")[1].split(' ')))


for i in range(1, len(data)):
    line = data[i]

    if line[0].isalpha():
        HEADER = line.split(sep=" map:")[0]
        FROM, TO = HEADER.split('-to-')

        rng = []

    if line[0].isdigit():
        rng.append(line.split(" "))

    parsed_data[HEADER] = {"map_from": FROM, "map_to": TO, "map": rng}


def calc_corresponding_value(key_item: str, from_value: int, parsed_dict: dict):
    """Function to create mapping table"""
    destination_value = from_value

    for lst in parsed_dict[key_item]['map']:
        destination_range_start = int(lst[0])
        source_range_start = int(lst[1])
        range_length = int(lst[2])
        diff = from_value - source_range_start

        source_range_end = source_range_start + range_length
        if (from_value >= source_range_start) and (from_value < source_range_end):
            return (destination_range_start + diff)

    return destination_value

locations = []

def calculate_location(seed):
    """Function to calculate location for a seed"""
    soil = calc_corresponding_value('seed-to-soil', seed, parsed_data)
    fertilizer = calc_corresponding_value('soil-to-fertilizer', soil, parsed_data)
    water = calc_corresponding_value('fertilizer-to-water', fertilizer, parsed_data)
    light = calc_corresponding_value('water-to-light', water, parsed_data)
    temperature = calc_corresponding_value('light-to-temperature', light, parsed_data)
    humidity = calc_corresponding_value('temperature-to-humidity', temperature, parsed_data)
    location = calc_corresponding_value('humidity-to-location', humidity, parsed_data)

    return location

for seed in seeds:
    locations.append(calculate_location(seed))

print(min(locations))

### Part 2

min_location = float('inf')
seeds = []
# Extracting numbers from the string
seed_numbers = [int(num) for num in data[0].split() if num.isdigit()]

# Creating tuples from pairs of numbers
seed_tuples = [(seed_numbers[i], seed_numbers[i + 1]) for i in range(0, len(seed_numbers), 2)]

for tup in seed_tuples:
    i = 0
    print(tup)
    
    while (i < tup[1]):
        seed = tup[0]
        location = calculate_location(seed)
        if location < min_location:
            min_location = location
        i += 1

        print(f'{i/tup[1]*100:.2%}')
        
print(min_location)

