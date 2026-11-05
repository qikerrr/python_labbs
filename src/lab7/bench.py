import csv
import random
import signal
import timeit

from src.lab7.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab7.search import linear_search, binary_search, two_sum_brute, two_sum_fast

from src.lab4.io_txt_csv import write_csv

class _timeout(Exception):
    pass

def problem(s, i):
    raise _timeout()

def time_once(fn, timeout=None):

    if timeout is None or not hasattr(signal, "SIGALRM"):
        return timeit.timeit(fn, number=1)

    old = signal.signal(signal.SIGALRM, problem)
    signal.alarm(timeout)

    try:
        return timeit.timeit(fn, number=1)
    except _timeout:
        return None
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)

def bench_sorts():
    rows = []
    sorts = [("sorted",     sorted),
        ("bubble",     bubble_sort),
        ("insertion",  insertion_sort),
        ("selection",  selection_sort)]

    for n in (1_000, 10_000, 100_000):
        data = random.sample(range(0, 1_000_000), n)
        for name, fn in sorts:
            if n >= 100_000 and name in ("bubble", "insertion", "selection"):
                rows.append({"task": "sort", "n": n, "impl": name, "seconds": ">60"})
                continue

            t = time_once(lambda: fn(data), timeout=60)
            seconds = ">60" if t is None else round(t,6)

            rows.append({"task": "sort", "n": n, "impl": name, "seconds": seconds})
    return rows

def bench_search():
    rows = []
    data = random.sample(range(0, 1_000_000), 100_000)
    s = [random.choice(data) for i in range(10_000)]

    t = time_once(lambda: [linear_search(data, i) for i in s])
    rows.append({"task": "search", "n": 100_000, "impl": "linear", "seconds": round(t, 6)})

    t_sort = time_once(lambda: sorted(data))
    rows.append({"task": "search", "n": 100_000, "impl": "sort_for_binary", "seconds": round(t_sort, 6)})

    s_data = sorted(data)
    t = time_once(lambda: [binary_search(s_data, i) for i in s])
    rows.append({"task": "search", "n": 100_000, "impl": "binary_after_sort", "seconds": round(t, 6)})
    
    return rows

def bench_two_sum():
    rows = []
    for n in (1_000, 10_000):
        data = random.sample(range(0, 1_000_000), n)
        target = data[-1] + data[-2]

        t = time_once(lambda: two_sum_brute(data,target))
        rows.append({"task": "two_sum", "n": n, "impl": "brute", "seconds": round(t, 6)})

        t = time_once(lambda: two_sum_fast(data,target))
        rows.append({"task": "two_sum", "n": n, "impl": "fast", "seconds": round(t, 6)})
    
    return rows


def print_table(rows):

    print(f"{'task':<10}{'n':>8}  {'impl':<20}{'seconds':>12}")
    print("-" * len(f"{'task':<10}{'n':>8}  {'impl':<20}{'seconds':>12}"))

    for i in rows:
        print(f"{i['task']:<10}{i['n']:>8}  {i['impl']:<20}{str(i['seconds']):>12}")

if __name__ == "__main__":

    random.seed(67)
    res = []
    res += bench_search()
    res += bench_sorts()
    res += bench_two_sum()

    print_table(res)

    rows_for_csv = [(r["task"], r["n"], r["impl"], r["seconds"]) for r in res]

    write_csv(rows_for_csv, "data/out/bench.csv", ("task", "n", "impl", "seconds"))
    print("CSV сохранён в data/out/bench.csv")








