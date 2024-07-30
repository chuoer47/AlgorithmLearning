"""
https://www.acwing.com/problem/content/922/
"""

from heapq import *


def Dij(weight: list, source):
    n = len(weight)
    visited = [0] * n
    dis = [float('inf')] * n
    dis[source] = 0
    stack = [(0, source)]
    heapify(stack)
    while stack:
        price, node = heappop(stack)
        if visited[node]:
            continue
        else:
            visited[node] = 1
        for i in range(n):
            if dis[node] + weight[node][i] < dis[i]:
                dis[i] = dis[node] + weight[node][i]
                heappush(stack, (dis[node] + weight[node][i], i))
    return dis


if __name__ == '__main__':
    m, n = map(int, input().strip().split(" "))
    weight = [[float('inf')] * (n + 10) for _ in range(n + 10)]
    for _ in range(m):
        route = list(map(int, input().strip().split(" ")))
        # 录入起始站到终点站的消息
        rl = len(route)
        for i in range(rl):
            for j in range(i, rl):
                weight[route[i]][route[j]] = 1
    if n == 0:
        print(0)
        exit(1)
    dis = Dij(weight, source=1)
    if dis[n] == float("inf"):
        print("NO")
    else:
        print(dis[n] - 1)  # 减一是因为到S的那次车不算换乘！
