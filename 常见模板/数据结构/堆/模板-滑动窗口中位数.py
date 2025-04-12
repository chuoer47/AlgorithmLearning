from collections import defaultdict
from heapq import *
from typing import List


class LazyHeap:
    def __init__(self):
        self.hq = []
        self.cnt = defaultdict(int)
        self.size = 0

    def push(self, num):
        if self.cnt[num] > 0:
            self.cnt[num] -= 1
        else:
            heappush(self.hq, num)
        self.size += 1

    def remove(self, num):
        self.size -= 1
        self.cnt[num] += 1

    def real_remove(self):
        while self.hq and self.cnt[self.hq[0]] > 0:
            self.cnt[self.hq[0]] -= 1
            heappop(self.hq)

    def top(self):
        self.real_remove()
        return self.hq[0]

    def pop(self):
        self.size -= 1
        self.real_remove()
        return heappop(self.hq)

    def pushpop(self, num):
        # 先push后pop
        self.real_remove()
        return heappushpop(self.hq, num)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        # 在维护过程中始终保持 upper.size == lower.size / upper.size + 1 == lower.size
        upper = LazyHeap()  # 上顶堆，本质小顶堆
        lower = LazyHeap()  # 下顶堆，本质大顶堆
        for i, v in enumerate(nums):
            # 1.加入
            if upper.size == lower.size:
                lower.push(-upper.pushpop(v))
            else:
                upper.push(-lower.pushpop(-v))

            if i < k - 1:
                continue
            # 2.添加答案
            if k & 1 == 1:
                ans.append(-lower.top())
            else:
                ans.append((upper.top() - lower.top()) / 2)

            # 3.删除
            del_num = nums[i - k + 1]
            if -lower.top() >= del_num:
                lower.remove(-del_num)
                if lower.size < upper.size:
                    lower.push(-upper.pop())
            else:
                upper.remove(del_num)
                if lower.size > upper.size + 1:
                    upper.push(-lower.pop())
        return ans