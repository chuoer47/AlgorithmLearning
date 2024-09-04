# 深搜尽力啦，完成不了捏

from typing import List


class Solution:
    dic = {}

    def maxProfit(self, prices: List[int]) -> int:
        self.dic = {}
        if not prices:
            return 0
        ans = 0
        n = len(prices)
        pre, right = float("inf"), 0
        while right < n:
            while right + 1 < n and prices[right + 1] > prices[right]:
                pre = min(pre,prices[right])
                right += 1
            if prices[right] > pre:
                ans = max(ans, prices[right] - pre + self.dfs(prices, right + 1))
            right = right + 1
        return ans

    def dfs(self, prices, pivot):
        if pivot in self.dic:
            return self.dic[pivot]
        minPrice = float("inf")
        profit = 0
        for i in range(pivot, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(0, prices[i] - minPrice, profit)
        self.dic[pivot] = profit
        return profit
