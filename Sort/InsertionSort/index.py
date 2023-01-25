def insertion(nums):

    indexing_length = range(1, len(nums))

    for i in indexing_length:
        value_to_sort = nums[i]

        while nums[i-1] > value_to_sort and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i = i - 1

    return nums


print(insertion([4, 6, 8, 3, 1, 2, 7,]))
