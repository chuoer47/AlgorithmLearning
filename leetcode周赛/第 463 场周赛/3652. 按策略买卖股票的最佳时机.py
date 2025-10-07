from itertools import accumulate
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ppi = list(accumulate(prices)) + [0]
        profit = [i * j for i, j in zip(prices, strategy)]
        pi = list(accumulate(profit, initial=0))
        rpi = list(accumulate(profit[::-1], initial=0))[::-1]
        n = len(prices)
        ans = pi[n]
        for i in range(k - 1, n):
            # [l,r]
            l = i - (k - 1)
            r = i
            m = i - (k // 2 - 1)
            left = pi[l]
            right = rpi[r + 1]
            mid = ppi[r] - ppi[m - 1]
            ans = max(ans, left + right + mid)
        return ans
