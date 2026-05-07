from collections import deque
import heapq
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


def recommend_structure(pattern: str) -> str:
    table = {
        "frequent prepend": "collections.deque",
        "ordered unique": "dict.fromkeys + list",
        "priority retrieval": "heapq",
        "fast membership": "set",
        "key value lookup": "dict",
    }
    return table.get(pattern, "list")


def workload_list_prepend(n: int) -> int:
    data: list[int] = []
    for i in range(n):
        data.insert(0, i)
    return len(data)


def workload_deque_prepend(n: int) -> int:
    dq: deque[int] = deque()
    for i in range(n):
        dq.appendleft(i)
    return len(dq)


def workload_heap_priority(n: int) -> int:
    heap: list[int] = []
    for i in range(n):
        heapq.heappush(heap, n - i)
    acc = 0
    while heap:
        acc += heapq.heappop(heap)
    return acc


def run_workload_benchmarks(n: int = 10_000) -> dict[str, float]:
    return {
        "list_prepend": time_op(workload_list_prepend, n, repeat=3),
        "deque_prepend": time_op(workload_deque_prepend, n, repeat=3),
        "heap_priority": time_op(workload_heap_priority, n, repeat=3),
    }


if __name__ == "__main__":
    print(recommend_structure("frequent prepend"))
    print(run_workload_benchmarks())
