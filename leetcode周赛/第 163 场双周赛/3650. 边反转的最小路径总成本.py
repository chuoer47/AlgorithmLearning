from collections import defaultdict
from typing import List
from heapq import *


def Dij(weight, source, n):
    visited = [0] * (n + 10)  # 这里稍微注意一下
    dis = [float('inf')] * (n + 10)
    dis[source] = 0
    stack = [(0, source)]
    heapify(stack)
    while stack:
        price, node = heappop(stack)
        if visited[node]:
            continue
        else:
            visited[node] = 1
        # 链表存储把这里逻辑改一下就好了
        for p, w in weight[node]:
            if dis[node] + w < dis[p]:
                dis[p] = dis[node] + w
                heappush(stack, (dis[node] + w, p))
    return dis


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # 状态就是(node,used)的最小值,跑最短路就好了。
        # 建立图和反图，用最小堆跑即可
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))
        dis = Dij(g, 0, n)
        ans = dis[n - 1]
        return ans if ans < inf else -1