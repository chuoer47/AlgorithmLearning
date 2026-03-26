"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = prices[0]
        profit = 0
        for i in prices:
            if maxPrice <= i:
                maxPrice = i
            else:
                profit += max(0, maxPrice - minPrice)
                minPrice = i
                maxPrice = i
        profit += max(0, maxPrice - minPrice)
        return profit
