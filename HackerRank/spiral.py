"""
Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

"""

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

r = 4
c = 4
answer = []
top = 0
bottom = r
right = c
left = 0

while top <= bottom and left <= right:
    for row in range(left, right):
        print(row)
        answer.append(matrix[top][row])
    top += 1
    print("---")
    for col in range(top, bottom+1):
        print(col)
        answer.append(matrix[col][right])
    right -= right

    print(answer)







spirallyTraverse(matrix, 4, 4)