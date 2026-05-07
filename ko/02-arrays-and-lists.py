from array import array
from collections import deque
from time import perf_counter
from typing import Any, Callable


def time_op(
    fn: Callable[..., Any], *args: Any, repeat: int = 5, loops: int = 1, **kwargs: Any
) -> float:
    best = float("inf")
    for _ in range(repeat):
        start = perf_counter()
        for _ in range(loops):
            fn(*args, **kwargs)
        best = min(best, perf_counter() - start)
    return best


def list_idioms(values: list[int]) -> dict[str, list[int] | int]:
    copied = values[:]
    comp = [x * 2 for x in values if x % 2 == 0]
    return {"slice": values[1:4], "copy_first": copied[0], "comp": comp}


def typed_array_sum(values: list[int]) -> int:
    arr = array("i", values)
    return sum(arr)


def prepend_list(n: int) -> int:
    data: list[int] = []
    for i in range(n):
        data.insert(0, i)
    return len(data)


def prepend_deque(n: int) -> int:
    data: deque[int] = deque()
    for i in range(n):
        data.appendleft(i)
    return len(data)


def prepend_benchmark(n: int = 10_000) -> dict[str, float]:
    return {
        "list_insert0": time_op(prepend_list, n, repeat=3),
        "deque_appendleft": time_op(prepend_deque, n, repeat=3),
    }


if __name__ == "__main__":
    print(list_idioms([1, 2, 3, 4, 5, 6]))
    print(typed_array_sum([1, 2, 3, 4]))
    print(prepend_benchmark())
