from bisect import *
from collections import defaultdict
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
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 按节点值排序
        unions = sorted((v, i) for i, v in enumerate(nums))
        nums = [v for v, _ in unions]
        idxs = [j for _, j in unions]
        mapper = {v: i for i, v in enumerate(idxs)}

        dsu = DSU(n)

        l = 0
        # 构建连通分量
        for r, v in enumerate(nums):
            while l < r and nums[r] - nums[l] > maxDiff:
                l += 1
            dsu.union(idxs[l], idxs[r])

        # 预处理 ST 表，记录下标
        st = [[0] * 20 for _ in range(n)]
        for i in range(n):
            st[i][0] = bisect_right(nums, nums[i] + maxDiff) - 1  # 初始化长度为 1 的区间最大元素的下标
        for j in range(1, 20):
            for i in range(n):
                idx = st[i][j - 1]
                nxt_idx = st[idx][j - 1]
                st[i][j] = nxt_idx
        def check(mid, u, v):
            for i in range(19, -1, -1):
                if mid & (1 << i):
                    u = st[u][i]
            return u >= v

        def find(u, v):
            if u == v:
                return 0
            u, v = mapper[u], mapper[v]
            if u > v:
                u, v = v, u
            # 二分查找最短距离
            ans = n
            l, r = 1, n
            while l <= r:
                mid = (l + r) >> 1
                if check(mid, u, v):
                    ans = min(ans, mid)
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

        ans = []
        for u, v in queries:
            flag = dsu.find(u) == dsu.find(v)
            if not flag:
                ans.append(-1)
            else:
                dis = find(u, v)
                ans.append(dis)
        return ans
