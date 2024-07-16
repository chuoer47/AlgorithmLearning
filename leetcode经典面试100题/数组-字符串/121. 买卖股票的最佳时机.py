"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 99999
        profit = 0
        for i in prices:
            minPrice = min(minPrice, i)
            profit = max(0, i - minPrice,profit)
        return profit
