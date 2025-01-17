from typing import Iterable

def find(k: int, m: int, iterable: Iterable[int]) -> int:
    lst = list(iterable)
    n = len(lst)
    if n < k:
        return -1
    for i in range(n - k + 1):
        total_sum = sum(lst[i:i+k])
        if total_sum == m:
            return i
    return -1