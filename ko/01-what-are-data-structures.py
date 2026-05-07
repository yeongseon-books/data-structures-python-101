# pyright: reportMissingParameterType=false, reportUnknownParameterType=false, reportExplicitAny=false, reportAny=false

from collections import Counter
from time import perf_counter


def time_op(fn, *args, repeat: int = 5, loops: int = 1, **kwargs) -> float:
    best = float("inf")
    for _ in range(repeat):
        start = perf_counter()
        for _ in range(loops):
            fn(*args, **kwargs)
        best = min(best, perf_counter() - start)
    return best


TEXT = "python data structures with python data"


def words_from_text(text: str) -> list[str]:
    return text.split()


def count_with_list(words: list[str]) -> dict[str, int]:
    uniq = sorted(set(words))
    return {w: words.count(w) for w in uniq}


def count_with_dict(words: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for w in words:
        out[w] = out.get(w, 0) + 1
    return out


def count_with_counter(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


def benchmark_counts(words: list[str]) -> dict[str, float]:
    return {
        "list+count": time_op(count_with_list, words, loops=200),
        "dict": time_op(count_with_dict, words, loops=200),
        "Counter": time_op(count_with_counter, words, loops=200),
    }


if __name__ == "__main__":
    words = words_from_text(TEXT)
    print(count_with_counter(words))
    print(benchmark_counts(words))
