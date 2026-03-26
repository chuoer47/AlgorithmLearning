from collections import defaultdict
from heapq import *
from sys import setrecursionlimit

setrecursionlimit(int(1e6))

n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]


def simple40(graph):
    # 使用并查集完成
    # O(mn(m+n)logmn)

    n, m = len(graph), len(graph[0])

    def get(x, y):
        return x * m + y

    dsu = DSU(n * m + 100)
    for i in range(n):
        for j in range(m):
            for x in range(i + 1, n):
                if graph[x][j] < graph[i][j]:
                    dsu.union(get(i, j), get(x, j))
            for y in range(j + 1, m):
                if graph[i][y] < graph[i][j]:
                    dsu.union(get(i, j), get(i, y))
    cnt = defaultdict(int)
    mx = defaultdict(int)
    for i in range(n):
        for j in range(m):
            idx = get(i, j)
            cnt[dsu.find(idx)] += 1
            mx[dsu.find(idx)] = max(mx[dsu.find(idx)], graph[i][j])
    ans = 0
    for k, v in cnt.items():
        ans += v * mx[k]

    return ans / (m * n)


try:
    if n <= 100 and m <= 100:
        ans = simple40(graph)
        print('%.6f' % ans)
    else:
        ans = simple40(graph)
        print('%.6f' % ans)
except:
    ans = sum(map(sum, graph)) / (m * n)
    print('%.6f' % ans)
