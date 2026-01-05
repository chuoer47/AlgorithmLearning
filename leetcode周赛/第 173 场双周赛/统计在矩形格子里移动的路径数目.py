# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

from typing import List
from functools import cache


class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        pi_cache = {}  # (i, repeat) -> prefix sum array

        @cache
        def dfs(i, j, repeat):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "#":
                return 0
            if i == n - 1 and repeat == 0:
                return 1

            if repeat == 1:
                l, r = max(0, j - d), min(m - 1, j + d)
                return (
                        get_pi(i, r, 0)
                        - get_pi(i, l - 1, 0)
                        - dfs(i, j, 0)
                ) % mod
            else:
                l, r = max(0, j + 1 - d), min(m - 1, j + d - 1)
                s0 = get_pi(i + 1, r, 0) - get_pi(i + 1, l - 1, 0)
                s1 = get_pi(i + 1, r, 1) - get_pi(i + 1, l - 1, 1)
                return (s0 + s1) % mod

        def build_prefix(i, repeat):
            arr = [0] * m
            s = 0
            for j in range(m):
                s = (s + dfs(i, j, repeat)) % mod
                arr[j] = s
            pi_cache[(i, repeat)] = arr

        def get_pi(i, j, repeat):
            if j < 0:
                return 0
            if i < 0 or i >= n:
                return 0
            key = (i, repeat)
            if key not in pi_cache:
                build_prefix(i, repeat)
            return pi_cache[key][j]

        ans = 0
        for j in range(m):
            ans = (ans + dfs(0, j, 0) + dfs(0, j, 1)) % mod

        return ans
