import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/08-graph-representations.py"))


def test_conversions_and_traversals():
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    adj = M.edge_list_to_adj_list(edges)
    assert adj["A"] == ["B", "C"]
    matrix = M.adj_list_to_matrix(["A", "B", "C", "D"], adj)
    assert matrix[0][1] == 1 and matrix[0][2] == 1
    assert M.bfs(adj, "A") == ["A", "B", "C", "D"]
    assert M.dfs(adj, "A")[0] == "A"
