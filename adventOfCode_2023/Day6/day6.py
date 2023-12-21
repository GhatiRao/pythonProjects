

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


