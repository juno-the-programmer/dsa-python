'''
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n ?

Write a function gridTraveler(m, n) that calculates this.
'''


def gridTraveler(m, n):
    table = [[0 for x in range(n+1)] for y in range(m+1)]
    table[1][1] = 1

    for i in range(0, m+1):
        for j in range(0, n+1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j+1] += current
            if i + 1 <= m:
                table[i+1][j] += current
    return table[m][n]


print(gridTraveler(1, 1))  # 1
# print(gridTraveler(2, 3))  # 3
# print(gridTraveler(3, 2))  # 3
# print(gridTraveler(3, 3))  # 6
# print(gridTraveler(18, 18))  # 2333606220
