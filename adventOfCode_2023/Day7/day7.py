from collections import Counter, OrderedDict
import re
from pprint import pprint
with open("input.txt", "r") as file:
    input_text = file.read().splitlines()
print(input_text)


def type_hand(string: str):

    string = string.replace('T', chr(58))
    string = string.replace('J', chr(59))
    string = string.replace('Q', chr(60))
    string = string.replace('K', chr(61))
    string = string.replace('A', chr(62))

    # string = string.replace('T', chr(ord('9') + 1))
    # string = string.replace('J', chr(ord('2') - 1))
    # string = string.replace('Q', chr(ord('9') + 3))
    # string = string.replace('K', chr(ord('9') + 4))
    # string = string.replace('A', chr(ord('9') + 5))

    C = Counter(string)
    if sorted(C.values()) == [5]:
        return (10, string)
    elif sorted(C.values()) == [1, 4]:
        return (9, string)
    elif sorted(C.values()) == [2, 3]:
        return (8, string)
    elif sorted(C.values()) == [1, 1, 3]:
        return (7, string)
    elif sorted(C.values()) == [1, 2, 2]:
        return (6, string)
    elif sorted(C.values()) == [1, 1, 1, 2]:
        return (5, string)
    elif sorted(C.values()) == [1, 1, 1, 1, 1]:
        return (4, string)


sorted_store = []
print(input_text)
answer = sorted(input_text, key=lambda x: type_hand(x.split()[0]))
print(answer)

total = 0
for index, entry in enumerate(answer):
    total += (index)*int(entry.split()[1])

print(total)










#
#
#
#
# hands, values = [[i.split(" ")[0] for i in input_text], [int(i.split(" ")[1]) for i in input_text]]
# mapped_values = {i: j for i, j in zip(hands, values)}
# pprint(mapped_values)
#
#
# def type_hand(string: str):
#     a = Counter(string)
#     if len(a) == 1:  # Five of a kind
#         return 7
#     if len(a) == 2 and max(a.values()) == 4:  # 'AAAA3' # Four of a kind
#         return 6
#     if len(a) == 2 and max(a.values()) == 3 and min(a.values()) == 2:  # 'AAA33' # Full house
#         return 5
#     if len(a) == 3 and max(a.values()) == 3:  # 'AAA32' # Three of a kind
#         return 4
#     if max(a.values()) == 2 and len(a) == 3:  # 'AAK33' # Two pair
#         return 3
#     if max(a.values()) == 2 and len(a) == 4:  # 'AA123' # One pair
#         return 2
#     return 1  # "23456" # High card
#
#
# a = OrderedDict()
# for string in hands:
#     string = string.replace('T', chr(58))
#     string = string.replace('J', chr(59))
#     string = string.replace('Q', chr(60))
#     string = string.replace('K', chr(61))
#     string = string.replace('A', chr(62))
#     a.setdefault(type_hand(string), []).append(string)
# #
# # pprint(a)
# # a[0] = sorted(a[0])
# # a[1] = sorted(a[1])
# # a[2] = sorted(a[2])
# # a[3] = sorted(a[3])
# # a[4] = sorted(a[4])
# # a[5] = sorted(a[5])
# # a[6] = sorted(a[6])
# print(a)
#
# # recombining
# summation = 0
# multiplier = 0
# pprint(a)
# for rude_dict in [1, 2, 3, 4, 5, 6]:
#     a[rude_dict] = sorted(a[rude_dict])
#     for string in a[rude_dict]:
#         multiplier += 1
#         string = string.replace(chr(58), 'T')
#         string = string.replace(chr(59), 'J')
#         string = string.replace(chr(60), 'Q')
#         string = string.replace(chr(61), 'K')
#         string = string.replace(chr(62), 'A')
#         print(string)
#         print(f"{multiplier}*{mapped_values[string]}")
#         summation += multiplier*mapped_values[string]
#
# print(summation)







0/0

def strength(string: str):
    print(string)
    print(chr(58))
    print(chr(59))
    print(chr(60))
    print(chr(61))
    print(chr(62))
    string = string.replace('T', chr(58))
    string = string.replace('J', chr(59))
    string = string.replace('Q', chr(60))
    string = string.replace('K', chr(61))
    string = string.replace('A', chr(62))
    print(string)


def weighted_strengths(string):
    print(string)
    string = string.replace('T', chr(58))
    string = string.replace('J', chr(59))
    string = string.replace('Q', chr(60))
    string = string.replace('K', chr(61))
    string = string.replace('A', chr(62))
    print(string)
    weighted_calc = []
    for index, character in enumerate(string, start = 0):
        print(f"{character} : {ord(character)}")
        weighted_calc.append((5-index)*ord(character))

    print(weighted_calc)
    print(sum(weighted_calc))


for hand in hands:
    print("------\n")
    weighted_strengths(hand)

#
# a = [ '234', 'K545']
# a.sort(key = lambda x: ord(f'{x}'))
# print(a)