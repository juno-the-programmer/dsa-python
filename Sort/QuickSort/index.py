def quick(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    items_greater = []
    items_lower = []

    for item in nums:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick(items_lower) + [pivot] + quick(items_greater)


print(quick([4, 6, 8, 3, 1, 2, 7,]))
