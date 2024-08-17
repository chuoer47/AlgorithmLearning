"""
给出一个图，问其中的由 n 个节点构成的边权和最小的环 (n > 3) 是多大。
"""

maxn = 100
val = [[0 for i in range(maxn + 1)] for j in range(maxn + 1)]  # 原图的邻接矩阵


def floyd(n):
    dis = [[0 for i in range(maxn + 1)] for j in range(maxn + 1)]  # 最短路矩阵
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = val[i][j]  # 初始化最短路矩阵
    ans = inf
    for k in range(1, n + 1):
        for i in range(1, k):
            for j in range(1, i):
                ans = min(ans, dis[i][j] + val[i][k] + val[k][j])  # 更新答案
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(
                    dis[i][j], dis[i][k] + dis[k][j]
                )  # 正常的 floyd 更新最短路矩阵
    return ans
