from cmath import inf
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-inf] * 3 for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i][0] = max(dp[i - 1][0], nums[i - 1]) + nums[i]
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1]) + nums[i]
            elif nums[i] < nums[i - 1]:
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]
        return max(dp[i][2] for i in range(n))
