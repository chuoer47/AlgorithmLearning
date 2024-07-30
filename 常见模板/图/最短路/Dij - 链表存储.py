from heapq import *


def Dij(weight, source, n):
    visited = [0] * (n + 10) # 这里稍微注意一下
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
    w = {
        0: [(1, 1), (2, 3), (3, 1)],
        1: [(0, 1), (2, 1)],
        2: [(0, 3), (1, 1), (3, 1)],
        3: [(0, 1), (2, 1)]
    }
    lst = Dij(w, 0, n=4)
    print(lst)
