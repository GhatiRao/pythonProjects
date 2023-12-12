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
What is the sum of all the part numbers in the engine schematic?


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

        #re.finditer is an iterable and consists (match, match start = , match end = , match value = )

        print(int(match.group()))


        # Extracts the immediate neighbor of the identified number in the row
        neighbor_cords = [(x_cords, y_cords) for y_cords, x_cords in product(
            range(row - 1, row + 2), range(match.start()-1, match.end()+1))
                        if (0 <= x_cords < len(line) and 0 <= y_cords < len(ans) and
                            ((y_cords, x_cords) not in product([row], range(match.start(), match.end()))))]

        # Checks if there is an alphanumeric char apart from '*' in the neighbor
        if any(not ans[row_neighb][col_neighb].isalnum() and ans[row_neighb][col_neighb] != '.' for
               col_neighb, row_neighb in neighbor_cords):
            numbers_considered.append(int(match.group()))

print("------\n")
pprint(numbers_considered)


print("------\n")
print(sum(numbers_considered))
"""

"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! 
As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.
You don't seem to be going very fast, though. Maybe something is still wrong? 
Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.
Before you can explain the situation, she suggests that you look out the window. 
There stands the engineer, holding a phone in one hand and waving with the other. 
You're going so slowly that you haven't even left the station. You exit the gondola.
The missing part wasn't the only issue - one of the gears in the engine is wrong. 
A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.
This time, you need to find the gear ratio of every gear and add them all up so that 
the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; 
it has part numbers 467 and 35, so its gear ratio is 16345. 
The second gear is in the lower right; its gear ratio is 451490. 
(The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

"""
Sourced from below link :
https://github.com/SlowFlo/advent_of_code_2023/blob/main/Day%203%20-%20Gear%20Ratios/part%202/gear_ratios.py
"""
from pprint import pprint
from itertools import product
import re

with open("input.txt", 'r') as filehandle:
    input_text = filehandle.read()
    ans = input_text.splitlines()

print(f"input ----\n {ans}")
def get_check_coords(
    lines: list[str], line_coord: int, match: re.Match
) -> tuple[tuple[int, int], ...]:
    def in_range(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])

    return tuple(
        (check_line_coord, check_char_coord)
        for check_line_coord, check_char_coord in product(
            range(line_coord - 1, line_coord + 2),
            range(match.start() - 1, match.end() + 1),
        )
        if in_range(check_line_coord, check_char_coord)
        and (check_line_coord, check_char_coord)
        not in product([line_coord], range(match.start(), match.end()))
    )


def get_coordinates_to_check(
    multi_lines_str: str,
) -> dict[int, list[tuple[tuple[int, int]], ...]]:
    lines = multi_lines_str.splitlines()
    coordinates = {}

    for line_coord, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            number = int(match.group(0))
            check_coords = get_check_coords(lines, line_coord, match)
            coordinates.setdefault(number, []).append(tuple(check_coords))

    return coordinates


coordinates_to_check = get_coordinates_to_check(input_text)
print("Coords")
pprint(coordinates_to_check)
lines = input_text.splitlines()

potential_gears_coord = {}
gears_ratios = []
for number, coordinates_list in coordinates_to_check.items():
    for coordinates in coordinates_list:
        for line_coord, char_coord in coordinates:
            if lines[line_coord][char_coord] == "*":
                potential_gears_coord.setdefault(
                    (line_coord, char_coord), []
                ).append(number)

for numbers in potential_gears_coord.values():
    if len(numbers) == 2:
        gears_ratios.append(product(numbers))

