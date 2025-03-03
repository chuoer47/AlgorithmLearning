# 思路一:DP
# dp[i][j] 下标为i 转化为数字j 满足条件的最小操作数
# dp[i][j] = dp[i-1][j-1] + abs(nums[i] - j)
# return [ min(dp[i]]) % mod for i in range(n)]
# 难点在于如何确定j的范围 一般来说取n? max(nums)? min(nums)
# 随意取一个大数字 明显会超时
from typing import List

mod = int(1e9 + 7)

from heapq import *


class MedianFinder:

    def __init__(self):
        self.upper = []  # 小顶堆
        self.lower = []  # 大顶堆
        self.num = 0  # 记录列表数量
        self.up_num = 0  # 记录上顶堆总和
        self.down_num = 0  # 记录下顶堆总和

    def addNum(self, num: int) -> None:
        self.num += 1
        heappush(self.upper, num)
        self.up_num += num

        if self.num % 2 == 0:
            now = heappop(self.upper)
            self.up_num -= now
            heappush(self.lower, -now)
            self.down_num += now
        if self.lower and self.upper and -self.lower[0] > self.upper[0]:
            x, y = heappop(self.upper), -heappop(self.lower)
            self.up_num += y - x
            self.down_num += x - y
            heappush(self.lower, -x)
            heappush(self.upper, y)

    def findMedian(self) -> float:
        return self.upper[0]

    def getNum(self):
        return self.up_num, self.down_num

    def help_numsGame(self):
        mid = self.findMedian()
        return self.up_num - mid * (self.num - self.num // 2) + mid * (self.num // 2) - self.down_num


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [v - i for i, v in enumerate(nums)]
        helper = MedianFinder()
        ans = [0] * n
        for i, v in enumerate(nums):
            helper.addNum(v)
            ans[i] = helper.help_numsGame()%mod
        return ans
