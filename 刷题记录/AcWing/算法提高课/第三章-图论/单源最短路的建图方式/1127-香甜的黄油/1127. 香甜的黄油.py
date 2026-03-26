"""
https://www.acwing.com/problem/content/description/1129/

其实之前的方法可行，但是由于建图使用矩阵，时间复杂度比较高，只需要建立列表就好了
害的我debug半天
草！
"""
from collections import Counter
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


if __name__ == '__main__':
    n, m, c = map(int, input().strip().split(" "))
    weight = dict()
    for i in range(m + 10):
        weight[i] = []
    cows = [int(input().strip()) for _ in range(n)]
    cnt = Counter(cows)
    for _ in range(c):
        rs, re, ci = map(int, input().strip().split(" "))
        weight[rs].append((re,ci))
        weight[re].append((rs,ci))
    # 获取所有牛的距离矩阵
    dis = [0] * (m + 10)
    for cow, repeat in cnt.items():
        lst = Dij(weight, source=cow,n=m)
        for i in range(m + 10):
            dis[i] += lst[i] * repeat
    print(min(dis))
