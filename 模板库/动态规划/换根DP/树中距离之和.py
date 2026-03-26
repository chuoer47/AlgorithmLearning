# https://leetcode.cn/problems/sum-of-distances-in-tree/description/
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 第一次系统学换根DP，看着题解敲出来的
        # 核心就是在dfs的时候去找【相邻节点的变化量】

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [0] * n
        size = [1] * n

        def dfs(node: int, fa: int, depth: int) -> None:
            ans[0] += depth
            for nxt in g[node]:
                if nxt == fa:
                    continue
                dfs(nxt, node, depth + 1)
                size[node] += size[nxt]

        def reroot(node: int, fa: int):
            for nxt in g[node]:
                if nxt == fa:
                    continue
                ans[nxt] = ans[node] + n - 2 * size[nxt]
                reroot(nxt, node)

        dfs(0, -1, 0)
        reroot(0, -1)
        return ans
