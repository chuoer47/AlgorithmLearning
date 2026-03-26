"""
https://www.acwing.com/problem/content/347/
"""
from collections import Counter
from sys import setrecursionlimit

setrecursionlimit(10000000)

N = 205
weight = [[float("inf")] * N for _ in range(N)]  # 记录权重
dicId = Counter()  # 记录ID的字典


def addDict(x):
    global n
    if not dicId[x]:
        dicId[x] = n
        n += 1


def multi(a, b):
    temp = [[float("inf")] * N for _ in range(N)]  # 记录权重
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                temp[i][j] = min(temp[i][j], a[i][k] + b[k][j])
    return temp


def qmi(k):
    """快速幂函数"""
    if k == 1:
        return weight
    tem = qmi(k // 2) #节约时间开销
    if k % 2 == 0:
        return multi(tem, tem)
    else:
        return multi(multi(tem, tem), weight)


if __name__ == '__main__':
    k, t, s, e = map(int, input().strip().split(" "))  # 把n改为k
    n = 1  # 记录id下标
    # 离散化
    addDict(s), addDict(e)
    s, e = dicId[s], dicId[e]

    for _ in range(t):
        l, u, v = map(int, input().strip().split(" "))
        # 离散化
        addDict(u), addDict(v)
        u, v = dicId[u], dicId[v]
        weight[u][v] = weight[v][u] = min(weight[u][v], l)

    res = qmi(k)
    print(res[s][e])
