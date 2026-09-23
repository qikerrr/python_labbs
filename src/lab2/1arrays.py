def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    max1 = nums[0]
    min1 = nums[0]

    for s in nums:
        if s > max1:
            max1 = s
        if s < min1:
            min1 = s

    return(min1, max1) 

##print(min_max([3, -1, 5, 5, 0]))
##print(min_max([42]))
##print(min_max([-5, -2, -9]))
##print(min_max([]))
##print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums):
    res = []
    for s in nums:
        if s not in res: #формируем список по уникальности
            res.append(s)

    for j in range(len(res)):
        for i in range(len(res)-1 - j):#перебираем по всему списку каждый раз исключая последний уже осортированный элемент
            if res[i] > res[i+1]:
                res[i], res[i+1] = res[i+1], res[i]

    return res

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

