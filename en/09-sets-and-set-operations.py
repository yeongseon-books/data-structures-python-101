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


def set_operations(a: set[int], b: set[int]) -> dict[str, set[int]]:
    return {
        "union": a | b,
        "intersection": a & b,
        "difference": a - b,
        "symmetric_difference": a ^ b,
    }


def ordered_unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def membership_benchmark(size: int = 50_000, target: int = 49_999) -> dict[str, float]:
    values = list(range(size))
    values_set = set(values)
    return {
        "list_in": time_op(lambda: target in values, loops=300),
        "set_in": time_op(lambda: target in values_set, loops=300),
    }


if __name__ == "__main__":
    print(set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))
    print(ordered_unique(["a", "b", "a", "c", "b"]))
    print(membership_benchmark())
