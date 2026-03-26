"""
https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150
经典DP题目
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+10)
        for i in range(n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]