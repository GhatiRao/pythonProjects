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
        return answer
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

# ans = Solution()
# ans.intersect([1,2,3, 34, 23,23, 23], [1, 23, 34, 23,4, 234])

def pass_the_pillow(n: int, time: int) -> int:
    # n - no of people
    # n = 5, dividing into chunks ..
    # 1 2 3 4 | 5 4 3 2 | 1 2 3 4 | 5 4 3 2 | 1 2 3 4

    chunks = time // (n-1)
    return (time % (n-1) + 1) if chunks % 2 == 0 else (n - time % (n-1))


print(pass_the_pillow(5, 10))
