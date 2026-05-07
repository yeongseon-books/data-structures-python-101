from collections import deque


def is_balanced_parentheses(text: str) -> bool:
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    visited = {start}
    q: deque[str] = deque([start])
    out: list[str] = []
    while q:
        cur = q.popleft()
        out.append(cur)
        for nxt in graph.get(cur, []):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return out


if __name__ == "__main__":
    demo = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print(is_balanced_parentheses("([]){}"))
    print(bfs_order(demo, "A"))
