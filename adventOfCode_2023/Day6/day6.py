

import re
with open("input.txt", "r") as file:
    input_text = file.read().splitlines()
print(input_text)
input_text_processed = [re.findall(r'\d+', i) for i in input_text]
max_time_distance_pairs = list(zip(input_text_processed[0], input_text_processed[1]))
print(max_time_distance_pairs)


wins = 1
for max_time, max_dist in max_time_distance_pairs:
    count = 0
    max_time = int(max_time)
    max_dist = int(max_dist)
    for hold_the_button in range(max_time):
        remaining = max_time - hold_the_button
        dist_traveled = remaining*hold_the_button
        if dist_traveled > max_dist:
            count += 1
    print(count)
    wins *= count

    print("--------\n")

print(wins)


from collections import Counter
import re
with open("input.txt", "r") as file:
    input_text = file.read().splitlines()
print(input_text)

hands, values = [[i.split(" ")[0] for i in input_text], [int(i.split(" ")[1]) for i in input_text]]


def type_hand(string: str):
    a = Counter(string)
    print(a)
    if len(a) == 1:  # Five of a kind
        return 6
    if len(a) == 2 and max(a.values()) == 4:  # 'AAAA3' # Four of a kind
        return 5
    if len(a) == 2 and max(a.values()) == 3 and min(a.values()) == 2:  # 'AAA33' # Full house
        return 4
    if len(a) == 3 and max(a.values()) == 3:  # 'AAA32' # Three of a kind
        return 3
    if max(a.values()) == 2 and len(a) == 3:  # 'AAK33' # Two pair
        return 2
    if max(a.values()) == 2 and len(a) == 4:  # 'AA123' # One pair
        return 1
    return 0  # "23456" # High card


for hand in hands:
    print(type_hand(hand))


a = [ '234', 'K545']


