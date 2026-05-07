import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/09-sets-and-set-operations.py"))


def test_set_ops_and_ordered_unique():
    ops = M.set_operations({1, 2, 3, 4}, {3, 4, 5})
    assert ops["union"] == {1, 2, 3, 4, 5}
    assert ops["intersection"] == {3, 4}
    assert ops["difference"] == {1, 2}
    assert ops["symmetric_difference"] == {1, 2, 5}
    assert M.ordered_unique(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_set_membership_faster_than_list():
    bench = M.membership_benchmark()
    assert bench["set_in"] < bench["list_in"]
