from typing import List


class Solution:
    def maxSubgraphScore(
            self, n: int, edges: List[List[int]], good: List[int]
    ) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        mx = [0] * n
        good = [1 if x else -1 for x in good]

        def dfs(node, fa):
            nonlocal mx
            ans = good[node]
            for nxt in g[node]:
                if nxt == fa:
                    continue
                s = dfs(nxt, node)
                if s > 0:
                    ans += s
            mx[node] = ans
            return ans

        def reroot(node, fa):
            nonlocal mx
            for nxt in g[node]:
                if nxt == fa:
                    continue
                fa_mx = mx[node] - (mx[nxt] if mx[nxt] > 0 else 0)
                mx[nxt] = mx[nxt] + (fa_mx if fa_mx > 0 else 0)
                reroot(nxt, node)

        dfs(0, -1)
        reroot(0, -1)
        return mx
