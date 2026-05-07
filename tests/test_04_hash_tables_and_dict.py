import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/04-hash-tables-and-dict.py"))


def test_counter_and_defaultdict_grouping():
    c = M.aggregate_with_counter(["x", "y", "x", "x"])
    assert c["x"] == 3
    grouped = M.group_with_defaultdict([("a", 1), ("a", 2), ("b", 3)])
    assert grouped == {"a": [1, 2], "b": [3]}


def test_dict_order_preserved_and_lookup_faster():
    assert M.ordered_dict_demo() == ["first", "second", "third"]
    bench = M.dict_vs_list_lookup()
    assert bench["dict_lookup"] < bench["list_lookup"]
