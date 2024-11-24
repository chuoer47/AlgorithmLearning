from functools import cache
from math import inf
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        @cache
        def dfs(i: int, j: int) -> int:
            if not (n - 1 - i <= j < n):
                return -inf
            if i == 0:
                return fruits[i][j]
            return max(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + fruits[i][j]

        ans = sum(row[i] for i, row in enumerate(fruits))
        ans += dfs(n - 2, n - 1)  # 从下往上走，方便 1:1 翻译成递推
        dfs.cache_clear()
        fruits = list(zip(*fruits))  # 按照主对角线翻转
        return ans + dfs(n - 2, n - 1)
