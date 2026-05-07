from collections import defaultdict, deque


def edge_list_to_adj_list(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    adj: defaultdict[str, list[str]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return {k: sorted(v) for k, v in adj.items()}


def adj_list_to_matrix(nodes: list[str], adj: dict[str, list[str]]) -> list[list[int]]:
    idx = {name: i for i, name in enumerate(nodes)}
    matrix = [[0 for _ in nodes] for _ in nodes]
    for u, neighbors in adj.items():
        for v in neighbors:
            matrix[idx[u]][idx[v]] = 1
    return matrix


def bfs(adj: dict[str, list[str]], start: str) -> list[str]:
    seen = {start}
    q: deque[str] = deque([start])
    out: list[str] = []
    while q:
        cur = q.popleft()
        out.append(cur)
        for nxt in adj.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return out


def dfs(adj: dict[str, list[str]], start: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()

    def walk(node: str) -> None:
        seen.add(node)
        out.append(node)
        for nxt in adj.get(node, []):
            if nxt not in seen:
                walk(nxt)

    walk(start)
    return out


if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    adj = edge_list_to_adj_list(edges)
    print(adj)
    print(adj_list_to_matrix(["A", "B", "C", "D"], adj))
    print(bfs(adj, "A"))
    print(dfs(adj, "A"))
