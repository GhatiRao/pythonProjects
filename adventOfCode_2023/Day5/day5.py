"""
----input
seeds: 79 14 55 13

soil-to-fertilizer map:
Soil  Seed  Count (Incl of Seed)
50      98      2
52      50      48

fertilizer-to-water map:
water-to-light map:
light-to-temperature map:
temperature-to-humidity map:
humidity-to-location map:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51

With this map, you can look up the soil number required for each initial seed number:
Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.

What is the lowest location number that corresponds to any of the initial seed numbers?
- Find the closest Location for the input **seeds**


from pprint import pprint as pp
import re
from collections import defaultdict
with open("input.txt", "r") as file:
    input_text = file.read()
_, seeds, *mapping_list = re.split(
    'seeds: |'
    '\nseed-to-soil map:\n|'
    '\nsoil-to-fertilizer map:\n|'
    '\nfertilizer-to-water map:\n|'
    '\nwater-to-light map:\n|'
    '\nlight-to-temperature map:\n|'
    '\ntemperature-to-humidity map:\n|'
    '\nhumidity-to-location map:\n', input_text)


def fun(seed: str, map_data: str):
    for line in map_data.splitlines():

        destination, source, range_incl = [int(x) for x in line.split(' ')]

        if source <= seed < source+range_incl:
            return destination + seed - source
    return seed


new = []
seeds = [int(x) for x in seeds.split(' ')]

for seed in seeds:
    local = seed
    for items in mapping_list:
        link_found = fun(local, items)
        local = link_found
    new.append(local)

print(min(new))

"""


# Instead of 4 initial seeds, there is a [ starting_seed1, range1, starting_seed2, range2.. ]
# find the nearest 'location' amongst all the input seeds.
# https://www.youtube.com/watch?v=iqTopXV13LE


import re
with open("input.txt", "r") as file:
    input_text = file.read()
_, seeds, *mapping_list = re.split(
    'seeds: |'
    '\nseed-to-soil map:\n|'
    '\nsoil-to-fertilizer map:\n|'
    '\nfertilizer-to-water map:\n|'
    '\nwater-to-light map:\n|'
    '\nlight-to-temperature map:\n|'
    '\ntemperature-to-humidity map:\n|'
    '\nhumidity-to-location map:\n', input_text)


seeds = [int(x) for x in seeds.split(' ')]
# This is the list[(val1, val2)]; val1 = original seed, val2 = end of range seed
min_max_seeds = list(map(lambda x: (x[0], x[0]+x[1]), zip(seeds[::2], seeds[1::2])))
print(min_max_seeds)


def fun(seed: str, min_val_seed, max_val_seed, map_data: str):
    for line in map_data.splitlines():
        soil_dest, seed_source, range_incl = [int(x) for x in line.split(' ')]
        seed_final = [seed_source, seed_source + range_incl] # 98, 99



        if source <= seed < source+range_incl:
            return destination + seed - source
    return seed


for min_seed, max_seed in min_max_seeds:
    for items in mapping_list:
        link_found = fun(local, min_seed, max_seed, items)
        local = link_found
    new.append(local)

print(min(new))









