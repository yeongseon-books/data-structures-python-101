import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/02-arrays-and-lists.py"))


def test_array_sum_and_idioms():
    assert M.typed_array_sum([1, 2, 3]) == 6
    out = M.list_idioms([1, 2, 3, 4, 5, 6])
    assert out["slice"] == [2, 3, 4]


def test_deque_appendleft_faster_than_list_insert0():
    bench = M.prepend_benchmark(10_000)
    assert bench["deque_appendleft"] / bench["list_insert0"] < 0.5
