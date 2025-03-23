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
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n, m = len(properties), len(properties[0])
        properties = [set(row) for row in properties]
        union = DSU(n)

        for i in range(n):
            for j in range(i + 1, n):
                if len(properties[i] & properties[j]) >= k:
                    union.union(i, j)
        par = set()
        for i in range(n):
            par.add(union.find(i))
        return len(par)
