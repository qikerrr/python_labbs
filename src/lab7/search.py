def linear_search(nums, x):

    for i, n in enumerate(nums):
        if n == x:
            return i

    return -1

def binary_search(sorted_nums, x):

    x1 = 0
    x2 = len(sorted_nums) - 1

    while x1 <= x2:
        mid = (x1+x2)//2

        if sorted_nums[mid] ==x:
            return mid

        elif sorted_nums[mid] < x:
            x1 = mid + 1
        else:
            x2 = mid - 1

    return -1

def two_sum_brute(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None

def two_sum_fast(nums, target):
    d = {}

    for i, x in enumerate(nums):
        pair = target - x

        if pair in d:
            return (d[pair], i)

        d[x] = i

    return None
        