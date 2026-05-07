import importlib.util
from pathlib import Path
import sys


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/06-trees-and-binary-trees.py"))


def test_bfs_and_dfs_names():
    root = M.TreeNode("root", [M.TreeNode("a"), M.TreeNode("b", [M.TreeNode("c")])])
    assert M.bfs_names(root) == ["root", "a", "b", "c"]
    assert M.dfs_names(root) == ["root", "a", "b", "c"]


def test_xml_tags():
    tags = M.xml_tags("<root><item/><item><name/></item></root>")
    assert tags == ["root", "item", "item", "name"]
