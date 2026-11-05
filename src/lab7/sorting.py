def bubble_sort(nums):

    nums = list(nums)
    n = len(nums)

    for i in range(n):
        fl = 0

        for j in range(n - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

                fl = 1

        if not fl:
            break

    return nums

def insertion_sort(nums):

    nums = list(nums)

    for i in range(1, len(nums)):

        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums

def selection_sort(nums):

    nums = list(nums)
    n  = len(nums)

    for i in range(n):
        min_idx = i 

        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums