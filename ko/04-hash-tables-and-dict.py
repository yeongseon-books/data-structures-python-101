from collections import Counter, defaultdict
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


def aggregate_with_counter(items: list[str]) -> Counter[str]:
    return Counter(items)


def group_with_defaultdict(pairs: list[tuple[str, int]]) -> dict[str, list[int]]:
    grouped: defaultdict[str, list[int]] = defaultdict(list)
    for k, v in pairs:
        grouped[k].append(v)
    return dict(grouped)


def ordered_dict_demo() -> list[str]:
    d = {"first": 1, "second": 2, "third": 3}
    return list(d.keys())


def dict_vs_list_lookup(size: int = 30_000, target: int = 29_999) -> dict[str, float]:
    values = list(range(size))
    mapping = {x: x for x in values}
    return {
        "list_lookup": time_op(lambda: target in values, loops=200),
        "dict_lookup": time_op(lambda: target in mapping, loops=200),
    }


if __name__ == "__main__":
    print(aggregate_with_counter(["a", "b", "a", "c", "a"]))
    print(group_with_defaultdict([("a", 1), ("a", 2), ("b", 3)]))
    print(ordered_dict_demo())
    print(dict_vs_list_lookup())
