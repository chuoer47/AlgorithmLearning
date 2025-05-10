from typing import List


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        if k == 0:
            return 0

        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append([v, w])

        # 消去t的依赖是否可行，使用哈希完成 dp[i][j] = set() list中的值表示可以到达的权值
        dp = [[set() for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0].add(0)

        # 转移：dp[i][j][s] -> dp[i][j+1][s+w]
        for i in range(k):
            for u in range(n):
                for s in dp[u][i]:
                    for v, w in graph[u]:
                        new_s = s + w
                        if new_s < t and i + 1 <= k:
                            dp[v][i + 1].add(new_s)

        for s in range(t - 1, -1, -1):
            for i in range(n):
                if s in dp[i][k]:
                    return s

        return -1
