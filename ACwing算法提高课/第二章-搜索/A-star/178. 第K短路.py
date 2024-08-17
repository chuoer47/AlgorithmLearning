"""
https://www.acwing.com/problem/content/180/

A-star 第一次遇见，感觉名字好高级，学起来看不出来和star有什么关系...
理解起来花了好多时间，参考博客：https://blog.csdn.net/Zhouzi_heng/article/details/115035298
核心思想就是找到两个函数h(x),g(x)
h(x):x到目标的估计距离，h(x)的值一定要小于等于真实的x到目标的估计距离
g(x):初始点到x的真实距离
然后，根据 h(x)+g(x) 为标准，使用最小堆，第k次弹出的满足第k短路
证明过程感性理解即可，主要是找h(x)比较难，本题是是使用反向Dij作为h(x)

重要优化点：
一个重要优化是如果一个点出队K次了，他就没有必要在入队了。
"""

from heapq import *


def Dij(weight: list, source):
    """之前打的模板，直接拿来用了"""
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


def Astar(weight, hx, k, s, t):
    cnt = [0] * (n + 1)
    stack = [(0 + hx[s], 0, s)]  # 第一项是hx+gx，第二项是gx, 第三项是到达点
    while stack:
        hn, gn, now = heappop(stack)  # hn,gn = h(now),g(now)
        cnt[now] += 1
        if cnt[t] == k:
            return gn
        for edge, value in weight[now]:
            if cnt[edge] < k:
                heappush(stack, (gn + value + hx[edge], gn + value, edge))
    return -1


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))  # 录入数据
    weight = [[] for _ in range(n + 1)]  # 正向图，用来完成g(x)
    rweight = [[float("inf")] * (n + 1) for _ in range(n + 1)]  # 反向图，用来构建h(x)
    for _ in range(m):
        a, b, l = map(int, input().strip().split(" "))  # 录入数据
        weight[a].append((b, l))
        rweight[b][a] = min(rweight[b][a], l)
    s, t, k = map(int, input().strip().split(" "))  # 录入数据
    # 第一步，构建h(x)
    hx = Dij(rweight, t)
    # 第二步，完成A-star
    if s == t:
        k += 1  # 对于源点和终点一直的情况，需要+1
    ans = Astar(weight, hx, k, s, t)
    print(ans)
