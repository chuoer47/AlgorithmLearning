from collections import deque
from typing import List


def topsort(graph, deg):
    # 给图 & 入度 完成topsort
    ans = set()
    q = deque(i for i, v in enumerate(deg) if v == 1)
    while q:
        now = q.popleft()
        ans.add(now)
        for nxt in graph[now]:
            if nxt in ans:
                continue
            deg[nxt] -= 1
            if deg[nxt] == 1:
                q.append(nxt)
    return ans


# bfs找路径
def bfs(start, n, graph):
    dis = [-1] * n
    step = 0
    q = deque([start])
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            if dis[now] != -1:
                continue
            dis[now] = step
            for nxt in graph[now]:
                if dis[nxt] == -1:
                    q.append(nxt)
        step += 1
    return dis


class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        n = len(edges)
        startA -= 1
        startB -= 1

        # 建立图
        graph = [[] for i in range(n)]
        deg = [0] * n
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # topsort 找 circle
        not_circle = topsort(graph, deg)
        circle = set(range(n)) - not_circle
        # 特判相邻情况
        if startA in graph[startB]:
            return 1
        # 特判B在环中，而且环满足 >3，则永远抓不到
        if startB in circle and len(circle) > 3:
            return -1

        # 下面的情况就是：不相邻 | not(B在环中+len(circle)>3)
        disA, disB = bfs(startA, n, graph), bfs(startB, n, graph)
        # 找 B 距环的入口
        entry = min((disB[i], i) for i in circle)[1]
        # 不可能抓到了，B躲进去环里面去了
        if len(circle) > 3 and disA[entry] > disB[entry]:
            return -1
        # 下面是一定会抓到的情况；disA[i] > disB[i] + 1 关键判定
        ans = max(disA[i] for i in range(n) if disA[i] > disB[i] + 1)
        return ans
