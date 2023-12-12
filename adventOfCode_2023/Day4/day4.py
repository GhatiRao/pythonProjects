from pprint import pprint
# lines = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#          "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#          "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#          "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#          "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#          "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

with open("input.txt", "r") as file:
    input_text = file.read()
lines = input_text.splitlines() # -> ["Card 1: ...", "Card 2:...", ..]

# pprint(lines)
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
