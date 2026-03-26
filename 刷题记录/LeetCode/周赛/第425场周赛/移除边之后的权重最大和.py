class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def dfs(x, fa):
            not_choose = 0
            inc = []
            for y, w in g[x]:
                if y == fa:
                    continue
                nc, c = dfs(y, x)
                not_choose += nc
                if (d := c + w - nc) > 0:
                    inc.append(d)
            inc.sort(reverse=True)
            return not_choose + sum(inc[:k]), not_choose + sum(inc[:k - 1])

        return dfs(0, -1)[0]
