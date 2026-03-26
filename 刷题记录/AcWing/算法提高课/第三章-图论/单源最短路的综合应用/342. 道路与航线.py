"""
https://www.acwing.com/problem/content/344/
"""
from heapq import *

bia = 1e9


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
                if w > 0:
                    heappush(stack, (dis[node] + w, p))
    return dis


if __name__ == '__main__':
    n, r, p, s = map(int, input().strip().split(" "))
    weight = dict()
    for i in range(n + 1):
        weight[i] = []
    for _ in range(r):
        x, y, t = map(int, input().strip().split(" "))
        weight[x].append((y, t))
        weight[y].append((x, t))
    for _ in range(p):
        x, y, t = map(int, input().strip().split(" "))
        weight[x].append((y, t))
    cost = Dij(weight, source=s, n=n)
    for i in range(1, n + 1):
        if cost[i] != float("inf"):
            print(cost[i])
        else:
            print("NO PATH")
