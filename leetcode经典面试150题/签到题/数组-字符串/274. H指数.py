"""
https://leetcode.cn/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h += 1
        return h
