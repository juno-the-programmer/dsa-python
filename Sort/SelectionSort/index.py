"""
Repeat: (unsorted list)
find the minumum value in the list
compare every num to its right
the minimum value will be most to the left
"""


def selection(nums):
    indexing_length = range(0, len(nums) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_value]:
                min_value = j

        if min_value != i:
            nums[min_value], nums[i] = nums[i], nums[min_value]

    return nums


print(selection([4, 6, 8, 3, 1, 2, 7,]))
