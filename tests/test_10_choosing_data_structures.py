import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/10-choosing-data-structures.py"))


def test_recommendation_table():
    assert M.recommend_structure("frequent prepend") == "collections.deque"
    assert M.recommend_structure("priority retrieval") == "heapq"
    assert M.recommend_structure("unknown") == "list"


def test_workload_benchmarks_contains_expected_keys():
    bench = M.run_workload_benchmarks(3000)
    assert set(bench) == {"list_prepend", "deque_prepend", "heap_priority"}
    assert bench["deque_prepend"] < bench["list_prepend"]
