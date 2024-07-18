"""
https://leetcode.cn/problems/single-number-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b