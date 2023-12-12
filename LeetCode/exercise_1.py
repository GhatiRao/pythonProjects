
"""
Itertools combinations (iterable, count)
"""

"""
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format
A single line containing the string  and integer value  separated by a space.
Constraints

HACK 2
A
C
H
K
AC
AH
AK
CH
CK
HK
"""


from itertools import combinations


def iteration(string: str, count: int):
    """
    :param string: string
    :param count: int
    :return: list[int]
    """
    # option 1 : using while loop and moving backwards
    # string = sorted(string)
    # answer = [word for word in string]
    # init = 2
    # while init <= count:
    #     for word in combinations(string, init):
    #         answer.append("".join(word))
    #     init += 1
    # print(answer)

    # option 2 : using the increment in count values
    string = sorted(string)
    for num in range(1, count+1):
        for word in combinations(string, num):
            print("".join(word))

input_ = input()
input_string, count = input_.split(" ")[0], int(input_.split(" ")[1])

iteration(input_string, count)


