"""
https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxCanJump = 0
        for i, p in enumerate(nums):
            if i <= maxCanJump:
                maxCanJump = max(maxCanJump, p + i)
        return maxCanJump >= len(nums)-1
