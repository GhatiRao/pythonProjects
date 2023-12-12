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


def function(string: str):
    pprint(string)
#
#
# input_string = ["467..114..",
#                 "...*......"]
# ans = product(input_string[0], input_string[1])
# for e in ans:
#     print(e)
#
# 0/0
# width = len(input_string[0])-1
# length = len(input_string)-1
# print(width)
# print(length)
# print(input_string[length][width])
# for row in input_string:
#     ans = [int(s) for s in re.findall(r'\b\d+\b', row)]
#     print(ans)
#

with open("input.txt", 'r') as filehandle:
    input_text = filehandle.read()
    ans = input_text.splitlines()


print(f"input ----\n {ans}")


def get_neighbours():
    pass


for row, line in enumerate(ans):
    for match in re.finditer(r"\d+", line):
        print(match)
        print(int(match.group()))
        print(match.start(), match.end())

        chosen_cords = [(x_cords, y_cords) for y_cords, x_cords in product(
            range(row - 1, row + 2), range(match.start()-1, match.end()+2))
                        if (0 <= x_cords < len(line) and 0 <= y_cords <= len(ans) and
                            ((y_cords, x_cords) not in product([row], range(match.start(), match.end()+1))))]

        pprint(chosen_cords)
        0/0

