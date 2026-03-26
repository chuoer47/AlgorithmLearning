"""
https://www.acwing.com/problem/content/description/1377/
"""
from heapq import *


def s2n(s):
    if 'a' <= s <= 'z':
        return ord(s) - ord('a')
    if 'A' <= s <= 'Z':
        return ord(s) - ord('A') + 26


def n2s(n):
    return chr(ord('A') + n)


n = int(input())
w = [[float('inf')] * 52 for _ in range(52)]
for _ in range(n):
    begin, end, ww = input().split(" ")
    begin, end, ww = s2n(begin), s2n(end), int(ww)
    w[begin][end] = min(ww, w[begin][end])  # 这里很关键
    w[end][begin] = min(ww, w[begin][end])  # 这个很关键


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


weight = Dij(weight=w, source=-1)
res = weight[26:-1]
nw = float('inf')
ni = -1
for i, v in enumerate(res):
    if v < nw:
        nw = v
        ni = i

print(n2s(ni), nw)
