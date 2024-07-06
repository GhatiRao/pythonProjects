
a = ['a', 'b', 'c', 'd']
v = [1, 2, 3, 4]
dictionary = {}
for i in range(len(v)):
    dictionary[a[i]] = v[i]

print(dictionary)

dictionary2 = { a[i]: v[i] for i in range(len(v)) }
dictionary3 = dict(zip(a,v))
dictionary4 = {}
for i, j in zip(a,v):
    dictionary4[i] = j

dictionary5 = { i:j for i, j in zip(a,v)}

print(dictionary2)
print(dictionary3)
print(dictionary4)
print(dictionary5)


# convert a string into decimals

string = "123345457"

import decimal
print(decimal.Decimal(string))

# count vowels in string
from itertools import count
from collections import Counter
vowels = ['a', 'e', 'i', 'o', 'u']

print(Counter(vowels))

import collections

help(collections)

