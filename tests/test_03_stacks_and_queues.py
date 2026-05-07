import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/03-stacks-and-queues.py"))


def test_balanced_parentheses_cases():
    assert M.is_balanced_parentheses("([]){}") is True
    assert M.is_balanced_parentheses("([)]") is False
    assert M.is_balanced_parentheses("(((())))") is True


def test_bfs_order():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert M.bfs_order(graph, "A") == ["A", "B", "C", "D"]
