# 4e8的时间复杂度过不了..有一点无语
from bisect import bisect_left
from cmath import inf
from functools import cache
from typing import List

min1 = lambda x, y: x if x < y else y


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # 从(x,y)到(0,0)，剩余传送次数为cnt次的最小总成本
        n, m = len(grid), len(grid[0])
        nums = []
        for i in range(n):
            for j in range(m):
                nums.append((i, j, grid[i][j]))
        nums.sort(key=lambda x: x[2])
        xy = [(x, y) for x, y, _ in nums]
        values = [v for _, _, v in nums]

        @cache
        def getPi(idx, cnt):
            # 用来缓解 for i in range(idx,n*m)
            if idx == m * n:
                return inf
            x, y = xy[idx]
            return min1(dfs(x, y, cnt - 1), getPi(idx + 1, cnt))

        @cache
        def dfs(x, y, cnt):
            # 边界条件
            if x < 0 or y < 0 or cnt < 0:
                return inf
            if x == 0 and y == 0:
                return 0
            ans = min1(dfs(x - 1, y, cnt), dfs(x, y - 1, cnt)) + grid[x][y]
            # 开始传送，去找 >= (x,y)
            idx = bisect_left(values, grid[x][y])
            ans = min1(ans, getPi(idx, cnt))
            return ans

        ans = dfs(n - 1, m - 1, k)
        dfs.cache_clear()
        getPi.cache_clear()
        return ans
