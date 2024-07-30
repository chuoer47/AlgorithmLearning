"""
https://www.acwing.com/problem/content/1128/
最小化损失即可
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
            tem = dis[node] + (1-dis[node])*weight[node][i] # 改变一下这里
            if tem < dis[i]:
                dis[i] = tem
                heappush(stack, (tem, i))
    return dis


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    weight = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        rs, re, ci = map(int, input().strip().split(" "))
        weight[rs][re] = ci*0.01
        weight[re][rs] = ci*0.01
    source,end = map(int, input().strip().split(" "))
    dis = Dij(weight, source=source)
    print("{:.8f}".format(100/(1-dis[end])))