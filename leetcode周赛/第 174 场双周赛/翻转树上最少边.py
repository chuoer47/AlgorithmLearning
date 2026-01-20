class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        if sum(int(x != y) for x, y in zip(start, target)) % 2 == 1:
            # 无解
            return [-1]
        vis = [0] * n
        g = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append((i, v))
            g[v].append((i, u))

        def dfs(node, fa) -> List:
            cnt = int(start[node] != target[node])
            for idx, child in g[node]:
                if child == fa:
                    continue
                if dfs(child, node):
                    cnt ^= 1
                    vis[idx] += 1
            return cnt == 1

        dfs(0, -1)
        return [i for i, v in enumerate(vis) if v == 1]
