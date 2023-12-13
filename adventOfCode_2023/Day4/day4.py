from pprint import pprint
# lines = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#          "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#          "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#          "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#          "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#          "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

"""with open("input.txt", "r") as file:
    input_text = file.read()
lines = input_text.splitlines() # -> ["Card 1: ...", "Card 2:...", ..]

points_total = 0
for line in lines:
    winning_details, our_hand = line.split("|")
    card_number, winning_numbers = winning_details.split(":")
    card_number, winning_numbers, our_hand = list(map(lambda x: x.strip(), [card_number, winning_numbers, our_hand]))
    # pprint([card_number, winning_numbers, our_hand])

    common = set(our_hand.split()).intersection(winning_numbers.split())
    # pprint(common)
    if len(common) >= 1:
        points = 2**(len(common)-1)
        # print(points)
        points_total += points

print(points_total)
"""
# ------------------ QUESTION 2 ------------------
# FROM https://github.com/SlowFlo/advent_of_code_2023/blob/main/Day%204%20-%20Scratchcards/part%202/scratchcards.py
"""
import re


class Scratchcard:
    def __init__(self, card: str):
        card_id, winning_numbers, numbers_i_have = re.split(r"[:|]", card)

        self.id = int(card_id.split()[1])
        self.winning_numbers = set(
            int(winning_number) for winning_number in winning_numbers.split()
        )
        self.numbers_i_have = set(
            int(numbers_i_have) for numbers_i_have in numbers_i_have.split()
        )
        self.winning_numbers_i_have = self.winning_numbers.intersection(
            self.numbers_i_have
        )

    def get_points(self) -> int:
        if not self.winning_numbers_i_have:
            return 0

        return 2 ** (len(self.winning_numbers_i_have) - 1)

    def get_copies_id(self) -> tuple[int, ...]:
        return tuple(
            self.id + index + 1 for index, _ in enumerate(self.winning_numbers_i_have)
        )


class PileOfScratchcards:
    def __init__(self, multi_lines_str: str):
        self.cards = [Scratchcard(line) for line in multi_lines_str.splitlines()]

    def get_total_points(self) -> int:
        total_points = 0

        for card in self.cards:
            total_points += card.get_points()

        return total_points

    def get_number_of_copies(self) -> dict[int, int]:
        number_of_copies = {card.id: 1 for card in self.cards}

        for card in self.cards:
            for _ in range(number_of_copies[card.id]):
                for copy_id in card.get_copies_id():
                    number_of_copies[copy_id] += 1

        return number_of_copies


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The pile of scratchcards is worth",
            PileOfScratchcards(input_text).get_total_points(),
            "in total.",
        )
        print(
            "At the end I have",
            sum(PileOfScratchcards(input_text).get_number_of_copies().values()),
            "cards.",
        )
"""

# From https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/4.py

from collections import defaultdict
with open("input.txt", "r") as file:
    input_text = file.read()
lines = input_text.splitlines()
# lines = ["Card 1: ...", "Card 2:...", ..]

# numbers = defaultdict(class : int, {})
numbers = defaultdict(int)

for card_number, line in enumerate(lines):
    print(card_number)
    print(numbers)

    print("-----\n")
    # Each card is assigned an initial value of 1
    # This means, one original card for each card.
    numbers[card_number] += 1

    winning_details, our_hand = line.split("|")
    _, winning_numbers = winning_details.split(":")
    _, winning_numbers, our_hand = list(map(lambda x: x.strip(), [_, winning_numbers, our_hand]))
    common = len(set(our_hand.split()).intersection(winning_numbers.split()))

    # new copies are generated for each existing card.
    # numbers - 'Key' : of that particular new copy card
    # numbers - 'Values' : sum of existing particular new copy card + existing card
    for copies in range(common):
        print(card_number + copies + 1)
        numbers[card_number + copies + 1] += numbers[card_number]
        print(numbers)

    if card_number == 2:
        0/0

print(sum(numbers.values()))


