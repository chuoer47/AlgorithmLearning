"""
https://www.acwing.com/problem/content/342/

越学算法越觉得自己太垃圾了
说明思路都想不到....
这神仙做法：二分+Dij
"""
from heapq import *


def Dij(bar):
    visited = [0] * (n + 1)  # 这里稍微注意一下
    dis = [float('inf')] * (n + 1)
    dis[1] = 0
    stack = [(0, 1)]
    heapify(stack)
    while stack:
        price, node = heappop(stack)
        if visited[node]:
            continue
        else:
            visited[node] = 1
        # 链表存储把这里逻辑改一下就好了
        for p, w in weight[node]:
            flag = 1 if w > bar else 0  # 把高于bar的计算为1
            if dis[node] + flag < dis[p]:
                dis[p] = dis[node] + flag
                heappush(stack, (dis[p], p))
    return dis[n] <= k


if __name__ == '__main__':
    n, p, k = map(int, input().strip().split(" "))
    weight = dict()
    for i in range(n + 1):
        weight[i] = []
    for _ in range(p):
        x, y, t = map(int, input().strip().split(" "))
        weight[x].append((y, t))
        weight[y].append((x, t))

    # 二分法，整数...
    l, r = 0, 1000010
    while l < r:
        mid = (l + r) >> 1
        if Dij(mid):
            r = mid
        else:
            l = mid + 1

    if r != 1000010:
        print(r)
    else:
        print(-1)
