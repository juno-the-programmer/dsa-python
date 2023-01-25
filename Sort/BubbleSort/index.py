'''
Compare 2 value at a time
iterate until all the values sorted
'''


def bubble(nums):
    indexing_length = len(nums) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums


print(bubble([4, 6, 8, 3, 1, 2, 7,]))
