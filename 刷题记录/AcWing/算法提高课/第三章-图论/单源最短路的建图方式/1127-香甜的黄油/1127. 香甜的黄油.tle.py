"""
https://www.acwing.com/problem/content/1129/
这道题目，不同一个牛在同一个牧场也要重复算
使用Dij算法会超时，烦诶
"""

from heapq import *
from collections import Counter


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
    n, m, c = map(int, input().strip().split(" "))
    weight = [[float('inf')] * (m + 10) for _ in range(m + 10)]
    cows = [int(input().strip()) for _ in range(n)]
    cnt = Counter(cows)
    for _ in range(c):
        rs, re, ci = map(int, input().strip().split(" "))
        weight[rs][re] = ci
        weight[re][rs] = ci
    # 获取所有牛的距离矩阵
    dis = [0] * (m + 10)
    for cow, repeat in cnt.items():
        lst = Dij(weight, source=cow)
        for i in range(m + 10):
            dis[i] += lst[i] * repeat
    print(min(dis))
