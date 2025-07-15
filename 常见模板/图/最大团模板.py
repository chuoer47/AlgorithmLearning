def edges_to_adjacency(edges):
    n = len(edges)
    adj = {i: set() for i in range(n)}
    for u in range(n):
        for v in edges[u]:
            if v < n:  # 确保顶点索引有效
                adj[u].add(v)
                adj[v].add(u)  # 无向图需双向添加
    return adj


def bron_kerbosch(R, P, X, adj, cliques):
    if not P and not X:
        cliques.append(R.copy())
        return
    pivot = next(iter(P | X)) if P | X else None
    for v in P - adj.get(pivot, set()):
        new_R = R | {v}
        new_P = P & adj[v]
        new_X = X & adj[v]
        bron_kerbosch(new_R, new_P, new_X, adj, cliques)
        P.remove(v)
        X.add(v)


def find_max_cliques(edges):
    adj = edges_to_adjacency(edges)
    n = len(adj)
    cliques = []
    bron_kerbosch(set(), set(range(n)), set(), adj, cliques)
    if not cliques:
        return []
    max_size = max(len(c) for c in cliques)
    return [c for c in cliques if len(c) == max_size]


# 示例用法
edges = [[1, 2], [0, 2], [0, 1]]
print(find_max_cliques(edges))