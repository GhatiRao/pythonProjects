from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):

        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        answer = []
        for x in nums2:
            if cnt[x] > 0:
                answer.append(x)
                cnt[x] -= 1
        return ans

        #
        #
        # # store the smallest list in this var
        # small = [nums2, len(nums2)] if len(nums2) < len(nums1) else [nums1, len(nums1)]
        # print(small)
        # print(Counter(small[0]))
        # cnt = Counter(nums1)
        # ans = []
        # for x in nums2:
        #     if cnt[x] > 0:
        #         ans.append(x)
        #         cnt[x] -= 1
        # return ans



        # if small[1] == 0:
        #     return [0]
        # return small


ans = Solution()
ans.intersect([1,2,3, 34, 23,23, 23], [1, 23, 34, 23,4, 234])


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

