from functools import cache
from typing import List


class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        @cache
        def dfs(i: int, pre: int):
            if i >= n:
                return pre
            if i + 1 >= n:
                return max(pre, nums[i])
            p = [nums[i], nums[i + 1], pre]
            p.sort()
            res = inf
            res = min(res, p[2] + dfs(i + 2, p[0]))
            res = min(res, p[1] + dfs(i + 2, p[2]))
            return res

        ans = inf
        q = [nums[0], nums[1], nums[2]]
        q.sort()
        ans = min(ans, dfs(3, q[0]) + q[2])
        ans = min(ans, dfs(3, q[2]) + q[1])
        return ans
