import importlib.util
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/01-what-are-data-structures.py"))


def test_counting_methods_match():
    words = M.words_from_text("a b a c b a")
    assert M.count_with_list(words) == {"a": 3, "b": 2, "c": 1}
    assert M.count_with_dict(words) == {"a": 3, "b": 2, "c": 1}
    assert M.count_with_counter(words) == {"a": 3, "b": 2, "c": 1}
