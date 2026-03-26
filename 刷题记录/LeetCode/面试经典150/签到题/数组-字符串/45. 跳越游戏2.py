"""
https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [9999] * n
        steps[0] = 0
        maxCanJump = 0
        for i, p in enumerate(nums):
            for j in range(maxCanJump, min(n, i + p + 1)):
                steps[j] = min(steps[j], steps[i] + 1)
                if steps[-1] != 9999:
                    return steps[-1]
            maxCanJump = max(maxCanJump, p + i)
        return steps[-1]
