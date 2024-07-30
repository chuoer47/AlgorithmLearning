"""
https://www.acwing.com/problem/content/description/905/
"""

from heapq import *


def Dij(down: int, up: int, source=0):
    visited = [0] * (n+1)
    dis = [float('inf')] * (n+1)
    dis[source] = 0
    stack = [(0, source)]
    heapify(stack)
    while stack:
        price, node = heappop(stack)
        if visited[node]:
            continue
        else:
            visited[node] = 1
        for i in range(n+1):
            if (down <= level[i] <= up or i==0) and dis[node] + weight[node][i] < dis[i]:
                dis[i] = dis[node] + weight[node][i]
                heappush(stack, (dis[node] + weight[node][i], i))
    return dis[1]


if __name__ == '__main__':
    m, n = map(int, input().strip().split(" "))
    # 创建数组
    weight = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n+1):
        weight[i][i] = 0
    level = [0] * (n + 1)
    # 数据录入
    for i in range(1, n + 1):  # 物品编号
        p, l, x = map(int, input().strip().split(" "))
        level[i] = l  # 录入数据
        weight[0][i] = p  # 录入等级
        for _ in range(x):
            t, v = map(int, input().strip().split(" "))
            weight[t][i] = v
    # 暴力枚举等级 这个好巧妙 老想不到
    ans = float("inf")
    for i in range(level[1] - m, level[1] + 1):
        ans = min(ans, Dij(i, i + m))
    print(ans)
