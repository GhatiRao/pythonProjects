"""
1. Two Sum - https://leetcode.com/problems/two-sum/

ALGO
- HASHMAP / DICTIONARY
- Iterate Left to Right
- Iterate one element at a time
- Store/compare the element in hashmap based on logic of question
"""

"""
2. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

ALGO
- Left Pointer, Right Pointer
- Start with Left Pointer : 
    if Right Pointer < Left Pointer
        Left Pointer = Right Pointer
        Right Pointer Increment
    
"""

"""
3. Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

ALGO
- Segment Forward Pass & Backward Pass
- Iterate Forward Pass
    store nums[i] to the left pointer  
"""


# TREE

"""
1. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/

root = [1, 2, 3, Null, Null, 4, 5]

1 -> 2, 3
2 -> Null, Null
3 -> 4, 5

- Binary Node Class contains parameters: Value, Left, Right

ALGO
DFS
- Recursive Function of : Max(function(root.left), function(root.right)) + 1
    Condition :
    if root : above
    else: 0
    

"""

"""
2. Same Tree - https://leetcode.com/problems/same-tree/

ALGO
- if p is not none and q is not none:
    if p.val == q.val
    return function(p.left, q.left) and function(p.right, q.right)
"""


"""
3. Invert/Flip Binary Tree - https://leetcode.com/problems/invert-binary-tree/

ALGO
- if not root: return root
"""