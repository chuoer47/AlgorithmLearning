from heapq import *


class MedianFinder:

    def __init__(self):
        self.upper = []  # 上顶堆
        self.lower = []  # 下顶堆
        self.num = 0  # 记录列表数量

    def addNum(self, num: int) -> None:
        self.num += 1
        heappush(self.upper, num)
        if self.num % 2 == 0:
            now = heappop(self.upper)
            heappush(self.lower, -now)
        while self.lower and self.upper and -self.lower[0] > self.upper[0]:
            heappush(self.lower, -heappop(self.upper))
            heappush(self.upper, -heappop(self.lower))

    def findMedian(self) -> float:
        if self.num % 2:
            return self.upper[0]
        else:
            return (self.upper[0] - self.lower[0]) / 2
