#
# a = ['a', 'b', 'c', 'd']
# v = [1, 2, 3, 4]
# dictionary = {}
# for i in range(len(v)):
#     dictionary[a[i]] = v[i]
#
# print(dictionary)
#
# dictionary2 = { a[i]: v[i] for i in range(len(v)) }
# dictionary3 = dict(zip(a,v))
# dictionary4 = {}
# for i, j in zip(a,v):
#     dictionary4[i] = j
#
# dictionary5 = { i:j for i, j in zip(a,v)}
#
# print(dictionary2)
# print(dictionary3)
# print(dictionary4)
# print(dictionary5)
#
#
# # convert a string into decimals
#
# string = "123345457"
#
# import decimal
# print(decimal.Decimal(string))
#
# # count vowels in string
# from itertools import count
# from collections import Counter
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# print(Counter(vowels))
#
# import collections
#
# help(collections)
#


import math


def get_minimum_slots(large_slots, small_slots, buses, cars):
    # for the bus, only large_slots can be assigned..
    # LS = 1B | 3C
    # SS = 0B | 1C
    # 2 LS - 12 SS
    # -- 1B, -- 3C

    # handle the excess case

    if buses > large_slots:
        return -1
    if cars > 3 * large_slots or cars > small_slots:
        return -1

    if large_slots + small_slots < buses + 3 * cars:
        return -1

    slotCounter = 0

    # Check if the buses is less than large slots
    if buses:
        if buses <= large_slots:
            slotCounter += buses
            large_slots -= slotCounter
        else:
            return -1
    if cars:
        if (large_slots*3)<cars:
            CarSlots, remainder = int(cars//(large_slots * 3)), int((large_slots * 3) % cars)
            slotCounter += CarSlots
            remainingCars = cars-(large_slots*3)
            # adjusting the excess with small slots, aka, remainder
            # slotCounter += remainder
            return slotCounter + remainingCars
        elif (large_slots*3)>cars:
            CarSlots, remainder = int((large_slots * 3)/cars), int((large_slots * 3) % cars)
            slotCounter += CarSlots

            # adjusting the excess with small slots, aka, remainder
            # slotCounter += remainder
            return slotCounter

        if cars > CarSlots:
            return -1

        return slotCounter + cars


print(get_minimum_slots(2, 12, 1, 4))

from json import dumps

def sort_by_marks_descending(json_string):
    actualString = eval(json_string)
    actualString = sorted(actualString, key=lambda x: x["mark"], reverse=True)
    actualString = dumps(actualString)

    print(type(str(actualString)))

    return actualString


print(sort_by_marks_descending(
    '[{"name": "John", "mark": 85}, {"name": "Alice", "mark": 90}, {"name": "Bob", "mark": 88}]'))











