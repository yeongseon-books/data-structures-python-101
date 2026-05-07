import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(
    str(Path(__file__).resolve().parents[1] / "ko/07-heaps-and-priority-queues.py")
)


def test_heap_pop_and_nlargest():
    assert M.min_heap_pop_order([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert M.top_n_largest([5, 1, 9, 3, 7], 3) == [9, 7, 5]


def test_merge_sorted_lists():
    merged = M.merge_sorted_lists([[1, 4], [2, 3], [0, 5]])
    assert merged == [0, 1, 2, 3, 4, 5]
