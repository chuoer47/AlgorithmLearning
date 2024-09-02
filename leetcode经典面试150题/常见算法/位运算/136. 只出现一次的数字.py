"""
https://leetcode.cn/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res