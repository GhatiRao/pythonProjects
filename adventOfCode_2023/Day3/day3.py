"""
The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because
they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
 Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger.
What is the sum of all of the part numbers in the engine schematic?
"""

import pandas as pd
from pprint import pprint
from itertools import product
import re

with open("input.txt", 'r') as filehandle:
    input_text = filehandle.read()
    ans = input_text.splitlines()

print(f"input ----\n {ans}")

numbers_considered = []
for row, line in enumerate(ans):
    for match in re.finditer(r"\d+", line):
        """
        re.finditer is an iterable and consists (match, match start = , match end = , match value = ) 
        """
        print(int(match.group()))

        """
        Extracts the immediate neighbor of the identified number in the row
        """
        neighbor_cords = [(x_cords, y_cords) for y_cords, x_cords in product(
            range(row - 1, row + 2), range(match.start()-1, match.end()+1))
                        if (0 <= x_cords < len(line) and 0 <= y_cords < len(ans) and
                            ((y_cords, x_cords) not in product([row], range(match.start(), match.end()))))]

        """
        Checks if there is an alphanumeric char apart from '*' in the neighbor
        """
        if any(not ans[row_neighb][col_neighb].isalnum() and ans[row_neighb][col_neighb] != '.' for
               col_neighb, row_neighb in neighbor_cords):
            numbers_considered.append(int(match.group()))

print("------\n")
pprint(numbers_considered)


print("------\n")
print(sum(numbers_considered))