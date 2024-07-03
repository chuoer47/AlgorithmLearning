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


w = [[0, 1, 3, 1],
     [1, 0, 1, 999],
     [3, 1, 0, 1],
     [1, 999, 1, 0]]
lst = Dij(w, 0)
print(lst)
