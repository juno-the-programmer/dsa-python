'''
Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetSum
using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.
'''


def canSum(targetSum, numbers):
    table = [False] * (targetSum + 1)
    table[0] = True

    for i in range(0, targetSum + 1):
        if table[i] is not False:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True

    return table[targetSum]


print(canSum(7, [2, 3]))  # true
print(canSum(7, [5, 3, 4, 7]))  # true
print(canSum(7, [2, 4]))  # false
print(canSum(8, [2, 3, 5]))  # true
print(canSum(300, [7, 14]))  # false
