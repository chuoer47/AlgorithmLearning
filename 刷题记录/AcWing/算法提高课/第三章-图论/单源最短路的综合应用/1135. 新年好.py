"""
https://www.acwing.com/problem/content/1137/
"""

from heapq import *
from itertools import permutations


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


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    weight = dict()
    for i in range(n + 10):
        weight[i] = []
    a, b, c, d, e = map(int, input().strip().split(" "))
    for _ in range(m):
        x, y, t = map(int, input().strip().split(" "))
        weight[x].append((y, t))
        weight[y].append((x, t))

    # 统计不同的距离
    dis = dict()
    for i in [1, a, b, c, d, e]:
        dis[i] = Dij(weight, source=i, n=n)

    # 一共120种情况，直接遍历一遍就好了
    ans = float("inf")
    for seq in permutations([a, b, c, d, e], 5):
        cost = dis[1][seq[0]]
        for i in range(1, 5):
            cost += dis[seq[i - 1]][seq[i]]
        ans = min(cost, ans)

    # 输出答案
    print(ans)
