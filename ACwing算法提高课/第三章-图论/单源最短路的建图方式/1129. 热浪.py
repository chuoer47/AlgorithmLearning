"""
https://www.acwing.com/problem/content/1131/
直接copy模板了，不自己打了
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
    t,c,source,end = map(int,input().strip().split(" "))
    weight = [[float('inf')]*(t+10) for _ in range(t+10)]
    for _ in range(c):
        rs,re,ci = map(int,input().strip().split(" "))
        weight[rs][re] = ci
        weight[re][rs] = ci
    dis = Dij(weight,source)
    print(dis[end])