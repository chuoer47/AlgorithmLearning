from typing import List


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


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2])
        weight = [0] * n
        size = n
        dsu = DSU(n)
        for x, y, w in edges:
            if size == k:
                break
            if dsu.union(x, y):
                size -= 1
                fx = dsu.find(x)
                weight[fx] = max(weight[fx], weight[x], weight[y], w)
        w = set([dsu.find(i) for i in range(n)])
        ans = max(weight[i] for i in w)
        return ans