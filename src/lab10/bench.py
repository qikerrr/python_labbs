import timeit
from collections import deque

import csv
from pathlib import Path

from src.lab10.linked_list import ll_prepend



def bench_queue(n):
    l = list(range(n))
    dq = deque(range(n))
    t_list = timeit.timeit(lambda: l.pop(0), number=n)
    t_deque = timeit.timeit(lambda: dq.popleft(), number=n)
    return t_list, t_deque


def bench_prepend(n):
    l = []
    t_list = timeit.timeit(lambda: l.insert(0, 0), number=n)

    head = None

    def prepend_n():
        nonlocal head
        for i in range(n):
            head = ll_prepend(head, i)

    t_ll = timeit.timeit(prepend_n, number=1)
    return t_list, t_ll

def write_csv(path, headers, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def main():

    ns = [10_000, 100_000]
    rows = []
    headers = ['Операция', 'n', 'list', 'deque/ll', 'Во сколько раз']

    for n in ns:
        t_list_q, t_deque_q = bench_queue(n)
        ratio_q = t_list_q / t_deque_q if t_deque_q else float('inf')
        rows.append(('queue pop', n, t_list_q, t_deque_q, ratio_q))

        t_list_p, t_ll_p = bench_prepend(n)
        ratio_p = t_list_p / t_ll_p if t_ll_p else float('inf')
        rows.append(('prepend', n, t_list_p, t_ll_p, ratio_p))

    print(f"{'Операция':<15} {'n':>8} {'list':>12} {'deque/ll':>12} {'Во сколько раз':>16}")
    for op, n, t_list, t_other, ratio in rows:
        print(f"{op:<15} {n:>8} {t_list:>12.6f} {t_other:>12.6f} {ratio:>16.2f}")

    write_csv('data/lab10/bench.csv', headers, rows)


if __name__ == '__main__':
    main()