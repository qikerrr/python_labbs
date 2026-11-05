import random 
from src.lab7.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab7.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, c=100):

    for i in range(c):
        n = random.randint(0, 50)
        nums = [ random.randint(-100, 100) for i in range(n) ]
        oreo = list(nums)

        res = fn(nums)

        assert res == sorted(oreo), f"Функция {fn.__name__} неправильно или вовсе не сортирует список"

        assert oreo == nums, f"Функция {fn.__name__} изменяет исходный список, а не форматирует его копию"


def check_search(c=100):

    for i in range(c):
        n = random.randint(0, 50)
        nums = [random.randint(-100,100) for i in range(n)]

        x = random.randint(-100,100)

        try:
            result = nums.index(x)
        except ValueError:
            result = -1

        res_fn = linear_search(nums, x)
        assert res_fn == result, "Функция linear_search() неправильно нашла искомое значение"

        s_nums = sorted(nums)
        res_fn = binary_search(s_nums, x)

        if x in s_nums:
            assert res_fn != -1 and s_nums[res_fn] == x, "Функция binary_search() неправильно нашла искомое значение"

        else:
            assert res_fn == -1, "Функиция binary_search() нашла то, чего нет"

def check_two_sum(c=100):

    for i in range(c):
        n = random.randint(0, 40)
        nums = [random.randint(-50,50) for i in range(n)]

        target = random.randint(-100,100)
        x1 = two_sum_brute(nums,target)
        x2 = two_sum_fast(nums, target)

        if x1 is None:
            assert x2 is None, f'Функция two_sum_brute() вывела None, а two_sum_fast() вывела {x2}'

        else:
            assert x2 is not None, f"Функция two_sum_fast() не нашла значение"


            assert nums[x2[0]] + nums[x2[1]] == target, "Функция two_sum_fast() вернула неправильное значение"
            assert nums[x1[0]] + nums[x1[1]] == target, "Функция two_sum_brute() вернула неправильное значение"

if __name__ == "__main__":

    random.seed(67)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)

    check_search()
    check_two_sum()
    print("Все проверки были успешно пройдены!")





