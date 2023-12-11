"""
As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.


def function(string):
    number = ""
    length = len(string)
    for index, num in enumerate(string):
        # if index == length/2:
        #     break
        if num.isnumeric():
            number += num
            break
    for index, num in enumerate(string[::-1]):
        #
        # if index == length/2:
        #     break
        if num.isnumeric():
            number += num
            break
    if len(number) == 1:
        number += number
    print(number)
    return number


answers = []
with open("input.txt", 'r') as filehandle:
    for line in filehandle:
        ans = function(line)
        answers.append(int(ans))


print(len(answers))
print(sum(answers))
"""

"""
Your puzzle answer was 53334.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

zero = "zero"
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"
words = [zero, one, two, three, four, five, six, seven, eight, nine]
words_dict = {'zero': 0,
              'one': 1,
              'two': 2,
              'three': 3,
              'four': 4,
              'five': 5,
              'six': 6,
              'seven': 7,
              'eight': 8,
              'nine': 9
              }


def function(string: str) -> str:
    number = ""
    length = len(string)
    index_words_forward = [string.find(num_in_word) for num_in_word in words]
    index_words_backward = [string.rfind(num_in_word) for num_in_word in words]
    print(index_words_forward)
    print(index_words_backward)

    for index, num in enumerate(string):
        if num.isnumeric():
            number += num
            break
        if index in index_words_forward:
            index_found = index_words_forward.index(index)
            number += str(words_dict[words[index_found]])
            break

    for index, num in enumerate(string[::-1]):
        index = length - 1 - index
        if num.isnumeric():
            number += num
            break
        if index in index_words_backward:
            index_found = index_words_backward.index(index)
            number += str(words_dict[words[index_found]])
            break
    if len(number) == 1:
        number += number
    print(number)
    return number




answers = []
with open("input.txt", 'r') as filehandle:
    for line in filehandle:
        ans = function(line)
        answers.append(int(ans))

print(answers)
print(sum(answers))